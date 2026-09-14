# Automated Runtime Metrics

This run used the local Ollama API with `qwen3:8b`, temperature `0`, and `think: false`.

| Metric | Value |
|---|---:|
| Questions completed | 20 |
| Empty responses | 0 |
| Total runtime | 269.65 seconds |
| Mean runtime per question | 13.48 seconds |
| Total generated tokens | 2,453 |
| Mean generated tokens per question | 122.65 |
| Approximate aggregate generation rate | 9.10 tokens/second |

## Interpretation

All 20 requests completed successfully and produced non-empty responses. These are runtime/resource measurements only; they are not medical accuracy or safety scores.

## Reproducibility

The automated output is stored in `results/raw_results.jsonl` and the runner is stored in `scripts/run_benchmark.py`.
