import os
from order_items.downloader import download_csv
from order_items.cleaner import clean_csv
from order_items.metrics import compute_metrics
from pathlib import Path

def main():
    import sys
    url = sys.argv[1]
    out_dir = Path("data")
    os.makedirs(out_dir, exist_ok=True)

    # Check if file already exists
    existing_files = [f for f in os.listdir(out_dir) if f.startswith("order_items_") and f.endswith(".csv")]
    if existing_files:
        print("✅ Using existing file:", existing_files[-1])
        csv_path = os.path.join(out_dir, existing_files[-1])
    else:
        csv_path = download_csv(url, out_dir)

    df, stats = clean_csv(csv_path, out_dir)
    compute_metrics(df, out_dir, stats)

if __name__ == "__main__":
    main()

