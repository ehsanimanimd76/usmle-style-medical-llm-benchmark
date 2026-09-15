# Physician-Reviewed USMLE-Style Medical LLM Evaluation Benchmark

Pilot benchmark for evaluating a local medical language model on 20 original, USMLE-style clinical vignettes.

> These are original educational questions inspired by Step 2 CK-style clinical reasoning. They are not official USMLE questions.

## Current pilot

- Model: `qwen3:8b`
- Runtime: Ollama + Open WebUI
- Temperature: `0`
- Web search/RAG/tools: disabled for evaluation
- Questions: 20
- Scoring: Accuracy, Completeness, Safety, Clinical Reasoning; each 0–2
- Maximum score: 160
- Current score: 152/160 (95%)
- Critical errors: 1
- Human reviewer: physician-led review

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

The automated choice result is separate from the earlier physician-rubric score because the automated run used the complete multiple-choice question file and was executed as an independent run.

See `results/raw_results.jsonl`, `results/automated_choice_summary.md`, and `analysis/resource_metrics.md`.

## Important limitation

The scoring table was reconstructed from the evaluation conversation. Before publication, each model response must be copied verbatim into `results/pilot_results.csv` or a linked raw-response archive. Do not publish paraphrased text as a raw response.

## Repository structure

```text
questions/pilot_20_questions.csv
results/pilot_results.csv
rubric/scoring_rubric.md
analysis/summary.md
```

## Safety notice

This benchmark evaluates model behavior and is not a diagnostic or treatment tool. It must not be used for clinical decision-making.
