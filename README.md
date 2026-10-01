# Smart Inbox

Smart Inbox is a small personal AI assistant that turns incoming questions into concise, useful answers.

Email is the first interface because it is simple, universal, and easy to test end-to-end. The interesting part of the project is the workflow behind it: decide how a question should be handled, optionally research it, and produce a good answer with an LLM.

```text
email
  ↓
decision
  ↓
optional research
  ↓
LLM
  ↓
reply
```

## Why

This project is a practical playground for:

- modern AI workflows;
- testing systems that include probabilistic components;
- web research and LLM integration;
- data flow, privacy, and basic information security;
- running a small service on a VPS.

The goal is not to build an AI platform. The goal is to keep the whole system small enough to understand, test, debug, and improve.

## Development approach

Smart Inbox is built as a sequence of small vertical slices.

Each feature commit should add one visible capability to the working system and remain easy to test manually end-to-end. New abstractions or infrastructure are added only when the current system gives a concrete reason for them.

## Status

Email echo: each run replies to one unread message from one configured sender in a dedicated Gmail account. Other unread messages stay unread. AI comes later.

Create a local `.env` file with the dedicated Gmail address and its [App Password](https://support.google.com/mail/answer/185833):

```dotenv
SMART_INBOX_EMAIL=your-address@gmail.com
SMART_INBOX_APP_PASSWORD=your-app-password
SMART_INBOX_ALLOWED_SENDER=your-other-address@example.com
```

The `.env` file is ignored by Git. After `uv sync`, send a plain-text email from the allowed address to the Gmail account and run:

```sh
uv run --env-file .env python -m smart_inbox
```

After sending the reply and marking that incoming message as read, the command prints `Echo reply sent`. Check that the reply arrives in the sender's inbox and that an unread message from another sender stays unread. If there is no unread message from the allowed sender, it prints `No unread messages from allowed sender`.

This is a one-shot manual flow. If the allowed sender has older unread messages, the oldest is processed first. Multiple senders and duplicate protection are later steps.

## Documentation

- [`SPEC.md`](SPEC.md) — product scope and delivery sequence.
- [`AGENTS.md`](AGENTS.md) — rules for agent-assisted development.

## License

MIT
