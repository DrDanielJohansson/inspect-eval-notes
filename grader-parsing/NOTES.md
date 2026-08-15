# Grader parsing — reproduction

Analysis and conclusions: see [README Finding 1](../README.md#finding-1---grader-integrity)
and upstream [inspect_ai #4872](https://github.com/UKGovernmentBEIS/inspect_ai/issues/4872).
This file is just the evidence and how to reproduce it.

## The pattern

From `inspect_ai/scorer/_model.py` (inspect-ai 0.3.258):  
DEFAULT_GRADE_PATTERN = r"(?is).(?<!\w)GRADE(?!\w)\s:\s*([CPI])"

The capture `([CPI])` matches exactly one character with no trailing boundary,
so any token beginning with C/P/I after `GRADE:` yields a "valid" grade and
never reaches the `Score.unscored` / `grade_parse_failure` path.

## truth_table.py — output

Run: `python truth_table.py`

GRADE: C -> C  
GRADE: CI -> NO MATCH (-> unscored)  
GRADE: Correct -> Correct  
GRADE: Correctness -> NO MATCH (-> unscored)  
GRADE: Incorrect -> Incorrect  
grade: c -> c  
The GRADE: C. -> C  
GRADE: CP -> NO MATCH (-> unscored)  

Left column is the proposed stricter/wider pattern
`(Correct|Partial|Incorrect|[CPI])(?!\w)`, showing it rejects the malformed
`CI`/`CP` mashups while still accepting spelled-out and lowercase grades.

## Why a pattern-only fix is not enough

`value_to_float()` (`_metric.py`) compares the grade to the letter constants
(`"C"`, `"I"`, ...) *before* it lowercases, and the lowercased branch only
knows booleans and numbers. So `"Correct"` and `"c"` both fall through to a
warning and score 0.0. A full fix needs word→letter normalization in code
after `match.group(1)`, not just a stricter regex.

## forced_grade_test.py — deterministic check

Run: `inspect eval forced_grade_test.py --model ollama/qwen2:1.5b`

Uses a `mockllm` grader with canned outputs so the grade path is exercised
without inference noise. Swap the canned string (`GRADE: Correct`, `GRADE: CI`,
`grade: c`, a grade-free ramble) to see each routing outcome end to end.

