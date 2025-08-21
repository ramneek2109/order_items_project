# Order Items Processor

Process large order-items CSVs (~1 GB): download (or reuse local), clean, log discarded rows, and produce monthly metrics.

## Quick Start

```bash
# 1) create & activate venv (if not already)
python3 -m venv ven && source ven/bin/activate

# 2) install deps
pip install pandas requests pytest

# 3) run (URL or local path both work)
PYTHONPATH=. python -m order_items.cli "https://storage.googleapis.com/nozzle-csv-exports/testing-data/order_items_data_2_.csv"
# or reuse an already-downloaded file
PYTHONPATH=. python -m order_items.cli data/order_items_YYYYMMDD_HHMMSS.csv

