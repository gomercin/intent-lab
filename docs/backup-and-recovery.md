# Backup and Recovery

Many users of this project may not know Git.

This project therefore includes a simple timestamped zip backup approach.

## When To Create a Backup

Create a backup before:

- large refactors,
- changing working UI automation,
- modifying extraction logic,
- upgrading dependencies,
- deleting files,
- changing folder structure,
- letting an AI agent make broad changes.

## Backup Location

Backups are stored in:

```text
backups/
```

Example:

```text
backups/project_backup_2026-05-21_1530.zip
```

## Excluded Files

Backups should exclude noisy or large artifacts:

- logs/
- screenshots/
- runs/
- extracted/
- .venv/
- node_modules/
- __pycache__/
- *.log
- *.tmp
- .env

## Recovery Instructions

To recover:

1. unzip the backup,
2. open the restored folder,
3. review `PROJECT_STATUS.md`,
4. run the last known working command.

## Agent Prompt Template

```text
Before making this risky change, create a timestamped backup using tools/create_backup.py.

Then update PROJECT_STATUS.md with:
- current working state,
- planned change,
- risk,
- recovery note.

Keep the change small and reversible.
```
