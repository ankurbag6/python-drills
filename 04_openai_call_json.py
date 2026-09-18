import json
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI()

def ask_model_json(question):
    """Ask a question, get a dict back (not prose)."""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": (
                    "You are a SaaS-metrics expert. "
                    "Respond with only a JSON object in this exact shape: "
                    '{"answer": "<one sentence>", "confidence": <0 to 1>}'
                ),
            },
            {"role": "user", "content": question},
        ],
        response_format={"type": "json_object"},   # API-level guarantee: valid JSON
        temperature=0
    )
    text = response.choices[0].message.content     # still a STRING at this point
    return json.loads(text)                        # string -> dict


if __name__ == "__main__":
    result = ask_model_json("What is MRR?")
    print(result)  
    print(result["answer"])                        # brackets — it's a dict now
    print(f"confidence: {result['confidence']:.0%}")