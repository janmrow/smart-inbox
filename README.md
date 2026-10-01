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

Project definition.

The first working milestone is deliberately simple:

```text
send email → receive it on the VPS → send a reply
```

AI comes after that loop works.

## Documentation

- [`SPEC.md`](SPEC.md) — product scope and delivery sequence.
- [`AGENTS.md`](AGENTS.md) — rules for agent-assisted development.

## License

MIT
