# Human baselining — notes

Analysis and conclusions: see [README Finding 3](../README.md#finding-3---human-baselining).

Agent: `human_cli()` on `inspect_evals/gdm_intercode_ctf`, same sandbox and
scoring as the model runs.

Attempted: 5 samples (17, 18, 19, 22, 26), stopped voluntarily —
no need to baseline all 78, and partial baselining is normal practice.

## Observations

- Considerable warm-up cost. Skills not currently in use needed refreshing:
  tools, tool flags, encoding/decoding utilities, which command does what.
  The model pays none of this cost per task.
- Rough time: ~15min per challenge for me vs Haiku's ~19s wall-clock average.
- Where my approach differed from the model's on the same challenge:
  The model consistently uses python whereas I first tried different tools from the terminal.

## Takeaway

The human is a noisy instrument, and the noise is dominated by skill currency
rather than raw ability — which is exactly why human-baseline data is expensive
and heavily caveated. Baselining measures "this person, today, with these skills
paged in," not abstract human capability.
