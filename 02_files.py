"""
02_files.py — card 6: loading a dataset (JSON + CSV)
Run: python 02_files.py
Creates data/sample.json and data/sample.csv on first run,
then reads both back — so it's self-contained.
Both paths land on the same shape: a list of dicts.
"""

import csv
import json
import os

# ---------------------------------------------------------------
# Setup: write sample data files once (delete data/ to regenerate).
# Hand-editing data/sample.json afterwards is a great JSON drill.
# ---------------------------------------------------------------

os.makedirs("data", exist_ok=True)

sample_rows = [
    {"id": 1, "question": "What is MRR?", "expected": "monthly recurring revenue"},
    {"id": 2, "question": "What is churn?", "expected": "customers leaving"},
    {"id": 3, "question": "What is ARR?", "expected": "annual recurring revenue"},
    {"id": 4, "question": "What is CAC?", "expected": "customer acquisition cost"},
    {"id": 5, "question": "What is LTV?", "expected": "lifetime value"},
]

if not os.path.exists("data/sample.json"):
    with open("data/sample.json", "w") as f:
        json.dump(sample_rows, f, indent=2)     # write-side twin of json.load

if not os.path.exists("data/sample.csv"):
    with open("data/sample.csv", "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "question", "expected"])
        writer.writeheader()
        writer.writerows(sample_rows)


# ---------------------------------------------------------------
# CARD 6a — JSON: two lines. Your quiz answer (with the fix).
# ---------------------------------------------------------------

with open("data/sample.json") as f:
    rows = json.load(f)

print(len(rows))                    # how many rows
print(rows[0]["question"])          # first row's question — list index THEN dict key
                                    # (the hop you missed in the quiz: rows[0] alone
                                    #  prints the whole dict)


# ---------------------------------------------------------------
# CARD 6b — CSV: one extra line, identical result shape
# ---------------------------------------------------------------

with open("data/sample.csv") as f:
    csv_rows = list(csv.DictReader(f))   # header row becomes the dict keys

print(len(csv_rows))
print(csv_rows[0]["question"])

# GOTCHA — CSV values are ALWAYS strings:
first = csv_rows[0]
print(type(first["id"]))            # <class 'str'>, not int
print(int(first["id"]) + 1)         # convert explicitly before math
# String comparison trap (same as JS): "9" > "10" is True in string-land.


# ---------------------------------------------------------------
# Proof both formats feed the same downstream code:
# ---------------------------------------------------------------

def preview(rows, label):
    for i, row in enumerate(rows, start=1):
        print(f"{i}. {row['question']} -> {row['expected']}")
    print(f"{label}: {len(rows)} rows\n")


preview(rows, "json")
preview(csv_rows, "csv")

# TRY IT (from memory):
# 1. Add a 6th row by hand-editing data/sample.json, rerun, confirm len is 6.
# 2. Write count_long(rows) -> how many questions are longer than 12 chars.
#    Print it as a percentage with :.1% formatting.