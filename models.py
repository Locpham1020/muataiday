import os
import json
from datetime import datetime

def _get_path(base, table):
    return os.path.join("airtable_data", f"{base}_{table}.json")

def read_data(base, table):
    path = _get_path(base, table)
    if not os.path.exists(path):
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_data(base, table, data):
    path = _get_path(base, table)
    all_data = read_data(base, table)
    all_data.append(data)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(all_data, f, indent=2, ensure_ascii=False)

def export_data(base, table):
    return read_data(base, table)

def clear_data(base, table):
    with open(_get_path(base, table), "w", encoding="utf-8") as f:
        json.dump([], f)
