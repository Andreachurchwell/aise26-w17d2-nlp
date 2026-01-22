import json
import numpy as np
from pathlib import Path

def f1_binary(y_true, y_pred):
    # positive class = 1 (Sports)
    tp = sum((t == 1 and p == 1) for t, p in zip(y_true, y_pred))
    fp = sum((t == 0 and p == 1) for t, p in zip(y_true, y_pred))
    fn = sum((t == 1 and p == 0) for t, p in zip(y_true, y_pred))
    if tp == 0:
        return 0.0
    precision = tp / (tp + fp) if (tp + fp) else 0.0
    recall = tp / (tp + fn) if (tp + fn) else 0.0
    return 0.0 if (precision + recall) == 0 else (2 * precision * recall) / (precision + recall)

def accuracy(y_true, y_pred):
    return sum(t == p for t, p in zip(y_true, y_pred)) / len(y_true) if y_true else 0.0

def load_jsonl(path):
    rows = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            rows.append(json.loads(line))
    return rows

def slice_metrics(rows, y_true, y_pred, slice_key):
    # compute metrics for each value of rows[i][slice_key]
    groups = {}
    for i, r in enumerate(rows):
        k = r.get(slice_key, "UNKNOWN")
        groups.setdefault(k, []).append(i)

    out = []
    for k, idxs in groups.items():
        t = [int(y_true[i]) for i in idxs]
        p = [int(y_pred[i]) for i in idxs]
        out.append({
            "slice": f"{slice_key}={k}",
            "n": len(idxs),
            "acc": accuracy(t, p),
            "f1": f1_binary(t, p)
        })
    # stable order: biggest group first
    out.sort(key=lambda d: d["n"], reverse=True)
    return out

def failure_type(row):
    # simple labeling rules (good enough for assignment)
    if row.get("slice_neg") == "negation":
        return "Negation confusion"
    if row.get("slice_punc") == "punctuation":
        return "Punctuation / emphasis"
    if row.get("slice_len") in ("short", "long"):
        return "Length sensitivity"
    return "Ambiguous / context-dependent"

def main():
    base = Path("runs/run1")
    eval_path = base / "eval_with_slices.jsonl"
    preds_path = base / "preds.npy"
    labels_path = base / "labels.npy"

    rows = load_jsonl(eval_path)
    y_pred = np.load(preds_path).tolist()
    y_true = np.load(labels_path).tolist()

    assert len(rows) == len(y_true) == len(y_pred), "Eval rows / preds / labels length mismatch"

    overall_acc = accuracy(y_true, y_pred)
    overall_f1 = f1_binary(y_true, y_pred)

    # 3 slices you created
    slices = []
    slices += slice_metrics(rows, y_true, y_pred, "slice_len")
    slices += slice_metrics(rows, y_true, y_pred, "slice_neg")
    slices += slice_metrics(rows, y_true, y_pred, "slice_punc")

    # Pick top 3 slice lines (one per slice family) for METRICS table:
    # We'll select the biggest group for each slice_key
    def biggest_for(key):
        m = slice_metrics(rows, y_true, y_pred, key)
        return m[0] if m else None

    s_len = biggest_for("slice_len")
    s_neg = biggest_for("slice_neg")
    s_punc = biggest_for("slice_punc")

    # Write METRICS.md
    metrics_md = []
    metrics_md.append("# METRICS\n")
    metrics_md.append("## Overall (eval set)\n")
    metrics_md.append("| Metric | Value |\n|---|---:|\n")
    metrics_md.append(f"| Accuracy | {overall_acc:.3f} |\n")
    metrics_md.append(f"| F1 (Sports=1) | {overall_f1:.3f} |\n")

    metrics_md.append("\n## Slice results\n")
    metrics_md.append("| Slice | Definition | N | Accuracy | F1 |\n|---|---|---:|---:|---:|\n")
    if s_len:
        metrics_md.append(f"| Slice A | Length slice (short/mid/long) – reported group: **{s_len['slice']}** | {s_len['n']} | {s_len['acc']:.3f} | {s_len['f1']:.3f} |\n")
    if s_neg:
        metrics_md.append(f"| Slice B | Negation keywords present vs not – reported group: **{s_neg['slice']}** | {s_neg['n']} | {s_neg['acc']:.3f} | {s_neg['f1']:.3f} |\n")
    if s_punc:
        metrics_md.append(f"| Slice C | Punctuation emphasis (! or ?) vs not – reported group: **{s_punc['slice']}** | {s_punc['n']} | {s_punc['acc']:.3f} | {s_punc['f1']:.3f} |\n")

    metrics_md.append("\n## Notes\n")
    metrics_md.append("- Dataset: AG News converted to binary classification: Sports (1) vs Not Sports (0).\n")
    metrics_md.append("- Eval subset: 800 examples; Train subset: 3000 examples; 1 epoch.\n")
    metrics_md.append("- Slice tags were computed using simple string/length rules stored in `runs/run1/eval_with_slices.jsonl`.\n")

    Path("METRICS.md").write_text("".join(metrics_md), encoding="utf-8")

    # Build FAILURES.md (10 misclassified examples)
    failures = []
    for i, row in enumerate(rows):
        if int(y_true[i]) != int(y_pred[i]):
            failures.append((i, row))

    failures_md = []
    failures_md.append("# FAILURES (10)\n\n")
    failures_md.append("Each example below is a misclassification from the eval subset. Failure types are heuristic labels.\n\n")

    if not failures:
        failures_md.append("No failures found in the sampled eval subset.\n")
    else:
        for j, (i, row) in enumerate(failures[:10], start=1):
            ftype = failure_type(row)
            text = row.get("text", "").replace("\n", " ").strip()
            true_lbl = "Sports" if int(y_true[i]) == 1 else "Not Sports"
            pred_lbl = "Sports" if int(y_pred[i]) == 1 else "Not Sports"
            failures_md.append(f"## {j}) Failure type: {ftype}\n")
            failures_md.append(f"- Text: \"{text}\"\n")
            failures_md.append(f"- True label: {true_lbl}\n")
            failures_md.append(f"- Predicted: {pred_lbl}\n")
            failures_md.append(f"- Slice tags: len={row.get('slice_len')}, neg={row.get('slice_neg')}, punc={row.get('slice_punc')}\n\n")

    Path("FAILURES.md").write_text("".join(failures_md), encoding="utf-8")

    print("Wrote METRICS.md and FAILURES.md")
    print(f"Overall accuracy={overall_acc:.3f}, f1={overall_f1:.3f}")
    print(f"Total failures in eval subset: {len(failures)}")

if __name__ == "__main__":
    main()