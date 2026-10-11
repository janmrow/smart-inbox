# Agent Instructions

## Goal

Help build Smart Inbox as the personal, adaptive AI consultation inbox defined in [SPEC.md](SPEC.md).

Keep the system small, understandable, testable, and useful. Complexity must earn its place.

A coding agent changes this repository. A model taking an analytical or critical role inside the application participates in a consultation. These are separate contexts; a product role does not prescribe a development-agent workflow.

## Sources of truth

The current user task defines the authorized scope and takes precedence over repository guidance. Within that scope, read:

1. [SPEC.md](SPEC.md) for product identity, scope, and answer quality;
2. [PLAN.md](PLAN.md) for delivery status and the next proposed step;
3. [ARCHITECTURE.md](ARCHITECTURE.md), relevant code, and tests for data flow, boundaries, and existing behavior;
4. [README.md](README.md) for the public description and working setup commands.

Each document owns a different subject. Keep detailed requirements in their owning document and link to them elsewhere. Resolve discrepancies against the current task and actual implementation; report material uncertainty rather than invent requirements.

The roadmap is not authorization to implement every step. The previous single-LLM and fixed-routing specification in Git history is historical context, not an active contract.

## Working rule

**One commit, one meaningful building block.**

A feature commit should add one concrete capability to the working application. A documentation change can be one coherent update to project definition and guidance.

Do not implement future delivery steps early or create abstractions for hypothetical use. Respect requested review boundaries: leave changes unstaged and uncommitted when requested, and do not commit without user authorization.

## Before changing code

- inspect the current branch, working tree, implementation, and relevant tests;
- identify the delivery step and trace the end-to-end data flow;
- state a short plan with scope, expected behavior, and verification;
- choose the smallest complete change that satisfies the current task.

Existing tests and behavior are contracts to preserve unless the task deliberately changes them. For example, adding AI answers replaces the echo-content contract while retaining relevant sender and email-thread behavior. Update affected tests to assert the intended result.

## Implementation

- build vertical slices, not empty layers;
- extend working code and prefer concrete integrations until repeated real cases justify an abstraction;
- keep dependencies and moving parts limited;
- avoid unrelated refactoring or cleanup;
- keep credentials and private user data out of the repository;
- preserve mailbox safety and document any changed failure or recovery behavior;
- implement model and tool limits alongside capabilities that spend money or perform external work.

A small amount of duplication is better than a premature abstraction. A conceptual stage in the product flow does not require its own module, agent, or API call.

## Verification

Code changes should have the smallest useful automated coverage. Run `make verify` before considering an implementation change complete; it checks linting, formatting, and tests.

Every feature should remain easy to verify manually through:

```text
send email → observe the system → receive reply
```

Use real integrations to validate integration behavior. Local tests and mocks can verify contracts and failures, but do not establish real email delivery, provider behavior, or consultation quality.

Keep three kinds of evidence separate:

- automated checks for behavior and safety contracts;
- real end-to-end checks for the email and external-service path;
- representative question comparisons for probabilistic answer quality, cost, time, and reliability.

If credentials, external access, or a suitable test mailbox are unavailable, state that E2E was not run and give the exact manual steps. Do not describe a missing check as passed.

For documentation-only changes, review all changed and new files, check links and commands against the repository, and run `git diff --check` for tracked changes. Inspect untracked files and check their whitespace separately; ordinary `git diff` omits them. Email delivery and paid model calls are not needed for that task.

## Experiments

Before adding a workflow, state its hypothesis, compare it with the existing working path, and define what result would justify adoption. Use non-private examples in repository artifacts.

More text, model agreement, and additional calls do not by themselves demonstrate better answers. Evaluate material omissions, evidence, uncertainty, and practical usefulness together with cost and time.

Keep disposable experiments separate from the production path. Adopt only the part supported by results and required by the current task.

## Task workflow

1. Inspect and state the narrow plan.
2. Implement the smallest complete change.
3. Run applicable automated checks.
4. Perform an applicable real E2E check, or provide exact manual steps and identify what remains unverified.
5. Review the full diff, including new files.
6. Update the owning documents when behavior, design decisions, or delivery status change.
7. Report what is implemented, automatically checked, checked E2E, proposed, or unverified, and any material remaining risk.
8. Stop at the requested boundary.

Do not continue into the next delivery step unless explicitly asked.

## Scope control

When extra work appears useful, ask:

- Is it required by the current task?
- What concrete problem does it solve now?
- What materially breaks if it is deferred?
- Can it be added later without significant cost?

If the added complexity does not clearly earn its place, defer it. Keep justified complexity when it materially improves correctness, security, privacy, reliability, or required quality.
