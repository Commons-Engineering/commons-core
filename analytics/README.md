# Traffic Analytics

Daily-captured traffic stats for this repository. GitHub's Traffic API only retains the last 14 days; this directory accumulates the daily snapshots for long-term tracking.

## Files

- `clones.jsonl` — one JSON line per (date, capture-day) clone-count tuple
- `views.jsonl` — one JSON line per (date, capture-day) view-count tuple

## Field schema

```json
{"date": "2026-05-12", "count": 3, "uniques": 2, "captured": "2026-05-15"}
```

- `date` — the day the clone/view happened
- `count` — total clones/views that day
- `uniques` — unique cloners/visitors that day
- `captured` — the day this row was captured by the workflow (may be 1–14 days after `date`)

## Capture cadence

Workflow `.github/workflows/traffic-stats.yml` runs daily at 04:07 UTC. Trigger manually via the Actions tab if needed.

## Note on private clones

GitHub counts private `git clone` operations as well as public ones, but does not reveal cloner identity. The clone count is therefore a usage signal, not a directory of users.
