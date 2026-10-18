# Repair Circle

Bring the object to the middle. Bring observations, not certainty.

A keeper names a shared item, proposes bounded remedies, and gathers observations from distinct places. A separate repair steward asks GenLayer validators for one attributed diagnosis and a safety status for every remedy. The contract then chooses the safe option with the lowest declared irreversibility. If none is safe, the circle records `NO_REPAIR` instead of improvising.

The chosen remedy is a coordination record, not professional safety certification. The keeper may adopt it or retire an unresolved circle.

## Workshop rhythm

```text
python -m pytest -q
genvm-lint lint contracts/contract.py
```

Look for the finalized deployment and gathering receipt in the two JSON records at the root.
