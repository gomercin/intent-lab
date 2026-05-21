# Bug Report Template

Optional structure for diagnosing a failed run.

The user should not have to fill this out before getting help. If the failure is unclear, the agent should inspect the latest run artifacts first, then ask a few focused questions and fill in the missing details itself.

## Expected Behavior

What should have happened?

Example:

> The script should read the Excel file, validate all rows, skip incomplete rows, and create a validation report.

## Actual Behavior

What happened instead?

Example:

> The script stopped after row 18 without creating a report.

## Reproduction Steps

Step-by-step:

1. I used input file: ...
2. I ran command: ...
3. I clicked: ...
4. The error happened when: ...

## Last Successful Step

What was the last thing that worked?

Example:

> The script opened the browser and loaded the target page, but failed when selecting the expected item.

## Evidence

Attach or point to:

- latest run folder,
- logs,
- screenshots,
- input file,
- output file,
- error message,
- timing file.

## Recent Changes

What changed recently?

Examples:

- Excel template changed,
- system UI changed,
- login flow changed,
- new input file received,
- agent changed selector logic,
- dependency updated.

## Suggested Agent Prompt

```text
The automation failed. Do not change code yet.

Inspect the latest run artifacts first:
- runs/latest/
- logs/
- screenshots/
- extracted data
- timing files

Create a short bug analysis with:
- expected behavior,
- actual behavior,
- last successful step,
- likely failure point,
- evidence found,
- minimal proposed fix.

If the evidence is incomplete, ask me only the next few questions needed to understand the failure.

Only after that, suggest or make the smallest safe code change.
```
