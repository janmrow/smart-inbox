# Agent Instructions

## Goal

Help build Smart Inbox as described in `SPEC.md`.

Keep the system small, understandable, testable, and useful. Complexity must earn its place.

## Sources of truth

Use:

1. `SPEC.md` for product scope and delivery order;
2. existing tests and working behavior for implementation contracts;
3. `README.md` for the public project description.

Do not invent requirements that are not supported by the current task or these sources.

## Working rule

**One commit, one meaningful building block.**

A feature commit should add one concrete capability to the working application.

Do not implement future delivery steps early. Do not create abstractions only because they might be useful later.

## Before changing code

- inspect the current implementation and tests;
- identify the current delivery step;
- understand the end-to-end data flow;
- choose the smallest complete change that satisfies the task.

Prefer extending working code over designing a future architecture.

## Implementation

- build vertical slices, not empty layers;
- prefer concrete code until repeated real cases justify an abstraction;
- keep dependencies and moving parts limited;
- avoid unrelated refactoring or cleanup;
- preserve working behavior unless the task requires changing it;
- keep secrets and private user data out of the repository.

A small amount of duplication is better than a premature abstraction.

## Verification

Code changes should have the smallest useful automated coverage.

Every feature commit must also remain easy to verify manually end-to-end. The preferred product-level check is:

```text
send email
→ observe the system
→ receive reply
```

Use real integrations when validating integration behavior. Do not replace an end-to-end check with mocks and treat them as equivalent.

Run the repository verification command, once it exists, before considering a change complete.

## Task workflow

For each task:

1. inspect;
2. implement the smallest complete change;
3. run applicable automated checks;
4. perform an end-to-end check when applicable, or provide the exact manual step when external access is required;
5. review the full diff;
6. report what changed, what was verified, and any material remaining risk;
7. stop.

Do not continue into the next delivery step unless explicitly asked.

## Scope control

When extra work appears useful, ask:

- Is it required by the current task?
- What concrete problem does it solve now?
- What materially breaks if it is deferred?
- Can it be added later without significant cost?

If the added complexity does not clearly earn its place, defer it.

Keep justified complexity when it materially improves correctness, security, reliability, or required quality.
