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

This integration shows {{Framework}} agents using JamJet's `@durable_agent`
decorator for crash recovery. If the process dies mid-tool-call, JamJet replays
the agent from the last completed step on restart — without re-paying for
prior LLM calls.

## How to Run

```bash
# Prerequisites: uv installed (https://docs.astral.sh/uv/), OpenAI API key
export OPENAI_API_KEY=sk-...

uv sync
uv run python main.py
```

Expected output:

```
[1/3] Agent started, durable session id: abc123
[2/3] Tool call: web_search → 4 results
[3/3] Final answer: ...
```

## See It In Action

> **REQUIRED.** Insert a screenshot OR a terminal-output snippet here that
> proves the JamJet capability works end-to-end.

```
$ uv run python main.py &
[1/3] Agent started, durable session id: abc123
[2/3] Tool call: web_search → 4 results
$ kill %1                            # crash mid-flight
$ uv run python main.py --resume abc123
[2/3] Resuming from checkpoint after web_search
[3/3] Final answer: ...               # same answer, no re-billed LLM calls
```

## Built by

[@your-github-handle](https://github.com/your-github-handle) — first JamJet ×
{{Framework}} integration.

---

⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime this
integration is built on.

🚀 Run this in production with multi-tenancy + dashboards →
[JamJet Cloud](https://app.jamjet.dev)
