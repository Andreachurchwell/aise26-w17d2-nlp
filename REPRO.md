# REPRO

## Environment
- OS: Windows (Git Bash)
- Python: (run `python --version` and paste here)
- Hardware: laptop CPU (no GPU)
- Libraries: see requirements.txt (frozen)

## Exact commands

### 1) Activate environment
```bash
source venv/Scripts/activate
```
### Train(One Run)
```
python train.py
```
### Generate Evidence Bundles
```
python make_evidence.py
```
### Outputs
- Saved model: artifacts/model/
- Saved tokenizer: artifacts/tokenizer/
- Eval records with slice tags: runs/run1/eval_with_slices.jsonl
- Evidence: METRICS.md, FAILURES.md, LIMITATIONS.md

## 2) Fill your Python version (one command)

Run:
```bash
python --version
```