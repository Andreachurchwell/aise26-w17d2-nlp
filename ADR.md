# ADR: Fine-tuning Strategy Decision

## Context
We need one reviewable NLP fine-tuning run with saved artifacts and slice-based evaluation evidence.

## Decision
I chose full fine-tuning (not LoRA) using distilbert-base-uncased on a small subset.

## Rationale
- Reviewability: full fine-tune uses a standard Trainer workflow and the saved artifacts are straightforward to audit
- Constraints: deadline + laptop CPU means a small subset and 1 epoch is practical
- Evidence-first: the goal is auditable metrics + failures + limitations, not max leaderboard performance

## Consequences
Positive:
- Simple implementation and reproducible artifacts
- Enough signal to produce slice metrics and failure analysis

Negative / Tradeoffs:
- Not optimized for speed/memory like LoRA
- Results are from a subset, so they may not match full-dataset performance

## Alternatives considered
- LoRA/PEFT: faster and lighter, but adds complexity (adapter configs/merging) for a single-run audit-focused assignment.
