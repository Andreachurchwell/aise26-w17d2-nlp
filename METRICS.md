# METRICS
## Overall (eval set)
| Metric | Value |
|---|---:|
| Accuracy | 0.985 |
| F1 (Sports=1) | 0.970 |

## Slice results
| Slice | Definition | N | Accuracy | F1 |
|---|---|---:|---:|---:|
| Slice A | Length slice (short/mid/long) – reported group: **slice_len=mid** | 461 | 0.985 | 0.971 |
| Slice B | Negation keywords present vs not – reported group: **slice_neg=no_negation** | 733 | 0.986 | 0.972 |
| Slice C | Punctuation emphasis (! or ?) vs not – reported group: **slice_punc=no_punctuation** | 761 | 0.986 | 0.971 |

## Notes
- Dataset: AG News converted to binary classification: Sports (1) vs Not Sports (0).
- Eval subset: 800 examples; Train subset: 3000 examples; 1 epoch.
- Slice tags were computed using simple string/length rules stored in `runs/run1/eval_with_slices.jsonl`.

**Because AG News labels reflect editorial topic categories, some sports-adjacent articles are labeled Not Sports, which contributes to observed failures.**