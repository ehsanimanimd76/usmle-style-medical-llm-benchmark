# Physician-Reviewed USMLE-Style Medical LLM Evaluation Benchmark

An exploratory physician-reviewed benchmark evaluating a locally deployed medical language model on 20 original USMLE-style clinical vignettes.

> These are original educational questions inspired by Step 2 CK-style clinical reasoning. They are not official USMLE questions.

## What this project evaluates

The benchmark assesses:

- Accuracy
- Completeness
- Safety
- Clinical reasoning

It also includes a controlled perturbation stress test examining whether answer choices remain stable when clinical information is changed or reordered.

## Physician-reviewed baseline pilot

- Model: `qwen3:8b`
- Runtime: Ollama + Open WebUI
- Temperature: `0`
- Web search, RAG, and tools: disabled
- Questions: 20
- Rubric: Accuracy, Completeness, Safety, and Clinical Reasoning
- Score per domain: 0–2
- Maximum score: 160
- Observed score: 152/160 (95%)
- Critical errors: 1
- Critical error: `MED-002`
- Reviewer: physician-led review by the project author

The baseline response archive is stored in `raw_responses/`, and the scoring table is stored in `results/pilot_results.csv`.

## Independent automated Ollama run

A separate automated run was performed through the local Ollama API using the same model and temperature setting.

- Questions completed: 20
- Empty responses: 0
- Explicit answer-choice accuracy: 18/20 (90%)
- Incorrect choices: 2
- Critical safety errors: 2
- Total runtime: 422.834 seconds
- Mean runtime: 21.14 seconds per question
- Total generated tokens: 3,928
- Mean generated tokens: 196.4 per question
- Approximate generation rate: 9.29 tokens per second

This automated result is separate from the physician-reviewed baseline. It uses answer-choice matching and does not replace the four-domain physician rubric.

See `results/raw_results.jsonl`, `results/automated_choice_summary.md`, and `analysis/resource_metrics.md`.

## Controlled perturbation stress test — v0.2.0

Five base questions were expanded into 15 controlled variants involving age changes, pregnancy, renal disease, added distractors, reordered information, and negative framing.

- Variants completed: 15
- Correct answer choices: 14/15
- Choice accuracy: 93.3%
- Unknown choices: 0
- Critical safety errors: 1

The error occurred in a reordered DKA vignette. The model selected immediate insulin instead of potassium replacement first when serum potassium was 3.0 mEq/L.

See `results/perturbation_results.jsonl` and `analysis/perturbation_summary_v0.2.md`.

## Limitations

- This is a small exploratory pilot.
- The questions are original educational items and are not official USMLE questions.
- The baseline and automated runs are separate experiments and must not be pooled.
- The perturbation set includes only five base questions and 15 variants.
- Results require larger samples, multiple models, physician review, and independent replication.
- This benchmark is not a measure of general clinical reliability.

## Repository structure
```text
questions/
  pilot_20_questions.csv
  pilot_20_questions_full.csv
  perturbation_set_v0.2.csv

results/
  pilot_results.csv
  raw_results.jsonl
  perturbation_results.jsonl
  automated_choice_summary.md
  README.md

raw_responses/
analysis/
rubric/
scripts/
README.md
LICENSE
