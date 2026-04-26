# Contributing a Framework Integration

Thank you for contributing! This guide walks you through building an
integration from claim to merge in 2-4 hours.

## The Flow

```
1. Claim a slot   →   2. Build it   →   3. Open PR   →   4. Get reviewed   →   5. Merge & rewards
       (24h)            (2-4 hrs)         (anytime)        (24h response)         (within days)
```

## 1. Claim a Slot

Pick from the open slots in [`integrations/README.md`](integrations/README.md).
Comment "I'd like to claim this slot" on the linked issue. A maintainer
assigns it to you within 24 hours. **Slots expire 14 days after claim** if no
PR opens — feel free to reclaim later.

## 2. Build It

Copy the relevant template and rename:

```bash
cp -r integrations/_template/python integrations/{{framework}}
cd integrations/{{framework}}
```

Replace `{{framework}}`, `{{Framework Name}}`, and other placeholders in the
README, code file, and dependency manifest.

### Pattern B (encouraged)

Keep the framework's normal API in place. Plug JamJet in as the durable /
governance / memory layer underneath. Existing framework users should be able
to adopt your integration without rewriting their agent code.

For Python, the canonical durable shape is a `Workflow` with `@workflow.step`
methods — completed steps are checkpointed and skipped on replay after a
crash. For Java, it's a `@DurableAgent`-annotated class with `@Checkpoint`
methods. Both templates demonstrate the pattern.

(Patterns A and C are accepted but reviewer-judged.)

## 3. Merge Bar — What's Required

Your PR must include:

- [ ] **README.md** with these sections in order:
  - H1 SEO title (e.g., "Durable LangChain Agents with JamJet")
  - Language declaration (`Python 3.11+` or `Java 17+`)
  - **Pinned framework version** (e.g., `langchain==0.4.x`)
  - `## What JamJet Adds` — explicitly cites at least one of the six safety
    capabilities: **durability**, **audit**, **HITL**, **policy**, **cost**,
    **memory**
  - `## How to Run` — single-command run instructions
  - `## See It In Action` — a screenshot OR terminal-output snippet
    demonstrating the capability working end-to-end (e.g., kill-and-replay,
    audit-log entry, approval gate firing)
  - **Cloud CTA footer** (verbatim):

    > 🚀 Run this in production with multi-tenancy + dashboards → [JamJet Cloud](https://app.jamjet.dev)

  - **Cross-promotion line** (verbatim):

    > ⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime this integration is built on.

  - Author credit line: `Built by [@handle](https://github.com/handle)`

- [ ] **Working code** — `main.py` / `Main.java` runnable locally with the
  framework + JamJet open-source. User-provided LLM API keys are OK.

- [ ] **No proprietary dependencies** — all deps must be free / open source
  (LLM APIs requiring user-paid keys are fine).

### What's NOT required (but appreciated — may unlock conference highlight)

- Unit tests / pytest / JUnit
- Loom / video walkthrough
- Benchmark numbers
- Docs page contribution to docs.jamjet.dev

## 4. Open the PR

Use the integration PR template (auto-suggested when you open the PR). Fill in
the checklist. A maintainer responds within 24 hours.

## 5. After Merge

Once your PR merges:

1. **Author credit** added to your integration's README.
2. **Index entry** added to `integrations/README.md` Authors section.
3. **Discord role** — drop your Discord handle in the merge comment to get
   the `Integration Contributor` role (or join via [discord.gg/gdx5hM5F](https://discord.gg/gdx5hM5F)).
4. **Social shoutout** — [@jamjet](https://twitter.com/jamjet) posts on X +
   LinkedIn within 48h.
5. **Swag (first 10 only)** — maintainer drops a Google Form link in the
   merge comment for size + shipping. Printful ships in ~2 weeks.
6. **Conference highlight** (standouts only) — if your integration includes
   tests, a video, benchmarks, or a novel pattern, the maintainer may reach
   out about featuring it in upcoming Devoxx / Spring I/O / JamJet talks.

## Questions?

Drop into the JamJet Discord [`#integrations` channel](https://discord.gg/gdx5hM5F)
or comment on your slot's issue.

---

⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime these
integrations are built on.
