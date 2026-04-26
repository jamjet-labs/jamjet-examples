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
class annotation paired with `@Checkpoint` methods. Each `@Checkpoint` step is
recorded in the event log; on restart after a crash, JamJet replays completed
steps as no-ops and resumes from the first incomplete one — completed LLM and
tool calls are not re-issued.

## How to Run

```bash
# Prerequisites: Java 17+, Maven 3.9+, OpenAI API key
export OPENAI_API_KEY=sk-...

mvn compile
mvn exec:java -Dexec.mainClass=Main
```

Expected output:

```
replace me
```

(The template returns a placeholder string. Replace `run()` with your real
{{Framework}} call to see the durable agent in action.)

## See It In Action

> **REQUIRED.** Insert a screenshot OR a terminal-output snippet here that
> proves the JamJet capability works end-to-end.
>
> Once you've wired in a real {{Framework}} agent, demonstrate the durable
> moment: kill the process mid-`@Checkpoint` and re-run; the agent should
> resume from the last completed checkpoint.

```
$ mvn exec:java -Dexec.mainClass=Main &
[checkpoint] start: query=...
[checkpoint] {{Framework}} called: ...
$ kill %1                                # crash mid-step
$ mvn exec:java -Dexec.mainClass=Main
[checkpoint] resumed at: <last-completed>  # skipped already-completed work
[checkpoint] result: ...
```

## Built by

[@your-github-handle](https://github.com/your-github-handle) — first JamJet ×
{{Framework}} integration.

---

⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime this
integration is built on.

🚀 Run this in production with multi-tenancy + dashboards →
[JamJet Cloud](https://app.jamjet.dev)
