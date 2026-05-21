# Template Design Notes

This project should feel like a helpful automation coach, not a compliance system.

## Design Principle

The agent should carry the structure. The user should be able to describe work in normal language.

Documents and templates are here to help the agent ask better questions, preserve decisions, and avoid unsafe automation. They are not required homework for the user.

## User-Facing Layer

- `README.md` gives the simplest starting path.
- `PROJECT_STATUS.md` explains what works, what is missing, and how to run the project.
- `inputs/templates/` contains optional worksheets for people who like writing things down.

## Agent-Facing Layer

- `AGENTS.md` tells the agent how to clarify, challenge assumptions, and keep work observable.
- `docs/` contains deeper playbooks for discovery, bug diagnosis, Office files, UI automation, backups, and run evidence.

## Expected Behavior

When requirements are unclear, the agent asks focused questions.

When a bug report is unclear, the agent inspects the latest run artifacts and then asks for only the missing facts.

When the user proposes UI automation, the agent checks safer alternatives first.

When work changes meaningfully, the agent updates `PROJECT_STATUS.md`.
