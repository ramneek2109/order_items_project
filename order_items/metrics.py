import pandas as pd
from pathlib import Path
import json

def compute_metrics(df: pd.DataFrame, out_dir: Path, stats: dict):
    out_dir.mkdir(parents=True, exist_ok=True)

    # Ensure numeric columns are properly converted
    num_cols = [
        "item_price",
        "item_promo_discount",
    ]
    for col in num_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

    # Convert created_at into month-year
    df["month_year"] = pd.to_datetime(
        df["purchased_at"], errors="coerce", format="mixed"
    ).dt.to_period("M").astype(str)

    # Aggregate metrics
    grouped = df.groupby("month_year").agg(
        total_items_promo_discount=("item_promo_discount", "sum"),
        total_items_price=("item_price", "sum"),
    ).reset_index()

    # Adjust total_items_price
    grouped["total_items_price"] = (
        grouped["total_items_price"] - grouped["total_items_promo_discount"]
    )

    # Save outputs
    grouped.to_csv(out_dir / "monthly_metrics.csv", index=False)

    with open(out_dir / "processing_stats.json", "w") as f:
        json.dump(stats, f, indent=4)

