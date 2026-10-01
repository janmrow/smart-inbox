# Smart Inbox — Product Specification

## Purpose

Build a small personal assistant that receives a question, decides how much work it needs, optionally researches it, and returns a concise, useful answer.

The project should also remain a practical environment for learning AI workflows, testing, data flow, deployment, and information security.

## User flow

For the first version:

1. the user sends an email to a dedicated mailbox;
2. Smart Inbox receives the message;
3. the system decides whether the question can be answered directly or needs web research;
4. when needed, the system performs limited research;
5. one LLM receives the question, relevant inputs, and a small private user context;
6. Smart Inbox sends the answer by email.

The complete path from incoming message to outgoing reply should remain easy to inspect and explain.

## First-version requirements

Smart Inbox should:

- receive email from an authorized sender;
- send replies by email;
- generate answers with one LLM;
- use Jev to choose between `direct` and `research`;
- perform limited web research for the research path;
- use a small private user-context file;
- avoid processing the same message twice;
- keep secrets and private context outside the public repository;
- handle ordinary failures predictably;
- expose enough logging to understand what happened;
- run reliably on a small VPS.

Answers should be concise, relevant, and useful.

## Non-goals

Do not add these unless real use later creates a clear need:

- a web UI;
- a custom mail server;
- multiple collaborating LLM agents;
- an agent framework;
- vector databases or general RAG infrastructure;
- autonomous shell or system access for models;
- context routing;
- judge or evidence agents;
- message queues or Redis;
- elaborate observability;
- a general evaluation platform;
- multi-user or large-scale architecture.

Email is the first interface, not a permanent architectural requirement. Other entry points may be explored later if they become useful.

## Delivery sequence

From the email loop onward, each step should leave the application working and manually testable end-to-end.

### 1. Project definition

Add the public project documentation.

### 2. Bootstrap

Create the runnable project, dependency setup, verification command, and at least one simple automated test.

### 3. Email loop

Receive a real email and reply with its subject or body.

**Manual check:** send an email and receive the echo reply.

### 4. LLM answer

Replace the echo with an answer from one LLM.

**Manual check:** send a question and receive a useful AI answer.

### 5. Minimum operational safety

Add the controls required for personal use:

- sender allowlist;
- secrets outside the repository;
- duplicate-message protection;
- sensible timeouts and failure handling.

### 6. Jev routing

Use Jev to classify a question as:

```text
direct
research
```

The selected route should be visible when debugging.

### 7. Research path

For `research`, perform limited web research and provide the results to the existing LLM before answering.

### 8. Personal context

Add one small private user-context file and provide it to the LLM.

Do not add context routing unless real usage later shows that it is needed.

### 9. Answer quality

Use real questions to improve prompts, research input, source handling, and answer brevity.

Prefer improving the existing flow over adding components.

### 10. Reliable VPS operation

Make the finished workflow easy to keep running:

- predictable startup and restart;
- useful logs;
- simple deployment and updates;
- recovery from ordinary failures.

At this point the first version is complete.

## Completion criteria

The first version is done when:

- sending an authorized email reliably produces a reply;
- current questions can use web research;
- answers are concise and useful;
- private data and secrets stay private;
- ordinary failures are understandable;
- the full workflow can be explained end-to-end;
- the codebase remains small enough to inspect and change comfortably.

Anything beyond this specification should be driven by evidence from real use.
