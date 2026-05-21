# UI Automation Protocol

UI automation is fragile. Use it only when better options are not available.

## Preferred Order

Try these first:

1. API,
2. batch import,
3. export/import files,
4. direct structured data access,
5. UI automation.

## Login and SSO

Do not assume login can be automated.

Company systems often use:

- SSO,
- 2FA,
- password prompts,
- VPN checks,
- remembered account selection.

The automation should:

1. open the login or target page,
2. wait for the user if needed,
3. allow the user to click account name / enter password / approve 2FA,
4. detect when the actual target page is loaded,
5. continue only after page readiness checks.

Never hardcode passwords.

## Human Takeover

For fragile flows, support human takeover.

Useful behavior:

- pause automation,
- show instructions to the user,
- allow the user to perform the next action,
- record what changed,
- continue after the target page/state is reached.

## Exploration Mode

When selectors or flows are unknown, create exploration tooling.

Exploration mode may:

- inspect DOM structure,
- list visible buttons/inputs,
- save screenshots,
- record user clicks/typing,
- save discovered selectors,
- produce a summary for the agent.

## Production Mode

After exploration succeeds:

- remove unnecessary full-page scans,
- use stable selectors,
- add readiness checks,
- measure timings,
- log key decisions,
- take screenshots only when useful.

## Avoid

Avoid:

- fixed long sleeps,
- clicking by screen coordinates,
- repeated exploratory searches in normal runs,
- ignoring slow steps,
- continuing after unknown page states.

## Agent Prompt Template

```text
We need UI automation, but first check whether API/import/export alternatives exist.

If UI automation is necessary, design it with:
- login wait for SSO/2FA,
- page readiness checks,
- screenshots on failure,
- pause/resume support,
- human takeover for unknown steps,
- run artifacts for debugging.

Do not hardcode credentials.
Do not assume the login flow is stable.
```
