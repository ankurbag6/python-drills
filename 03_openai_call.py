"""03_openai_call.py — card 8: first API call."""

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()                # reads .env -> OPENAI_API_KEY
client = OpenAI()            # picks the key up automatically
SYSTEM_PROMPT = """
    You are a consise assistant.
    Answer in 1 sentence 
    Send 1 question, return the reply text
"""

def ask_model(question, system_prompt=SYSTEM_PROMPT):
    messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": question}
        ]
    response = client.chat.completions.create(model="gpt-4.1-nano",
                                   messages=messages)
    return response.choices[0].message.content


if __name__ == "__main__":
    print(f"Assistant: {ask_model(question='Whats is MRR?')}")
    # Prompt engineering IS this argument:
    print(f"Assistant: {ask_model('What is MRR?', system_prompt='You are a Snarky assistant.')}")


# Format: there's no required format. A system prompt is just a string sent as the first message. Most good ones are written in this order:

# Role: who the model is.
# Task: what it's helping with.
# Rules: length, tone, what to avoid.
# Output format: exactly what the reply should look like.
# Examples (optional): one sample input and output. This works better than describing the format.
# A better version of yours:


# SYSTEM_PROMPT = """You are a concise assistant for SaaS and business terms.

# Rules:
# - Answer in exactly one sentence.
# - Use plain English; define any acronym you use.
# - If the question is unclear, give the most common meaning.
# - No greetings, no follow-up questions, no markdown.

# Example:
# Q: What is ARR?
# A: ARR (Annual Recurring Revenue) is the yearly value of all active subscription contracts."""