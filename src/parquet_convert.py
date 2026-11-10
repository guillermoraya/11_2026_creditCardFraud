import pandas as pd

for name in ["train", "test", "sample_submission"]:
    pd.read_csv(f"data/raw/{name}.csv").to_parquet(f"data/processed/{name}.parquet", index=False)