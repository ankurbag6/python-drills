# python-drills

My Python practice playground: small, self-contained drill files, each covering a few "cards" of core concepts.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Drills

| File | Topics |
| --- | --- |
| `01_basics.py` | Indentation, dicts (`[]` vs `.get()`), nested access, `for` loops and `enumerate`, f-strings and format specs, functions, default args, tuple returns |
| `02_files.py` | Loading datasets from JSON and CSV into a list of dicts, the "CSV values are always strings" gotcha |

Run any drill directly:

```bash
python 01_basics.py
python 02_files.py
```

`02_files.py` creates `data/sample.json` and `data/sample.csv` on first run. Delete `data/` to regenerate them (it's gitignored).

Each file ends with a **TRY IT** section: exercises to do from memory, then run.
