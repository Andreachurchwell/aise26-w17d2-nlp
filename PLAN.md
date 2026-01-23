# PLAN

## Goal
Produce a training PR that a reviewer can audit quickly (config + evidence + limitations).

## Model choice
- Base model: distilbert-base-uncased
- Why this model:
  - Small and fast enough for a single-run fine-tune on a laptop CPU
  - Strong baseline for text classification
  - Easy to reproduce with common Hugging Face tooling

## Fine-tuning approach decision (LoRA vs Full)
I used: Full fine-tune (no LoRA)

Reasoning:
- Keep the run simple and auditable (fewer moving parts than LoRA/PEFT)
- One small subset + 1 epoch fits the deadline and CPU constraints
- Evidence focus (slices + failures) matters more than peak performance

## Dataset + task
- Dataset: AG News (Hugging Face)
- Task: Binary classification
  - Sports = 1 (original label 1)
  - Not Sports = 0 (original labels 0,2,3)

## Evaluation slices (3)
Computed on the same eval subset using simple, explicit rules stored with each record:

1) Slice A (Length)
   - Short: ≤ 12 words
   - Mid: 13–39 words
   - Long: ≥ 40 words

2) Slice B (Negation)
   - Negation present if text contains any of:
     {not, never, no, n't} (case-insensitive)

3) Slice C (Punctuation)
   - Emphasis present if text contains '!' or '?'

## Success metric
Primary metric: Accuracy (with F1 as supporting metric)
Target: >= 0.90 accuracy on eval subset

## What will be saved
- artifacts/model (trained model)
- artifacts/tokenizer (tokenizer)
- Evidence bundle: METRICS.md, FAILURES.md, LIMITATIONS.md, REPRO.md