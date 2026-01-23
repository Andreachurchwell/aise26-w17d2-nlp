# REPRO

## Environment
- OS: Windows (Git Bash)
- Python: 3.12.3
- Hardware: laptop CPU (no GPU)
- Libraries: see requirements.txt (frozen)


## Dataset + Label Mapping

This run uses the Hugging Face `ag_news` dataset.

Original labels:
- 0 = World
- 1 = Sports
- 2 = Business
- 3 = Sci/Tech

Binary mapping used:
- Sports (1): original label == 1
- Not Sports (0): original label in {0, 2, 3}

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