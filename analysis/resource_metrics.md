# Automated Runtime Metrics

This run used the local Ollama API with `qwen3:8b`, temperature `0`, and `think: false`.

| Metric | Value |
|---|---:|
| Questions completed | 20 |
| Empty responses | 0 |
| Total runtime | 422.834 seconds |
| Mean runtime per question | 21.14 seconds |
| Total generated tokens | 3,928 |
| Mean generated tokens per question | 196.4 |
| Approximate generation rate | 9.29 tokens/second |

## Interpretation

All 20 requests completed successfully and produced non-empty responses. These are runtime and resource measurements only; they are not medical accuracy or safety scores.

## Reproducibility

The automated outputs are stored in `results/raw_results.jsonl`. The runner is stored in `scripts/run_benchmark.py`.

The automated run is separate from the physician-reviewed Open WebUI baseline and should not be pooled with its rubric score.
