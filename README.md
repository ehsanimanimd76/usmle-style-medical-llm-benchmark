# Physician-Reviewed USMLE-Style Medical LLM Evaluation Benchmark

An exploratory physician-reviewed benchmark for evaluating a locally deployed medical language model on 20 original, USMLE-style clinical vignettes.

> These are original educational questions inspired by Step 2 CK-style clinical reasoning. They are not official USMLE questions.

## What this project evaluates

The benchmark assesses four dimensions of model behavior:

- Accuracy
- Completeness
- Safety
- Clinical reasoning

It also includes a small controlled perturbation stress test to examine whether answer choices remain stable when selected clinical information is changed or reordered.

## Baseline pilot

- Model: `qwen3:8b`
- Runtime: Ollama + Open WebUI
- Temperature: `0`
- Web search/RAG/tools: disabled for evaluation
- Questions: 20
- Scoring: Accuracy, Completeness, Safety, Clinical Reasoning; each 0–2
- Maximum score: 160
- Current score: 152/160 (95%)
- Critical errors: 1
- Human reviewer: physician-led review by the project author, a physician

## Automated Ollama run

An independent automated run was performed through the local Ollama API using the same model and temperature setting.

- Questions completed: 20
- Empty responses: 0
- Explicit answer-choice accuracy: 18/20 (90%)
- Incorrect choices: 2
- Critical safety errors: 2
- Total runtime: 269.65 seconds
- Mean runtime per question: 13.48 seconds
- Mean generated tokens per question: 122.65
- Approximate aggregate generation rate: 9.10 tokens/second

The automated choice result is separate from the physician-rubric score because it is an independent API run and uses answer-choice matching rather than the full four-domain rubric.

See `results/raw_results.jsonl`, `results/automated_choice_summary.md`, and `analysis/resource_metrics.md`.

## Controlled perturbation stress test — v0.2.0

Five base questions were expanded into 15 controlled variants involving age changes, pregnancy, renal disease, distractors, reordered information, and negative framing.

- Variants completed: 15
- Correct answer choices: 14/15 (93.3%)
- Unknown choices: 0
- Critical safety errors: 1

The only error occurred in a reordered DKA vignette: the model selected immediate insulin instead of potassium replacement first when serum potassium was 3.0 mEq/L. This pilot finding suggests that answer stability may be sensitive to information presentation and should be investigated with a larger perturbation set.

See `results/perturbation_results.jsonl` and `analysis/perturbation_summary_v0.2.md`.

## Limitations

- This is a small pilot and is not a measure of general clinical reliability.
- The questions are original educational items inspired by Step 2 CK-style reasoning, not official USMLE questions.
- The baseline and automated runs are separate experiments and should not be pooled.
- The perturbation set covers only five base questions and 15 variants.
- Results require further physician review, larger samples, multiple models, and independent replication before strong conclusions can be drawn.

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
raw_responses/
analysis/
rubric/
scripts/
README.md
LICENSE
```

## Safety notice

This benchmark evaluates model behavior and is not a diagnostic or treatment tool. It must not be used for clinical decision-making.
