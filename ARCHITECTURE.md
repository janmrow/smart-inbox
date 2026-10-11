# Smart Inbox — Architecture

[SPEC.md](SPEC.md) defines the product. This document describes the current implementation and the boundaries for its evolution. [PLAN.md](PLAN.md) owns delivery status and sequence.

## Current implementation

The application is a one-shot Python process using the standard library for email transport. It handles one dedicated Gmail account and one configured sender.

```text
environment configuration
  → connect to Gmail IMAP and select INBOX
  → find unread candidates matching the sender filter
  → fetch without setting Seen
  → parse and check the exact From address
  → build a plain-text echo reply
  → send through Gmail SMTP with STARTTLS
  → mark the handled message Seen
  → exit
```

At most one reply is sent per run. Unmatched messages stay unread. If no eligible unread message is found, the process exits with a status message.

### Code and tooling map

| File | Current responsibility |
| --- | --- |
| [src/smart_inbox/__main__.py](src/smart_inbox/__main__.py) | Configuration, IMAP/SMTP flow, and reply construction |
| [src/smart_inbox/__init__.py](src/smart_inbox/__init__.py) | Package marker |
| [tests/test_smoke.py](tests/test_smoke.py) | Reply content and headers, multipart plain-text selection, and sender filtering |
| [pyproject.toml](pyproject.toml) | Python requirement, package build, and development dependencies |
| [uv.lock](uv.lock) | Reproducible dependency resolution |
| [Makefile](Makefile) | Aggregate lint, format, and test checks |

There are no AI providers, research tools, consultation planner, persistent processing state, scheduler, or deployment configuration in the current application.

### Input and reply contracts

Configuration uses `SMART_INBOX_EMAIL`, `SMART_INBOX_APP_PASSWORD`, and `SMART_INBOX_ALLOWED_SENDER`. The local command and setup are documented in [README.md](README.md).

The IMAP `FROM` search is a candidate filter. `build_reply` parses the message and accepts exactly one `From` header containing exactly one address whose address matches the configured sender case-insensitively. This filters addresses; it does not authenticate the sender.

The parser selects the plain-text body, including from multipart messages. A message without a plain-text body raises an error. Attachments and HTML-only input are not supported as consultation inputs.

The reply is addressed to the accepted sender and includes a subject, date, and message ID. If the incoming message has a message ID, the reply includes threading headers. The current body is `You wrote: ...`.

### Failure and state boundaries

Messages are fetched with `BODY.PEEK[]`. The handled message is marked `Seen` only after SMTP sending succeeds. This preserves unread state before sending, but is not durable duplicate protection.

If SMTP succeeds and marking the message fails, another run can send the reply again. A send failure can also leave delivery outcome uncertain. Current error paths raise errors or exit; there is no explicit retry or recovery policy and no configured network timeout.

Tests cover reply construction and sender filtering, not the full transport or these failure windows. Real integration verification must be recorded separately.

## Intended consultation design

The conceptual responsibilities in [SPEC.md](SPEC.md) will be implemented incrementally. This section records boundaries, not an implemented module layout.

### Transport and consultation

Email transport should supply the accepted question and deliver the resulting answer. The consultation workflow should choose the work and produce one final answer. Preserve existing sender, mailbox, and threading behavior when replacing echo content.

Do not split the application into empty layers before a working capability needs that separation. The conceptual stages can share functions or model calls.

### Adaptive work and model roles

The workflow should recognize the problem and knowledge needs, then choose among working capabilities. A small task can finish with one model; further analysis, research, or another model should have a reason and a bounded scope.

Analysis, complementary interpretation, critique, and synthesis are possible roles, not a permanent team or mandatory call sequence. Distinct models should be selected for useful contributions. Additional calls and model agreement alone do not establish better results.

The final step should resolve material disagreements, retain relevant uncertainty, and produce one coherent consultation. Intermediate model outputs should remain internal.

### Limits and failure policy

Introduce limits together with each external capability: timeouts, maximum work, and cost or usage bounds. Check the limits before starting additional work; do not rely solely on model instructions to enforce them.

Each capability needs an explicit policy for unavailable services, insufficient evidence, and exhausted limits. A task can stop or use a simpler path where justified, but the final answer must not hide material limitations or claim research that did not occur.

The duplicate-processing and recovery policy must describe supported failure cases and uncertainty around SMTP delivery. Do not promise exactly-once delivery across independent mail and local-state operations.

### Privacy and tool access

Email contents, personal context, and external sources are inputs to analyze. Their text cannot grant tool permissions or override application limits.

The application should control which tools are available and how they are used. Arbitrary shell or system access is outside the product scope. External content should be handled as untrusted input.

Minimize private information sent to model providers and research services. Search queries should not copy unnecessary personal details. Credentials and private context stay outside the repository.

### Diagnostics

Keep enough diagnostics to identify the selected path, important decisions, service failures, elapsed time, and cost or usage. Record what can be measured; do not label a rough estimate as a billed amount.

Do not log full private emails, personal context, or internal model reasoning by default. The user-facing reply should include relevant evidence and limitations, while operational traces remain separate.

### Deployment boundary

Mikrus is the intended small production environment. The current one-shot command is the starting point; process scheduling, restart behavior, state location, and deployment commands will be chosen when implementing regular operation.

## Decisions intentionally left open

Choose concrete model and research integrations, routing criteria, role combinations, limits, persistence, and scheduling when implementing the relevant slice. No provider framework, fixed specialist taxonomy, routing service, or private-context mechanism is prescribed.

Keep adopted decisions and the current implementation description here. Keep task order, acceptance checks, and verification results in [PLAN.md](PLAN.md).
