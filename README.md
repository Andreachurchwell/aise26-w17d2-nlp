# Reviewable NLP Fine-Tuning Run (Sports Classification)

This repository contains a **single, reviewable Natural Language Processing (NLP) fine-tuning run** designed to be easy to audit. The goal is not maximum performance, but **clear decisions, transparent evaluation, and honest limitations**.

---

## What is NLP?

**Natural Language Processing (NLP)** is the field of machine learning focused on working with human language (text).  
In this project, NLP is used to **classify text** by learning patterns in words, phrases, and sentence structure.

---

## What this project does

I fine-tuned a pre-trained language model to perform a **binary text classification task**:

- **Sports (1)**  
- **Not Sports (0)**

The model was trained on sports-related news headlines and short articles, then evaluated both **overall** and across **specific slices of the data** to understand where it performs well and where it fails.

---

## Model & Data

- **Base model:** `distilbert-base-uncased`
- **Dataset:** AG News (Hugging Face), converted to binary classification  
- **Training setup:**
  - 3,000 training examples
  - 800 evaluation examples
  - 1 training epoch
  - CPU-only (laptop)

A small subset was intentionally used to keep the run fast, reproducible, and reviewable.

---

## What was evaluated

### Overall performance
- Accuracy and F1 score on the evaluation subset

### Slice-based evaluation
To understand model behavior beyond a single metric, performance was also evaluated on:
- **Text length** (short / medium / long)
- **Negation presence** (e.g., “not”, “never”)
- **Punctuation emphasis** (e.g., `!`, `?`)

### Failure analysis
Misclassified examples were collected and labeled with likely failure types (e.g., negation confusion, ambiguity, length sensitivity).

---

## Key artifacts

- `artifacts/model/` – trained model weights  
- `artifacts/tokenizer/` – tokenizer used during training  

---

## Evidence files

| File             | Purpose                                                 |
|------------------|---------------------------------------------------------|
| `PLAN.md`        | Experiment plan and success criteria                    |
| `ADR.md`         | Main tradeoff decision (full fine-tune vs alternatives) |
| `METRICS.md`     | Overall and slice-based evaluation metrics              |
| `FAILURES.md`    | 10 misclassified examples with failure labels           |
| `LIMITATIONS.md` | Known weaknesses and constraints                        |
| `REPRO.md`       | Exact commands and environment details                  |

---

## Reproducibility

This run can be reproduced end-to-end using the commands in `REPRO.md`.  
Dependencies are captured in `requirements.txt`, and all outputs needed for review are included in this repository.

### **Note: Model artifacts are generated locally under artifacts/ but are not committed because GitHub rejects files larger than 100MB. The run can be reproduced using the commands in REPRO.md.**
---

## Why this structure

This project is structured to mirror **real-world ML review practices**:
- one controlled training run
- explicit decisions
- slice-based analysis
- failure inspection
- clear limitations

The emphasis is on **auditability and clarity**, not leaderboard optimization.