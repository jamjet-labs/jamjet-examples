# JamJet Framework Integrations

Community-built integrations showing JamJet alongside popular AI frameworks.
Each integration demonstrates a real production-safety capability — durability,
audit trails, human approval, policy enforcement, cost governance, or memory —
that the framework alone doesn't provide.

> 🎁 **Swag slots remaining: 10 / 10**
>
> The first 10 merged integrations earn a JamJet T-shirt + sticker pack
> (worldwide shipping). Plus a permanent author credit, social shoutout from
> [@jamjet](https://twitter.com/jamjet), JamJet Discord `Integration
> Contributor` role, and a 24-hour first response on your PR.

---

## Available slots

| # | Framework | Language | Pattern | Status | Issue |
|---|-----------|----------|---------|--------|-------|
| 1 | LangChain | Python | B | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Flangchain) |
| 2 | LlamaIndex | Python | B (mcp-native) | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Fllamaindex) |
| 3 | CrewAI | Python | B | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Fcrewai) |
| 4 | AutoGen | Python | B | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Fautogen) |
| 5 | Pydantic-AI | Python | B (mcp-native) | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Fpydantic-ai) |
| 6 | DSPy | Python | B | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Fdspy) |
| 7 | Spring AI | Java | B (extension) | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Fspring-ai) |
| 8 | LangChain4j | Java | B (extension) | 🟢 Open | [Claim →](../../issues?q=is%3Aissue+is%3Aopen+label%3Aframework%2Flangchain4j) |

> Pattern variants: `(mcp-native)` = the framework already speaks MCP natively; `(extension)` = uses an existing JamJet binding for that ecosystem.

---

## How to contribute

1. **Pick a slot** from the table above and click "Claim →".
2. **Comment** "I'd like to claim this slot" on the issue. A maintainer will
   assign it to you within 24 hours.
3. **Copy the template** at [`_template/python/`](_template/python) or
   [`_template/java/`](_template/java) into a new folder named after the
   framework (e.g., `integrations/langchain/`).
4. **Build it** following the merge bar in
   [`CONTRIBUTING-INTEGRATIONS.md`](../CONTRIBUTING-INTEGRATIONS.md).
5. **Open a PR.** A maintainer will respond within 24 hours and review.
6. **Get merged.** Receive your shoutout, Discord role, and (if you're in the
   first 10) a swag form link.

> ⏱ **Slot expiry:** if no PR is opened within 14 days of claim, the slot
> returns to the pool. Reclaiming is allowed.

---

## Pattern B (encouraged)

> Keep the framework's normal API in place. Plug JamJet in as the durable /
> governance / memory layer underneath.

This is the highest-leverage pattern: existing framework users adopt JamJet
without rewriting their code. Patterns A (JamJet wraps framework) and C
(side-by-side comparison) are also accepted with reviewer judgment.

---

## What you get for contributing

| Reward | Detail |
|--------|--------|
| **Author credit** | Your `@handle` permanently in your integration's README. |
| **Index entry** | Your `@handle` listed permanently in the "Authors" section of this index. |
| **Social shoutout** | [@jamjet](https://twitter.com/jamjet) posts on X + LinkedIn tagging you within 48h of merge. |
| **Discord role** | `Integration Contributor` badge in the JamJet Discord. |
| **Swag** | T-shirt + sticker pack mailed worldwide — first 10 merged contributors only. |
| **Conference exposure** | Standout integrations selected for demos in upcoming JamJet conference talks (Devoxx, Spring I/O, and others). |
| **Fast review** | Maintainer first response within 24h on every PR. |

---

## Authors

_This list updates as PRs merge._

_No integrations merged yet — be the first._

---

## Cross-promotion

⭐ Star [JamJet](https://github.com/jamjet-labs/jamjet) — the runtime these
integrations are built on.

🚀 Run integrations in production with multi-tenancy + dashboards →
[JamJet Cloud](https://app.jamjet.dev)

💬 Ask in the `#integrations` channel of [JamJet Discord](https://discord.gg/gdx5hM5F).
