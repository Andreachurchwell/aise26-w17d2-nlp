import os
import numpy as np
from datasets import load_dataset
from transformers import (
    AutoTokenizer,
    AutoModelForSequenceClassification,
    DataCollatorWithPadding,
    TrainingArguments,
    Trainer,
)
import evaluate


def make_binary(ds):
    """
    AG News labels:
      0 World, 1 Sports, 2 Business, 3 Sci/Tech
    Convert to binary:
      1 = Sports
      0 = Not Sports
    """
    def to_binary(example):
        example["label"] = 1 if example["label"] == 1 else 0
        return example
    return ds.map(to_binary)


def word_count_slice(example):
    n = len(example["text"].split())
    if n <= 12:
        return "short"
    if n >= 40:
        return "long"
    return "mid"


def negation_slice(example):
    t = example["text"].lower()
    neg_words = [" not ", " never ", " no ", "n't"]
    return "negation" if any(w in t for w in neg_words) else "no_negation"


def punctuation_slice(example):
    t = example["text"]
    return "punctuation" if ("!" in t or "?" in t) else "no_punctuation"


def compute_metrics(eval_pred):
    metric_acc = evaluate.load("accuracy")
    metric_f1 = evaluate.load("f1")
    logits, labels = eval_pred
    preds = np.argmax(logits, axis=-1)
    acc = metric_acc.compute(predictions=preds, references=labels)["accuracy"]
    f1 = metric_f1.compute(predictions=preds, references=labels)["f1"]
    return {"accuracy": acc, "f1": f1}


def main():
    model_name = "distilbert-base-uncased"

    # Load dataset
    ds = load_dataset("ag_news")

    # Binary labels (Sports vs Not Sports)
    ds = make_binary(ds)

    # Small subsets for speed (YOU CAN ADJUST)
    train_ds = ds["train"].shuffle(seed=42).select(range(3000))
    eval_ds = ds["test"].shuffle(seed=42).select(range(800))

    # Add slice tags (for later slice evaluation)
    def add_slices(example):
        example["slice_len"] = word_count_slice(example)
        example["slice_neg"] = negation_slice(example)
        example["slice_punc"] = punctuation_slice(example)
        return example

    train_ds = train_ds.map(add_slices)
    eval_ds = eval_ds.map(add_slices)

    tokenizer = AutoTokenizer.from_pretrained(model_name)

    def tokenize(batch):
        return tokenizer(batch["text"], truncation=True)

    train_tok = train_ds.map(tokenize, batched=True)
    eval_tok = eval_ds.map(tokenize, batched=True)

    data_collator = DataCollatorWithPadding(tokenizer=tokenizer)

    model = AutoModelForSequenceClassification.from_pretrained(model_name, num_labels=2)

    args = TrainingArguments(
        output_dir="runs/run1",
        num_train_epochs=1,
        per_device_train_batch_size=16,
        per_device_eval_batch_size=32,
        learning_rate=2e-5,
        logging_steps=25,
        report_to="none",
        seed=42,
    )

    trainer = Trainer(
        model=model,
        args=args,
        train_dataset=train_tok,
        eval_dataset=eval_tok,
        tokenizer=tokenizer,
        data_collator=data_collator,
        compute_metrics=compute_metrics,
    )

    # Train once
    trainer.train()

    # Final eval
    results = trainer.evaluate()
    print("\nFINAL EVAL:", results)

    # Save artifacts (required)
    os.makedirs("artifacts/model", exist_ok=True)
    os.makedirs("artifacts/tokenizer", exist_ok=True)
    trainer.save_model("artifacts/model")
    tokenizer.save_pretrained("artifacts/tokenizer")

    # Save predictions for failures + slice metrics later
    preds_output = trainer.predict(eval_tok)
    logits = preds_output.predictions
    preds = np.argmax(logits, axis=-1)
    labels = np.array(preds_output.label_ids)

    np.save("runs/run1/preds.npy", preds)
    np.save("runs/run1/labels.npy", labels)

    # Also save eval texts + slice tags to rebuild FAILURES + slice metrics
    eval_tok.select(range(len(eval_tok))).to_json("runs/run1/eval_with_slices.jsonl")

    print("\nSaved model -> artifacts/model")
    print("Saved tokenizer -> artifacts/tokenizer")
    print("Saved eval records -> runs/run1/eval_with_slices.jsonl")


if __name__ == "__main__":
    main()