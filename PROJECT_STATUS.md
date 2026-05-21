# Project Status

This file is the living status page for the automation project.

It should be updated after meaningful changes so a non-technical user can understand where the project stands.

## Goal

Describe the real business goal here.

Do not only describe the current manual action. Explain what the process is ultimately trying to achieve.

Example:

> The goal is to validate incoming work items, process only complete and approved entries, and produce a clear report of completed, skipped, and failed items.

## Current State

Describe what currently works.

Example:

- The input Excel file can be read.
- Required columns are validated.
- A normalized CSV is created.
- The action step is not implemented yet.

## Missing / Not Yet Implemented

List open work items.

Example:

- Add validation for duplicate item IDs.
- Add login wait flow for company SSO.
- Add confirmation checks for completed actions.
- Add user-friendly summary report.

## Known Issues

List fragile areas, bugs, or things that need attention.

Example:

- Excel files with merged headers are not handled yet.
- The page selector for the submit button may change after login.
- Large files are slow because the whole workbook is currently loaded.

## Assumptions

List assumptions that still need verification.

Example:

- The input file always contains the expected sheet or section.
- Each item has a unique ID.
- Empty status means the row should be skipped.

## Last Successful Run

- Date:
- Input file:
- What worked:
- Output created:
- Notes:

## How To Run

Write simple steps for the user.

Example:

1. Put the input Excel file in `inputs/`.
2. Run the extraction script.
3. Review the validation report in `output/`.
4. Start the action step only after checking the report.

## Before Running Checklist

- [ ] VPN connected, if needed.
- [ ] Input file is available.
- [ ] Correct Excel template/version is used.
- [ ] User can log in to the legacy system manually.
- [ ] Previous run output has been reviewed.
- [ ] Backup created before risky changes.

## Notes for the Agent

Before changing code, read this file and inspect the latest run artifacts.

## Template Status

This starter template is documentation-first, but users do not need to fill every document before work can begin.

What works now:

- `AGENTS.md` tells the agent to clarify goals, risks, examples, and stop conditions before implementation.
- `README.md` gives the user a simple first prompt.
- `inputs/templates/` contains optional worksheets for intake, bugs, and project scope.
- `docs/` contains deeper guidance for discovery, Excel/Office files, UI automation, backups, and diagnostics.

Next useful improvement:

- Add a tiny example project that shows a completed intake, status file, run artifact, and safe first implementation.
