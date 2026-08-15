# inspect-eval-notes
Eval harness fieldnotes

Field notes from three weeks with Inspect (UK AISI's LLM evaluation framework): a grade-parsing integrity issue, a limit-sensitivity and variance study on an agentic CTF benchmark, and self-run human baselining.

This repo is a brief write-up on the experiences gained as a system engineer getting familiar with eval infrastructure. The motivation behind it is to get a better understanding of the limits of AI and how to test it for capability (before propensity) as the models get more and more complex.

Finding 1:
Evaluation of locally run qwen 2.5 1.5b, one question received a malformed judge output, GRADE: CI. This grade bypassed the parse-failure test and scored as correct. A strict pattern that prevents this instead breaks spelled out grades, requiring normalization in code to fully fix the bug.
