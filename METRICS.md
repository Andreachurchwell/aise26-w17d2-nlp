# METRICS

## Overall Performance (Eval Set)

| Metric   | Value |
|----------|------:|
| Accuracy | 0.985 |
| F1 Score | 0.970 |

---

## Slice-Based Results

Each slice is evaluated on the same 800-example evaluation subset.

| Slice | Description                                                | N   | Accuracy | F1    |
|-------|------------------------------------------------------------|-----|----------|-------|
| A     | **Medium-length headlines** (neither short nor long)       | 461 | 0.985    | 0.971 |
| B     | **No negation present** (no “not”, “never”, “no”, “n’t”)   | 733 | 0.986    | 0.972 |
| C     | **No punctuation emphasis** (no `!` or `?`)                | 761 | 0.986    | 0.971 |

---

## Notes

- **Dataset:** AG News, converted to binary classification  
  - Sports = 1  
  - Not Sports = 0  
- **Training setup:**  
  - Train subset: 3,000 examples  
  - Eval subset: 800 examples  
  - Epochs: 1  
- **Slice definitions:**  
  - Length slices based on word count  
  - Negation detected via keyword matching  
  - Punctuation emphasis detected via `!` or `?`  
- Slice tags are stored with each eval example in  
  `runs/run1/eval_with_slices.jsonl`.
