# {{Framework Name}} × JamJet — {{One-line value prop}}

> **Replace this whole header line with your SEO title.**
> Example: `# Spring AI Agents with HITL Approval`

**Language:** Java 17+
**Framework version:** `{{framework}}:{{X.Y.Z}}` ← pin to a specific version
**JamJet runtime:** `dev.jamjet:jamjet-runtime-core:0.1.1+`
**Pattern:** B (framework-wraps-JamJet)

## What JamJet Adds

> **REQUIRED.** Pick at least one of: durability, audit, HITL, policy, cost,
> memory. Explain in 2-3 sentences how this integration uses it.

This integration shows {{Framework}} agents using JamJet's `@DurableAgent`
annotation for crash recovery. The agent's tool-call sequence is event-sourced;
on restart JamJet replays from the last completed step.

## How to Run

```bash
# Prerequisites: Java 17+, Maven 3.9+, OpenAI API key
export OPENAI_API_KEY=sk-...

mvn compile
mvn exec:java -Dexec.mainClass=Main
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
$ mvn exec:java -Dexec.mainClass=Main &
[1/3] Agent started, durable session id: abc123
[2/3] Tool call: web_search → 4 results
$ kill %1                                   # crash mid-flight
$ mvn exec:java -Dexec.mainClass=Main -Dresume=abc123
[2/3] Resuming from checkpoint after web_search
[3/3] Final answer: ...                      # same answer
```

## Built by

[@your-github-handle](https://github.com/your-github-handle) — first JamJet ×
{{Framework}} integration.

---

⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime this
integration is built on.

🚀 Run this in production with multi-tenancy + dashboards →
[JamJet Cloud](https://app.jamjet.dev)
