import csv
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
questions_file = ROOT / "questions" / "pilot_20_questions.csv"
results_file = ROOT / "results" / "raw_results.jsonl"

with questions_file.open(encoding="utf-8-sig", newline="") as f:
    expected = {row["id"]: row["correct_answer"].upper() for row in csv.DictReader(f)}

results = []
for line in results_file.read_text(encoding="utf-8").splitlines():
    if line.strip():
        results.append(json.loads(line))

correct = incorrect = unknown = 0
for item in results:
    response = item.get("raw_response", "")
    # Only accept an explicit answer label near the beginning of the response.
    # Do not scan the reasoning broadly, because it may mention distractor letters.
    match = re.search(
        r"^\s*(?:\*{0,2})\s*(?:answer|final answer|choice)\s*[:\-]?\s*"
        r"(?:\*{0,2})\s*([A-E])\b",
        response,
        re.I,
    )
    if not match:
        match = re.search(
            r"^\s*(?:\*{0,2})\s*([A-E])\s*[\.:\-]",
            response,
            re.I,
        )
    if not match:
        match = re.search(
            r"^.{0,180}?\b(?:answer|diagnosis|next step|treatment|choice)\b"
            r".{0,40}?(?:\*{0,2})\s*([A-E])\s*[\.:\-]?\b",
            response,
            re.I,
        )
    observed = match.group(1).upper() if match else "UNKNOWN"
    expected_answer = expected[item["id"]]
    status = "CORRECT" if observed == expected_answer else "INCORRECT" if observed != "UNKNOWN" else "UNKNOWN"
    if status == "CORRECT":
        correct += 1
    elif status == "INCORRECT":
        incorrect += 1
    else:
        unknown += 1
    print(f"{item['id']}: expected={expected_answer} observed={observed} {status}")

print("\nSummary")
print(f"Correct: {correct}")
print(f"Incorrect: {incorrect}")
print(f"Unknown: {unknown}")
print("Note: This is preliminary choice matching, not physician rubric scoring.")
