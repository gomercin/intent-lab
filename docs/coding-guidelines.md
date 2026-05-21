# Coding Guidelines

## Philosophy

Prefer simple, observable, maintainable automation.

Avoid giant scripts that combine everything.

## Recommended Architecture

Separate:

1. extraction,
2. normalization,
3. validation,
4. decision-making,
5. execution,
6. reporting,
7. diagnostics.

## User-Friendly Behavior

Assume users may not know:

- Git,
- terminals,
- Python environments,
- logs,
- stack traces,
- selectors,
- APIs.

Messages should explain:

- what happened,
- what succeeded,
- what failed,
- what the user should do next.

## Logging

Log important events, not noise.

Good logs:

- input file loaded,
- number of rows extracted,
- number of rows skipped,
- validation failures,
- page loaded,
- login waiting started/ended,
- item processed,
- confirmation received.

## Error Messages

Errors should be actionable.

Weak:

> Failed.

Better:

> Could not find the Submit button after login. A screenshot was saved at runs/latest/screenshots/submit_button_missing.png. Please check whether the page layout changed or whether login completed successfully.

## Agent Prompt Template

```text
Implement this change using the existing pipeline structure.

Keep extraction, validation, execution, reporting, and diagnostics separate.

Update PROJECT_STATUS.md after the change.

Add or update user-friendly error messages.

Avoid broad rewrites unless clearly necessary.
```
