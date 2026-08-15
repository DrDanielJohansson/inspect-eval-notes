import re
pat = r"(?is).*(?<!\w)GRADE(?!\w)\s*:\s*(Correct|Partial|Incorrect|[CPI])(?!\w)"
for s in ["GRADE: C", "GRADE: CI", "GRADE: Correct", "GRADE: Correctness",
          "GRADE: Incorrect", "grade: c", "The GRADE: C.", "GRADE: CP"]:
    m = re.search(pat, s)
    print(f"{s!r:28} -> {m.group(1) if m else 'NO MATCH (-> unscored)'}")
