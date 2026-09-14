import csv
import json
import argparse
import time
from datetime import datetime, timezone
from pathlib import Path

import requests


ROOT = Path(__file__).resolve().parents[1]
QUESTIONS_FILE = ROOT / "questions" / "pilot_20_questions.csv"
OUTPUT_FILE = ROOT / "results" / "raw_results.jsonl"
OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3:8b"
SYSTEM_PROMPT = (
    "You are a medical question-answering assistant.\n"
    "Answer the following clinical question based only on your medical knowledge.\n"
    "Give a concise answer and briefly explain your reasoning.\n"
    "Do not assume information that is not provided."
)


def run_question(item: dict) -> dict:
    prompt = (
        f"{item['question']}\n\n"
        "Choose the single best answer and briefly explain your reasoning. "
        "Do not use tools or create tasks."
    )
    started = time.perf_counter()
    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL,
            "messages": [
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": prompt},
            ],
            "stream": False,
            "think": False,
            "options": {"temperature": 0},
        },
        timeout=600,
    )
    response.raise_for_status()
    payload = response.json()
    elapsed = time.perf_counter() - started
    message = payload.get("message", {})
    return {
        "id": item["id"],
        "specialty": item["specialty"],
        "model": MODEL,
        "temperature": 0,
        "question": item["question"],
        "correct_answer": item["correct_answer"],
        "raw_response": message.get("content", ""),
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "elapsed_seconds": round(elapsed, 3),
        "eval_count": payload.get("eval_count"),
        "eval_duration_ns": payload.get("eval_duration"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    with QUESTIONS_FILE.open("r", encoding="utf-8-sig", newline="") as handle:
        questions = list(csv.DictReader(handle))
    if args.limit is not None:
        questions = questions[: args.limit]

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    with OUTPUT_FILE.open("w", encoding="utf-8") as output:
        for index, item in enumerate(questions, start=1):
            print(f"[{index}/{len(questions)}] Running {item['id']}...", flush=True)
            result = run_question(item)
            output.write(json.dumps(result, ensure_ascii=False) + "\n")
            output.flush()
            print(f"    saved ({result['elapsed_seconds']} seconds)", flush=True)


if __name__ == "__main__":
    main()
