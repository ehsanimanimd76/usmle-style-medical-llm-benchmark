import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
questions_file = ROOT / "questions" / "perturbation_set_v0.2.csv"
results_file = ROOT / "results" / "perturbation_results.jsonl"


def extract_choice(response: str) -> str:
    patterns = [
        r"^\s*(?:\*{0,2})\s*(?:answer|final answer|choice)\s*[:\-]?\s*(?:\*{0,2})\s*([A-E])\b",
        r"^\s*(?:\*{0,2})\s*([A-E])\s*[\.:\-]",
        r"^.{0,180}?\b(?:answer|diagnosis|next step|treatment|choice)\b.{0,40}?(?:\*{0,2})\s*([A-E])\s*[\.:\-]?\b",
    ]
    for pattern in patterns:
        match = re.search(pattern, response, re.I | re.S)
        if match:
            return match.group(1).upper()
    return "UNKNOWN"


with questions_file.open(encoding="utf-8-sig", newline="") as handle:
    expected = {
        row["variant_id"]: row["correct_answer"].upper()
        for row in csv.DictReader(handle)
    }

items = [
    json.loads(line)
    for line in results_file.read_text(encoding="utf-8").splitlines()
    if line.strip()
]

correct = incorrect = unknown = 0
for item in items:
    observed = extract_choice(item.get("raw_response", ""))
    answer = expected[item["id"]]
    status = "CORRECT" if observed == answer else "INCORRECT" if observed != "UNKNOWN" else "UNKNOWN"
    if status == "CORRECT":
        correct += 1
    elif status == "INCORRECT":
        incorrect += 1
    else:
        unknown += 1
    print(f"{item['id']}: expected={answer} observed={observed} {status}")

print("\nSummary")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Unknown: {unknown}")
if items:
    print(f"Choice accuracy: {correct / len(items) * 100:.1f}%")
