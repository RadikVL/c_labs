import json
import pytest
from pathlib import Path


@pytest.fixture
def write_json(tmp_path: Path):
    """Write dict/list → JSON file. Returns path."""
    def _writer(name: str, data):
        p = tmp_path / name
        p.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
        return p
    return _writer


@pytest.fixture
def write_csv(tmp_path: Path):
    """Write CSV by headers + rows. Returns path."""
    import csv

    def _writer(name: str, headers, rows):
        p = tmp_path / name
        with p.open("w", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for r in rows:
                writer.writerow(r)
        return p
    return _writer
