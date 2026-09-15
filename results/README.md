# Results

This directory contains outputs from two separate experiments. Their scores must not be pooled.

## Physician-reviewed baseline

`pilot_results.csv` contains the physician-led four-domain rubric scores for the 20-question baseline pilot.

- Maximum score: 160
- Observed score: 152/160 (95%)
- Critical safety errors: 1
- Critical error: MED-002

The baseline response archive is stored in `raw_responses/`.

## Automated Ollama run

`raw_results.jsonl` contains independent local Ollama API responses, including model output, timing, and token metadata.

Choice matching is summarized in `automated_choice_summary.md`. Runtime measurements are reported in `analysis/resource_metrics.md`.

## Perturbation stress test

`perturbation_results.jsonl` contains 15 controlled variants derived from five base questions.

- Correct choices: 14/15
- Choice accuracy: 93.3%
- Critical safety errors: 1
- Critical error: P002-C, a reordered DKA vignette

All results are exploratory and require further physician review, larger samples, multiple models, and independent replication.
