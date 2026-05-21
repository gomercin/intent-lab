# Agent Starter Prompts

Use these prompts with Codex or another coding agent.

## 1. Start Discovery

```text
Read AGENTS.md, PROJECT_STATUS.md, and docs/workflow-discovery.md.

Do not implement yet.

First help me clarify:
- the real business goal,
- the current manual workflow,
- the inputs and outputs,
- edge cases,
- failure handling,
- safer alternatives to UI automation.

Ask only a few focused questions at a time.
If the user has not filled out any templates, interview them and summarize the important parts yourself.
```

## 2. Convert Messy Request to Requirements

```text
I will describe a manual process informally.

Your job is to translate it into clear automation requirements.

Do not assume my proposed solution is the best solution.
Do not ask me to fill out a form unless I request one.

Identify:
- real goal,
- current workaround,
- missing information,
- assumptions,
- edge cases,
- recommended MVP,
- agent-ready implementation prompt.
```

## 3. Debug a Failed Run

```text
The automation failed.

Do not change code yet.

Inspect the latest run artifacts first:
- runs/latest/
- logs/
- screenshots/
- extracted data
- timings

Produce a bug analysis:
- expected behavior,
- actual behavior,
- last successful step,
- evidence found,
- likely failure point,
- smallest safe fix.

If the evidence is missing or unclear, ask only the next few questions needed to diagnose the issue.
```

## 4. Excel Automation

```text
We are working with Excel or Office files.

Before writing business logic, review docs/excel-and-office-file-strategy.md.

Create or improve a separate extractor step that produces normalized, inspectable data.

Preserve IDs as text where needed.
Preserve macros unless explicitly asked otherwise.
Do not mix Excel parsing, business logic, and UI automation in one large script.
```

## 5. UI Automation

```text
We may need UI automation.

Before implementing, review docs/ui-automation-protocol.md.

First check whether API/import/export alternatives exist.

If UI automation is necessary, include:
- login wait for SSO/2FA,
- page readiness checks,
- screenshots on failure,
- pause/resume or human takeover if needed,
- run artifacts for debugging.

Do not hardcode credentials.
```

## 6. Risky Change

```text
Before making this risky change:
1. create a timestamped backup using tools/create_backup.py,
2. update PROJECT_STATUS.md,
3. explain the planned change in plain language,
4. keep the change small and reversible.
```
