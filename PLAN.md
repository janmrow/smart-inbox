# Smart Inbox — Delivery Plan

[SPEC.md](SPEC.md) owns the product requirements. [ARCHITECTURE.md](ARCHITECTURE.md) describes the implementation and design boundaries. This document owns delivery status, order, and verification criteria.

## Current position

The project has a runnable Gmail email echo. The documentation refresh for adaptive consultation is implemented and awaiting manual review; implementation of the next capability is not part of that task.

| Building block | Implementation status | Verification status |
| --- | --- | --- |
| Project definition | Updated to the adaptive consultation direction; manual review pending | Five documents reviewed; local links and whitespace checks passed |
| Python bootstrap | Implemented | `make verify` passed during the documentation refresh |
| Gmail email echo | Implemented | Three automated reply/sender tests passed; real Gmail E2E is not recorded here |
| Operational safeguards beyond sender filtering | Not implemented | Not verified |
| AI consultation, research, and adaptive orchestration | Not implemented | Not verified |
| Regular Mikrus operation | Not implemented | Not verified |

The existing allowlist and ignored `.env` are part of the baseline. They do not imply full sender authentication, durable duplicate protection, or complete failure handling.

Record actual verification when it occurs. Implemented, checked automatically, checked E2E, proposed, and unverified are separate statuses.

## Delivery rules

Build small, working vertical slices. Each feature should leave the email loop usable and have a concrete manual check.

Only the current user task is authorized. A proposed next step or later roadmap entry is not permission to implement it. Stop after the requested task.

The next proposed implementation work is to verify and strengthen the email loop before adding paid AI processing. Later steps are directions; refine their scope using evidence from completed work.

## 0. Documentation refresh — implemented, manual review pending

**Goal:** make the new identity, existing behavior, and development direction clear.

**Scope:** update `README.md`, `SPEC.md`, and `AGENTS.md`; add `ARCHITECTURE.md` and this plan. Preserve the code, dependencies, repository name, and Git history. The previous specification remains available in history.

**Acceptance:** documents have distinct ownership, incorporate the refreshed vision, describe the existing echo accurately, and identify the proposed next step without presenting future capabilities as implemented.

**Verification:** review every changed and new document, check local links and commands against the repository, and run `git diff --check` for tracked changes. Check new, untracked files separately. No mailbox or paid integration check is needed. Leave changes available for the requested manual review.

**Recorded results:** all five documents were reviewed against the code and the refreshed vision. All local links resolve; code fences, whitespace, final newlines, and file modes passed checks. `make verify` passed Ruff linting, formatting, and all three tests. Code and dependencies were unchanged. Real Gmail E2E and AI quality checks were not run for this documentation task; the remaining echo check is documented in [README.md](README.md). Changes are unstaged and uncommitted for manual review.

## 1. Email-loop verification and operational safeguards — proposed next work

**Goal:** establish a predictable email foundation before external AI work adds cost and additional failure points.

**Scope:** perform the real echo check, add explicit transport timeouts, and define processing state and recovery for duplicate prevention. Implement safeguards as separate meaningful building blocks where needed.

**Preserve:** exact parsed-address filtering, unrelated unread messages, plain-text input, reply threading, and at most one handled message per invocation unless a task explicitly changes that behavior.

**Acceptance:** network work has explicit limits; the supported duplicate-prevention and recovery cases are documented and tested; uncertain SMTP outcomes and the send/mark-read failure window are accounted for without an exactly-once guarantee. Private operational state stays outside tracked files.

**Automated checks:** run `make verify` and add narrowly scoped tests for introduced failure and state behavior. Local simulations establish recovery contracts, not real mail delivery.

**Manual E2E:** follow the echo procedure in [README.md](README.md) using a dedicated test mailbox. Run again after success and confirm that the handled message does not receive another reply. Observe that the unrelated sender's message remains unread. Record real results; exercise new recovery behavior only with a controlled test setup.

**Dependencies:** suitable Gmail credentials and test messages. Credentials must not enter the repository or verification report.

**Deferred:** models, research, a scheduler, a general mail-provider abstraction, and new input formats.

## Later delivery direction

These steps are not implementation-ready task specifications. Before starting each one, define the smallest complete scope, relevant files, exclusions, acceptance criteria, automated checks, exact E2E procedure, and external dependencies.

| Step | Working increment | Acceptance and verification direction |
| --- | --- | --- |
| 2. Single-model consultation | Replace echo with one useful AI answer using one concrete integration | Preserve email contracts; introduce provider limits and basic elapsed-time/cost or usage reporting. Send a real question and receive the model answer. Test introduced behavior and failures; establish the comparison baseline. |
| 3. First adaptive work choice | Recognize the matter and choose between two working depths of analysis | Keep the decision bounded and inspectable. Check simple and harder representative emails, the selected paths, and resulting answers. A route label alone is not a working capability. |
| 4. Research | Add bounded external research for questions needing current or external knowledge | Validate real retrieval, relevant source links, and handling of missing or weak results. Use real email questions requiring sources; check limits and failure contracts automatically. |
| 5. Multimodel consultation | Add a second distinct model for selected cases and critically synthesize findings | Return one answer, examine disagreements, and handle additional-service failures. Compare real consultations with the existing path to identify benefits and costs. |
| 6. Adaptive selection across capabilities | Choose models, tools, research, and critique among already working options | Show justified economy on simple cases and escalation on difficult ones. Inspect decisions, limits, answer quality, and failure behavior through representative real emails. |
| 7. Regular Mikrus operation | Run the working consultation service without manual invocations | Choose simple scheduling and state management. Verify deployment, restart, update, recovery, and resource limits through several real email cycles. Record remaining operational limitations. |

Useful role combinations and deeper orchestration should follow question comparisons. Do not introduce a fixed model team or generic agent framework to prepare for these steps.

Answer quality is evaluated from the first AI slice onward. Regular production deployment can be revisited earlier if actual use makes it necessary; the roadmap should then explain the concrete reason.

## Consultation evaluation

Start with a small set of non-private representative questions when implementing the first AI capability. Use real model or research services for claims about their behavior. Keep a written hypothesis and compare proposed changes with the current working path.

The set should cover:

- a simple matter that should finish without escalation;
- a question requiring current sources;
- a decision with material tradeoffs;
- an ambiguous or cross-domain problem;
- a question where another analysis could expose a significant omission;
- a service failure or exhausted-work limit as a separate reliability scenario.

Judge whether the answer addresses the actual problem, covers important considerations, uses suitable evidence, represents uncertainty, and helps the user act. Consider cost, time, and reliability alongside those qualities. Automated contract checks and human assessment of probabilistic answers have different purposes.

Record material improvements, regressions, and inconclusive results. More text, more models, more calls, or model agreement alone is not a success criterion. A workflow may help one class of question while being wasteful for another; that result should inform routing.

Public examples and results must not contain private email contents or credentials. Do not build an evaluation platform before the small comparison process proves insufficient.

## Deferred possibilities

Personal context, further tools, additional models, or more specialized domain handling can be proposed when actual questions demonstrate their value. They are not prerequisites for the current task or the first single-model consultation.

## Handoff and maintenance

At task completion, update the relevant status and record:

- the concrete capability or documentation change delivered;
- automated checks actually run and their outcome;
- real E2E checks actually run, or exact remaining manual steps;
- quality-comparison evidence when applicable;
- material limitations and the next proposed step.

Keep this plan focused on the current state and next work. Use Git history for detailed past changes and temporary task plans for implementation details that do not belong in permanent documentation.
