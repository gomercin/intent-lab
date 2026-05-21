# AI Automation Starter Project

This repository is a starter template for AI-assisted automation projects, especially where non-technical users work with Excel files, legacy systems, browser UIs, and manual operational processes.

The goal is to help Codex or another coding agent guide the work safely. The user should not have to understand the whole folder structure before getting help.

## What This Template Helps With

- Refining incomplete requirements.
- Challenging false assumptions.
- Avoiding premature UI automation.
- Handling Excel and Office files more safely.
- Creating observable runs with logs, screenshots, extracted data, and timings.
- Maintaining user-friendly project documentation.
- Creating timestamped backups for users who do not use Git.

## Recommended Workflow

Start with a conversation, not a form.

1. Tell the agent what you do manually today, in ordinary language.
2. The agent should ask a few focused questions to clarify the real goal, examples, risks, and stop conditions.
3. The agent should summarize the agreed plan in `PROJECT_STATUS.md`.
4. The agent should build the smallest safe version first.
5. After each meaningful run, the agent should save evidence under `runs/` and update the status.

The templates in `inputs/templates/` are optional worksheets. Use them when they help. If they feel like homework, ask the agent to interview you and fill in the important parts itself.

## First Prompt To Codex

```text
Read AGENTS.md, PROJECT_STATUS.md, and docs/workflow-discovery.md.

I want to automate a manual business process. Do not implement yet.

First help me clarify the real business goal, the current manual steps, normal and problematic examples, stop conditions, and the safest automation strategy.

Ask only a few focused questions at a time. If my request is unclear, interview me instead of asking me to fill out a template.
```

## Important Files

- `AGENTS.md` - rules for Codex or another AI coding agent.
- `PROJECT_STATUS.md` - short, user-friendly project state.
- `docs/workflow-discovery.md` - how the agent should clarify a workflow.
- `docs/agent-starter-prompts.md` - reusable prompts for common situations.
- `docs/template-design-notes.md` - design intent for keeping the template approachable.
- `docs/bug-report-template.md` - optional structure for diagnosing failures.
- `docs/excel-and-office-file-strategy.md` - Excel and Office handling rules.
- `docs/ui-automation-protocol.md` - safe UI automation guidance.
- `docs/self-diagnosis-and-healing.md` - diagnostics and run evidence guidance.
- `tools/create_backup.py` - creates a timestamped backup zip.

## License

MIT License. See `LICENSE`.