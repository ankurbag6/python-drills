"""
    This is my basic practise file.
    Steps to run: python 01_basics.py
"""
print("Hello world");

# ---------------------------------------------------------------
# CARD 1 — Indentation IS the syntax
# Colon opens a block, indentation defines it. No braces.
# ---------------------------------------------------------------

def grade(score):
    if score >=80:
        return "Pass"
    else:
        return "Fail"

print(grade(99))

def check(temp):
    if temp>97:
        return "Fever"
    return "Ok"

print(check(102))

# ---------------------------------------------------------------
# CARD 2 — Dicts: brackets = required (fail loud),
#          .get() = optional (fail quiet, with default)
# ---------------------------------------------------------------
row = {"question": "What is MRR?", "expected_answer": "Monthly recurring revenue"}

required = row["expected_answer"]
optional = row.get("difficulty","medium")

print(required+" | "+optional)


# Nested access — OpenAI-response shape:
response = {
    "choices": [
        {"message": {"role": "assistant", "content": "The answer is 42."}}
    ]
}
text = response['choices'][0]['message']['content']

print(text)

# ---------------------------------------------------------------
# CARD 3 — Lists and the for loop: three shapes, ranked
# ---------------------------------------------------------------
misses = ["What is MRR?", "What is ARR?", "What is churn?"]

# Shape 1 — want items (default, 90% of the time). Your quiz answer:
for miss in misses:
    print(miss)

# Shape 2 — want items + index. enumerate can start at 1 (your quiz trap):
for i,miss in enumerate(misses):
    print(f"{i}:{miss}")

# Shape 3 — want only the index (rare; reads as JS-translated):
for i in range(len(misses)):
    print(misses[i])

# len() is a standalone function, not a property:
print(len(misses))

# ---------------------------------------------------------------
# CARD 4 — f-strings: prefix f, {} like JS ${}
# Forget the f -> braces print literally. Silent bug.
# ---------------------------------------------------------------
 
correct = 23
total = 40
 
# Your quiz answer (with the parens fix):
print(f"{correct/total:.2%}")

# Format spec variations you asked about:
print(f"{correct/total:%}")     # 57.500000%  (default: 6 decimals)
print(f"{correct/total:.0%}")   # 58%         (rounds)
print(f"{correct/total}")       # 0.575       (raw float, no spec)

# Truncating long output — slicing, JS slice():
answer = "MRR stands for monthly recurring revenue, which measures..."
print(f"MISS: {answer[:40]}")

# ---------------------------------------------------------------
# CARD 5 — Functions: def, default args, tuple multi-return
# ---------------------------------------------------------------
 
def summarize(scores, label="run"):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg            # secretly a tuple: (total, avg)

t,a = summarize([9,19,20],label="final")
print(t,a)

 
# Tuples: immutable, any length, unpacking must match count:
point = (3, 5)
x, y = point
single = (89,)
print(x,y, single)



# TRY IT (from memory, then run):
# 1. Write is_long(text, limit=50) -> returns True if len(text) > limit

def is_long(text, limit=50):
    return len(text) > limit
text = "I m Ankur"
print(f"{text} is long : {is_long(text)}")

# 2. Write minmax(nums) -> returns (smallest, largest) as a tuple, unpack it
def minmax(nums):
    smallest = float("inf")
    largest = float("-inf")
    for n in nums:
        if n < smallest:
            smallest = n
        if n > largest:
            largest = n
    return smallest, largest
# min, max = minmax([1,4,-1,0,10,25])
# print(f"MIN: {min} | MAX: {max}")

print(f"MIN: {min([1,4,-1,0,10,25])} | MAX: {max([1,4,-1,0,10,25])}")
 
