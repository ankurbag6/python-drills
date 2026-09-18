"""05_eval.py — the harness. Everything from cards 3-9 assembled."""

import json

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

SYSTEM_PROMPT = (
    "You are a SaaS-metrics expert answering a quiz with canonical definitions "
    "Respond with only a JSON object: "
    '{"answer": "<one sentence, no preamble, no hedging>"}'
)


def ask_model(question):
    """One API call, returns the answer string."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": question},
        ],
        response_format={"type": "json_object"},
        temperature=0,
    )
    return json.loads(response.choices[0].message.content)["answer"]


# def score(answer, expected):
#     """Substring match, case-insensitive. Upgrade point: LLM-as-judge."""
#     return expected.lower() in answer.lower()

def score(answer, expected):
    keywords = [k.strip() for k in expected.split("|")]
    return any(k.lower() in answer.lower() for k in keywords)


def run_eval(rows):
    """Returns (correct_count, list_of_miss_dicts)."""
    correct = 0
    misses = []
    for row in rows:
        answer = ask_model(row["question"])
        if score(answer, row["expected"]):
            correct += 1
        else:
            misses.append({"question": row["question"],
                           "expected": row["expected"],
                           "got": answer})
    return correct, misses


if __name__ == "__main__":
    with open("data/sample.json") as f:
        rows = json.load(f)

    correct, misses = run_eval(rows)

    print(f"Score: {correct}/{len(rows)} ({correct/len(rows):.1%})")
    for i, m in enumerate(misses, start=1):
        print(f"\nMISS {i}: {m['question']}")
        print(f"  expected: {m['expected']}")
        print(f"  got:      {m['got'][:80]}")