# Smart Inbox

Smart Inbox is a personal consultation inbox being built around multiple AI models. You email a question, problem, or topic; the system chooses how much analysis, research, and model collaboration it needs and returns one coherent, useful answer.

**Simple interface. Adaptive intelligence underneath. One valuable answer at the end.**

## Intended workflow

```text
email
  → understand the problem and its knowledge needs
  → choose the depth of work, models, and tools
  → research, analyze, and critique as needed
  → synthesize one consultation
  → email reply
```

This is the product direction. The current application implements the email echo described below.

The user does not choose a model or working mode. A simple question may need one model; a difficult question may benefit from sources, complementary model analyses, and critical synthesis. The answer should make relevant uncertainty, tradeoffs, risks, and next steps clear without exposing internal orchestration.

## Why

The project explores a practical question: **How can a small AI system decide how much intelligence to use for a particular problem?**

It is a laboratory for problem recognition, adaptive effort, model roles, research, and answer quality, with cost, time, privacy, and reliability considered together. Additional calls or longer answers must earn their place through useful results.

Email remains the only primary interface. Mikrus is the intended production environment; deployment is a later step. The project should stay small enough to understand, test, debug, and improve.

## Current status

Email echo is implemented for one dedicated Gmail account and one configured sender. Each run replies to at most one matching unread message. Other messages stay unread. There are no model calls, research, adaptive routing, or deployment files yet.

The implementation fetches messages without marking them read, checks the exact parsed `From` address, sends a threaded reply, and marks the incoming message read after SMTP succeeds. Address filtering is not complete sender authentication. If sending succeeds but marking the message fails, a later run may send another reply; duplicate protection and bounded failure handling are planned.

Automated tests cover reply construction and sender filtering. They do not establish real Gmail delivery; see [PLAN.md](PLAN.md) for verification status and the next proposed work.

## Local development

Use Python 3.12 or later and `uv`. Install the project and development dependencies:

```sh
uv sync
```

Run the repository checks:

```sh
make verify
```

This runs Ruff linting, Ruff formatting checks, and pytest without contacting the mailbox or AI providers.

## Manual email echo check

Create a local `.env` file with the dedicated Gmail address and its [App Password](https://support.google.com/mail/answer/185833):

```dotenv
SMART_INBOX_EMAIL=your-address@gmail.com
SMART_INBOX_APP_PASSWORD=your-app-password
SMART_INBOX_ALLOWED_SENDER=your-other-address@example.com
```

The `.env` file is ignored by Git. Keep it private.

Use a dedicated test mailbox. The command processes the oldest matching unread message first, so check for older messages from the allowed sender before expecting your new test message to be selected.

1. Send a plain-text email from the allowed address with a recognizable subject and body.
2. Leave a test email from a different sender unread in the same mailbox.
3. Run:

   ```sh
   uv run --env-file .env python -m smart_inbox
   ```

4. Confirm that the allowed sender receives a reply containing `You wrote: ...`, the reply belongs to the original thread, and the handled message becomes read.
5. Confirm that the message from the other sender remains unread and receives no reply.

After a successful run, the command prints `Echo reply sent`. If no eligible unread message is found, it prints `No unread messages from allowed sender`. This is a one-shot flow; it does not poll continuously.

## Development approach

Build small, working vertical slices. One feature commit should add one meaningful capability and remain easy to check through a real email exchange. Add abstractions and infrastructure only when the current task gives a concrete reason.

The earlier product direction remains in Git history. The current specification defines adaptive consultation; the roadmap describes how to reach it from the existing email loop.

## Documentation

- [SPEC.md](SPEC.md) — product identity, scope, answer quality, and completion criteria.
- [ARCHITECTURE.md](ARCHITECTURE.md) — current implementation, data flow, and design boundaries.
- [PLAN.md](PLAN.md) — delivery status, next proposed step, and verification criteria.
- [AGENTS.md](AGENTS.md) — workflow and scope rules for coding agents.

## License

MIT
