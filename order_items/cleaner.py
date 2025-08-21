import pandas as pd
from pathlib import Path

def clean_csv(file_path: Path, out_dir: Path):
    out_dir.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(file_path)

    total_rows = len(df)

    empty_rows = df[df.isna().all(axis=1)]
    df = df.dropna(how="all")

    duplicates = df[df.duplicated()]
    df = df.drop_duplicates()

    discarded = pd.concat([empty_rows, duplicates])
    discarded.to_csv(out_dir / "discarded_rows.csv", index=False)

    stats = {
        "total_rows": int(total_rows),
        "total_empty_rows_removed": int(len(empty_rows)),
        "total_invalid_rows_discarded": 0,  # can extend later
        "total_duplicate_rows_removed": int(len(duplicates)),
        "total_usable_rows": int(len(df)),
    }

    return df, stats

