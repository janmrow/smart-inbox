# Smart Inbox — Product Specification

## Identity and purpose

Smart Inbox is a personal consultation inbox built around multiple AI models. The user emails a question, problem, or topic and receives one useful consultation.

The system should understand what the matter is really about, what kind of knowledge it requires, and how much work is worth doing. It then chooses the models, tools, research, and critical analysis appropriate to that task.

The central question of the project is: **How can a small AI system decide how much intelligence to use for a particular problem?**

**Simple interface. Adaptive intelligence underneath. One valuable answer at the end.**

This specification defines the intended product. See [ARCHITECTURE.md](ARCHITECTURE.md) for the current implementation and system boundaries, and [PLAN.md](PLAN.md) for delivery status and order.

## User experience

Email is the only primary interface in the current concept. The user does not select a model, tool, or working mode. They send their problem and receive an answer in the email thread.

Internal orchestration should stay out of the user's way. Useful sources, assumptions, and limitations belong in the answer when relevant; routing traces and individual model transcripts do not.

The system should provide one coherent consultation rather than require the user to reconcile several model responses.

## Adaptive consultation

The conceptual flow is:

```text
email
  → understand the problem
  → identify its domain and knowledge needs
  → choose the depth of work
  → select models and tools
  → research when needed
  → analyze and critically synthesize
  → send one answer by email
```

These are responsibilities, not a requirement for separate modules, agents, or API calls. A simple task may combine several responsibilities in one model call.

The system should consider the nature of the problem, ambiguity, need for current information, consequences of a poor answer, and likely value of further work. Domain recognition should help choose knowledge and methods; it does not require a fixed taxonomy of specialist agents.

Depending on the task, the system may:

- answer directly with one model;
- spend more effort analyzing a difficult problem;
- use bounded web research to gather relevant sources;
- ask different models to contribute complementary analysis or interpretations;
- critique preliminary conclusions and resolve material disagreements;
- synthesize the findings into one answer.

The system should stop when additional work is unlikely to justify its cost and time. Multiple models and research are available capabilities, not mandatory steps for every email.

The intended product includes a useful path involving distinct models. Repeating prompts to the same model may be a useful experiment, but does not by itself establish the value of a multimodel consultation.

## Answer quality

A good answer should resemble a consultation from a competent practitioner:

- address the underlying problem and the user's actual question;
- give concrete, relevant guidance at a depth proportionate to the task;
- distinguish supported facts, assumptions, interpretation, and uncertainty;
- explain important alternatives, tradeoffs, and risks when they affect the decision;
- recommend practical next steps when appropriate;
- use relevant, traceable sources when external research supports the answer;
- acknowledge missing information or limits instead of manufacturing confidence.

Conciseness should remove repetition and filler without making a difficult answer superficial. The answer need not use a fixed template or include every item above for a simple question.

Critical synthesis should examine omissions, weak evidence, and disagreements. Model agreement alone is not proof of correctness, and concatenating model responses is not synthesis.

Quality should be assessed against the working single-model path using representative questions. More text, more calls, or more models are not sufficient evidence of improvement. Compare usefulness and correctness together with cost, time, and reliability; [PLAN.md](PLAN.md) describes the evaluation approach.

## Operating constraints

- Keep the code and architecture small enough to understand, inspect, and change comfortably.
- Apply Just Enough: complexity must solve a concrete problem or add demonstrated value.
- Keep email as the primary interface and use Mikrus as the intended small production environment.
- Restrict processing to allowed senders and preserve unrelated mailbox messages.
- Keep credentials, private context, and private email contents out of the public repository.
- Treat disclosure to model and research providers as part of the privacy boundary; minimize what is sent.
- Bound model calls, research, elapsed time, and spending, and make ordinary failures understandable.
- Protect against repeated processing within an explicitly documented failure and recovery policy.
- Expose enough diagnostics to understand decisions, cost, time, and failures without collecting unnecessary private data.
- Verify integration behavior through real email delivery and real services when applicable.
- Preserve the existing repository and Git history, and develop through small working vertical slices.

## Learning goals

Smart Inbox is a practical laboratory for AI systems beyond a single model API call. It should help explore:

- recognizing the character and domain of a problem;
- choosing how deeply to work on it;
- deciding when one model is enough and when several help;
- assigning useful roles to models with different properties;
- choosing when web research or other bounded tools add value;
- comparing and critiquing different model results;
- distinguishing additional text from an actual improvement in quality;
- building useful orchestration without an unnecessary agent framework;
- observing cost, time, quality, and reliability across the process;
- moving an experiment into a small application that is regularly used.

Experiments should inform the working product. They do not justify adding every possible workflow at once.

## Non-goals and deferred choices

The current scope does not require:

- a separate web UI or another primary interface;
- a custom mail server;
- an agent framework or a general AI platform;
- vector databases or general RAG infrastructure;
- autonomous shell or system access for models;
- message queues, Redis, or large-scale infrastructure;
- elaborate observability or a general evaluation platform;
- multi-user architecture.

No particular model provider, routing service, fixed roster of roles, or private user-context file is required by this vision. Choose concrete integrations when implementing a capability. Personal context can be added later if actual use establishes its value and privacy requirements.

## First adaptive version: completion criteria

The first adaptive version is complete when:

- an email from an allowed sender reliably produces one useful reply;
- simple tasks can use a bounded single-model path;
- appropriate tasks can use web research and a useful multimodel path;
- the system chooses among those capabilities without user-selected modes;
- the final answer critically synthesizes relevant findings and uncertainty;
- evaluation provides evidence for the added work relative to the single-model baseline;
- cost, time, privacy, duplicate handling, and ordinary failures have explicit controls;
- the service runs regularly on Mikrus and has been checked end-to-end;
- the entire flow remains understandable and the codebase remains small.

These are product goals, not a claim about today's implementation. Further development should follow evidence from real use.

## Change of direction

This specification replaces the earlier single-LLM and fixed-routing vision. The earlier specification remains in Git history, including at commit `d6a44ba`, as historical context rather than an active delivery contract.
