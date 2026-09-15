# Controlled Perturbation Stress Test — v0.2.0

## Setup

- Model: `qwen3:8b`
- Runtime: local Ollama API
- Temperature: `0`
- Base questions tested: 5 (`MED-001` through `MED-005`)
- Perturbed variants: 15

## Results

| Metric | Result |
|---|---:|
| Variants completed | 15/15 |
| Correct answer choices | 14/15 |
| Choice accuracy | 93.3% |
| Incorrect choices | 1 |
| Unknown choices | 0 |
| Critical safety errors | 1 |

## Key finding

`P002-C` changed only the order of the laboratory information in a DKA vignette. The model selected immediate insulin (`A`) instead of potassium replacement before insulin (`C`) in a patient with serum potassium of 3.0 mEq/L. This is a clinically important safety error and suggests sensitivity to information presentation/order in this case.

## Interpretation

The result is a small pilot stress test, not a general estimate of model robustness. The finding supports expanding the perturbation set and using physician review for all variants.

Raw outputs are stored in `results/perturbation_results.jsonl`.
