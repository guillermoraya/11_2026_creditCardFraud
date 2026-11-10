# Credit Card Fraud Kaggle Competition - November 2026
## Playground Series - Season 6 Episode 11

The goal of this competition is predicting credit card fraud. Submissions are evaluated on area under the ROC curve between the predicted probability and the observed target. For each id in the test set, we must predict a probability for the is_fraud. The file should contain a header and have the following format:

```
id,is_fraud
699960,0.3
699961,0.9
699962,0.2
etc.
```


## Folder structure
```
11_2026_creditCardFraud/
├── README.md                 # link, metric (AUC-style on probabilities), CV scheme, experiment log
├── pyproject.toml            # uv-managed env
├── Makefile
├── .gitignore                # data/, outputs/, .venv/, .DS_Store
├── configs/
│   ├── base.yaml             # target=is_fraud, seed, n_folds, paths
│   └── exp001_lgbm.yaml
├── data/
│   ├── raw/                  # move train/test/sample_submission here
│   └── processed/            # folds.csv, feature parquet files
├── notebooks/00_eda.ipynb
├── src/ccfraud/
│   ├── config.py, data.py, features.py, models.py, cv.py, metrics.py
├── scripts/  train.py, predict.py, submit.py
├── outputs/exp001/           # oof.npy, test_preds.npy, metrics.json, config.yaml
└── submissions/
```