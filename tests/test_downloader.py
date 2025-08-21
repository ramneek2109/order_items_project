from order_items.downloader import download_csv
from pathlib import Path

def test_download_csv(monkeypatch, tmp_path):
    # Mock requests.get to avoid real network call
    class MockResponse:
        def __enter__(self): return self
        def __exit__(self, *args): pass
        def raise_for_status(self): pass
        def iter_content(self, chunk_size=8192):
            yield b"col1,col2\n1,2\n"

    def mock_get(*args, **kwargs):
        return MockResponse()

    import requests
    monkeypatch.setattr(requests, "get", mock_get)

    file_path = download_csv("http://fake-url.com/file.csv", tmp_path)
    assert file_path.exists()
    assert "order_items_" in file_path.name

