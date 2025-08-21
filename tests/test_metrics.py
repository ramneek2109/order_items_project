import pandas as pd
from order_items.metrics import compute_metrics

def test_compute_metrics(tmp_path):
    df = pd.DataFrame({
        "item_price": [100, 200],
        "item_promo_discount": [10, 20],
        "created_at": ["2021-01-01", "2021-02-01"],
    })

    stats = {"total_rows": 2}
    compute_metrics(df, tmp_path, stats)

    output_file = tmp_path / "monthly_metrics.csv"
    assert output_file.exists()

    # Verify content
    out_df = pd.read_csv(output_file)
    assert "month_year" in out_df.columns
    assert "total_items_price" in out_df.columns

