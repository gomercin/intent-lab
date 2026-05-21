# Workflow Discovery

Use this before implementation starts.

The purpose is to understand the real workflow and prevent the agent from automating the wrong thing.

The user does not need to fill out this document. Use it as an agent guide for a focused conversation.

## 1. Real Goal

What is the actual business outcome?

Do not only write the manual action.

Weak version:

> Fill the form and click submit.

Better version:

> Process validated items in the target system and produce a report of successful, skipped, and failed items.

## 2. Current Manual Process

Describe the process step by step.

For each step, capture:

- what the user does,
- what system/file they use,
- what they check,
- what decision they make,
- what can go wrong.

## 3. Inputs

List all inputs.

Examples:

- Excel files,
- CSV exports,
- emails,
- screenshots,
- downloaded reports,
- legacy system pages,
- manually entered values.

For each input, record:

- where it comes from,
- who prepares it,
- expected format,
- common format problems,
- example normal file,
- example problematic file.

## 4. Outputs

List what the process should produce.

Examples:

- processed items,
- updated Excel file,
- validation report,
- error list,
- confirmation screenshots,
- audit trail.

## 5. Decision Points

What decisions does the human make today?

Examples:

- skip row if field is empty,
- choose the right handling path based on category,
- mark item urgent if priority is high,
- stop if approval is missing.

## 6. Exceptions and Edge Cases

Ask for:

- one normal example,
- one problematic example,
- one case where automation should stop.

Potential edge cases:

- missing required field,
- duplicate ID,
- invalid date,
- unexpected status,
- changed Excel template,
- login expired,
- page loads slowly,
- item already exists,
- action appears to succeed but confirmation is missing.

## 7. Failure Handling

Define what should happen when something fails.

Should the automation:

- stop immediately,
- skip the item and continue,
- ask the user,
- retry,
- save a screenshot,
- write a report,
- rollback or undo something?

## 8. Automation Strategy

Before UI automation, check whether there is:

- API,
- batch import,
- database access,
- export/import file,
- template upload,
- existing report,
- Power Automate flow,
- macro or internal tool.

## Agent Prompt Template

```text
We are still in discovery mode. Do not write code yet.

Help me clarify the automation requirements.

First identify whether I am describing the real goal, the current manual workaround, or an imagined solution.

Ask me for:
1. one normal example,
2. one problematic example,
3. one case where the process should stop.

If my answer is incomplete, ask the next useful question instead of sending me to a template.

Then produce:
- workflow summary,
- assumptions,
- edge cases,
- missing information,
- recommended automation strategy.
```
