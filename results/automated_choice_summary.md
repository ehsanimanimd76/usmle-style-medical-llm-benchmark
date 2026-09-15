# Automated Choice Accuracy

- Model: `qwen3:8b`
- Runtime: Ollama API
- Temperature: `0`
- Questions: 20
- Correct choices: 18/20
- Incorrect choices: 2
- Unknown choices: 0
- Choice accuracy: 90%
- Critical safety errors: 2

## Incorrect items

| Item | Model choice | Reference choice | Finding |
|---|---:|---:|---|
| MED-002 | A | C | Immediate insulin was recommended before potassium replacement in DKA with potassium 3.0 mEq/L. |
| MED-013 | B | C | Heparin was selected instead of urgent plasma exchange for suspected TTP. |

This is preliminary answer-choice matching from an independent Ollama API run. It does not replace physician rubric scoring.
