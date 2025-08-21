import pandas as pd
from order_items.cleaner import clean_csv

def test_clean_csv(tmp_path):
    test_csv = tmp_path / "test.csv"
    pd.DataFrame({
        "item_price": [10, 10, None],
        "item_promo_discount": [2, 2, None],
        "created_at": ["2021-01-01", "2021-01-01", None],
    }).to_csv(test_csv, index=False)

    df, stats = clean_csv(test_csv, tmp_path)

    assert stats["total_empty_rows_removed"] == 1
    assert stats["total_duplicate_rows_removed"] == 1
    assert stats["total_usable_rows"] == 1
    assert (tmp_path / "discarded_rows.csv").exists()

