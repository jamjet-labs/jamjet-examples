# {{Framework Name}} × JamJet — {{One-line value prop}}

> **Replace this whole header line with your SEO title.**
> Example: `# Durable LangChain Agents with JamJet`

**Language:** Python 3.11+
**Framework version:** `{{framework}}=={{X.Y.Z}}`  ← pin to a specific version
**JamJet version:** `jamjet>={{X.Y.Z}}`
**Pattern:** B (framework-wraps-JamJet)

## What JamJet Adds

> **REQUIRED.** Pick at least one of: durability, audit, HITL, policy, cost,
> memory. Explain in 2-3 sentences how this integration uses it.

This integration shows {{Framework}} agents wrapped in a JamJet `Workflow`,
where each step is checkpointed via `@workflow.step`. If the process dies
mid-step, JamJet replays from the last completed step on restart — completed
LLM calls and tool calls are skipped, so you don't re-pay for them.

## How to Run

```bash
# Prerequisites: uv installed (https://docs.astral.sh/uv/), OpenAI API key
export OPENAI_API_KEY=sk-...

uv sync
uv run python main.py
```

Expected output:

```
replace me
```

(The template returns a placeholder string. Replace `run()` with your real
{{Framework}} call to see the durable workflow in action.)

## See It In Action

> **REQUIRED.** Insert a screenshot OR a terminal-output snippet here that
> proves the JamJet capability works end-to-end.
>
> Once you've wired in a real {{Framework}} agent, demonstrate the durable
> moment: kill the process mid-step and re-run; the workflow should resume
> from the last checkpointed step.

```
$ uv run python main.py &
[step] start: query=...
[step] {{Framework}} called: ...
$ kill %1                              # crash mid-step
$ uv run python main.py
[step] resumed at: <checkpointed-step>  # skipped already-completed work
[step] result: ...
```

## Built by

[@your-github-handle](https://github.com/your-github-handle) — first JamJet ×
{{Framework}} integration.

---

⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime this
integration is built on.

🚀 Run this in production with multi-tenancy + dashboards →
[JamJet Cloud](https://app.jamjet.dev)
