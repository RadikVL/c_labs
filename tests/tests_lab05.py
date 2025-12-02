import os
import sys
import json
import csv
import pytest
from pathlib import Path

# Ensure the src directory is in the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from lab05.json_csv import json_to_csv, csv_to_json

def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"
    dst = tmp_path / "people.csv"

    data = [
        {"name": "Алиса", "age": 22},
        {"name": "Боб", "age": 25},
    ]

    src.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    json_to_csv(str(src), str(dst))

    rows = list(csv.DictReader(dst.open(encoding="utf-8")))
    assert len(rows) == 2
    assert set(rows[0].keys()) == {"name", "age"}
    assert rows[0]["name"] == "Алиса"


def test_json_to_csv_empty_list(tmp_path: Path):
    src = tmp_path / "empty.json"
    dst = tmp_path / "empty.csv"

    src.write_text("[]", encoding="utf-8")

    json_to_csv(str(src), str(dst))
    # CSV must contain only header or be empty depending on implementation
    content = dst.read_text(encoding="utf-8").strip()
    assert content == "" or "name" in content


def test_json_to_csv_invalid_json(tmp_path: Path):
    src = tmp_path / "bad.json"
    dst = tmp_path / "out.csv"
    src.write_text("{not-json}", encoding="utf-8")

    with pytest.raises(ValueError):
        json_to_csv(str(src), str(dst))


def test_json_to_csv_missing_file():
    with pytest.raises(FileNotFoundError):
        json_to_csv("no_such_file.json", "out.csv")

def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"

    with src.open("w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["name", "age"])
        writer.writeheader()
        writer.writerow({"name": "Alice", "age": "22"})
        writer.writerow({"name": "Bob", "age": "25"})

    csv_to_json(str(src), str(dst))

    data = json.loads(dst.read_text(encoding="utf-8"))
    assert len(data) == 2
    assert set(data[0].keys()) == {"name", "age"}


def test_csv_to_json_unicode(tmp_path: Path):
    src = tmp_path / "rus.csv"
    dst = tmp_path / "rus.json"

    with src.open("w", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["имя", "возраст"])
        writer.writeheader()
        writer.writerow({"имя": "Егор", "возраст": "30"})

    csv_to_json(str(src), str(dst))

    data = json.loads(dst.read_text(encoding="utf-8"))
    assert data[0]["имя"] == "Егор"


def test_csv_to_json_missing_file():
    with pytest.raises(FileNotFoundError):
        csv_to_json("missing.csv", "out.json")
