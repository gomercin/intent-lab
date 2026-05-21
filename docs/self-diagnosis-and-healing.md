# Self-Diagnosis and Healing

Automation should help diagnose itself.

The goal is that a user can say:

> Check the last run results.

and the agent can inspect enough evidence to understand what happened.

## Run Folder Structure

Each meaningful run should create a timestamped folder.

Example:

```text
runs/2026-05-21_1530/
  run-log.jsonl
  timings.json
  decisions.json
  errors.json
  screenshots/
  extracted-data/
  output/
```

Also update:

```text
runs/latest/
```

so the latest result is easy to find.

## What To Record

Record:

- input file used,
- start time,
- end time,
- key steps,
- decisions made,
- skipped records,
- validation errors,
- external system actions,
- screenshots on failure,
- timings for critical operations.

## Timing Measurements

Measure important actions:

- reading Excel,
- extracting data,
- validating rows,
- opening browser,
- waiting for login,
- page load,
- finding UI elements,
- processing items,
- waiting for confirmation.

This helps detect slow or outdated exploratory code.

## Stale Exploratory Code

Agents often leave old exploratory logic in production paths.

Look for:

- full DOM scans every run,
- repeated fallback selector searches,
- long fixed sleeps,
- repeated workbook loading,
- unnecessary screenshots,
- debug logging that slows normal use.

Once reliable selectors or extraction methods are known, production mode should use the direct path.

## Healing Strategies

Possible safe recovery strategies:

- retry transient page load failures,
- refresh stale pages,
- re-check target page state,
- pause for user takeover,
- skip failed item and continue when safe,
- stop and report when data integrity is at risk.

## Agent Prompt Template

```text
Inspect the latest run artifacts and timing files.

Identify:
- where the run spent most time,
- whether old exploratory code still runs in the production path,
- whether failures are deterministic or transient,
- whether screenshots/logs show a changed UI state,
- the smallest safe improvement.

Do not rewrite large parts of the automation unless evidence supports it.
```
