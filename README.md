# python-drills

My Python practice playground: small, self-contained drill files, each covering a few "cards" of core concepts.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

The drills from `03` on call the OpenAI API. Put your key in a `.env` file at the repo root (it's gitignored):

```
OPENAI_API_KEY=sk-...
```

## Drills

| File | Topics |
| --- | --- |
| `01_basics.py` | Indentation, dicts (`[]` vs `.get()`), nested access, `for` loops and `enumerate`, f-strings and format specs, functions, default args, tuple returns |
| `02_files.py` | Loading datasets from JSON and CSV into a list of dicts, the "CSV values are always strings" gotcha |
| `03_openai_call.py` | First API call: `load_dotenv()`, the `messages` list, system vs user roles, reading `choices[0].message.content` |
| `04_openai_call_json.py` | Structured output: `response_format={"type": "json_object"}`, `temperature=0`, parsing the reply string with `json.loads` |
| `05_eval.py` | A small eval harness: fixed question/answer rows, keyword scoring, pass rate and a list of misses |

## Algorithms

Practice problems under `data-structure-algorithms/`, one folder per pattern.

| Pattern | File | Topics |
| --- | --- | --- |
| `two-pointers` | `triangle_numbers.py` | Counting valid triangle triplets: sort, then two pointers with a fixed largest side |

Run any drill directly:

```bash
python 01_basics.py
python data-structure-algorithms/two-pointers/triangle_numbers.py
```

`02_files.py` creates `data/sample.json` and `data/sample.csv` on first run. Delete `data/` to regenerate them (it's gitignored).

Each file ends with a **TRY IT** section: exercises to do from memory, then run.
