# CLAUDE.md — Podcast / Talkshow Content & Script Producer (Skill #156)

**Slug:** `podcast-talkshow-producer`  •  **Cluster:** `marketing-content-branding`  •  **Source idea:** 156  •  **Phase:** Built (v1)

## Tagline
Produces in-depth podcast/talkshow content and scripts using compelling narrative structures and trending-topic intelligence.

## Problem This Skill Solves
Podcasts lose listeners to weak cold opens, flat segment pacing, and stale topics. This skill structures episodes around narrative arcs, writes interview/segment scripts, and scores retention potential against trend data.

## Harness Flow Summary
1. **Intake** (`sub-intake`) — gather structured inputs, scope, goals.

2. **Framework selection** (`sub-framework-selector`) — choose named world-renowned framework(s).
3. **Research** (WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN) — gather highest-tier evidence.
4. **Scoring** (`sub-scoring-engine`) — multi-dimensional weighted scores with citations.
5. **Challenge** — devil's-advocate review of assumptions and weak evidence.

**Roadmap** (`sub-improvement-roadmap`) — prioritized effort/impact recommendations.
**Synthesize** — assemble the professional deliverable; pass Quality Gates.

## Gates
- No mandatory safety/compliance gate for this cluster, but the standard Quality Gates below still apply.

## Sub-skills
- `skills/sub-intake.md` — Intake & Context Gathering: Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- `skills/sub-framework-selector.md` — Evaluation Framework Selector: Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- `skills/sub-scoring-engine.md` — Scoring Engine: Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- `skills/sub-improvement-roadmap.md` — Improvement Roadmap: Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.

## Tools Required
- `WebSearch`, `WebFetch` — live evidence and standards updates
- `Read`, `Write` — load knowledge base, emit deliverables
- `Bash` — run `tools/knowledge_updater.py`
- Skill tool — invoke sub-skills in sequence

## Knowledge Sources
- ArXiv: cs.CL, cs.SD
- Authoritative domain sources:
  - https://blog.pacific-content.com
  - https://www.edisonresearch.com
  - https://transom.org
  - https://www.npr.org/sections/npr-extra
- Crawl queries: podcast storytelling structure retention; talkshow interview question techniques; podcast cold open hook; trending podcast topics 2026

## Supporting Tools
- `tools/knowledge_updater.py` — crawl4ai pipeline that grows `SECOND-KNOWLEDGE-BRAIN.md` (weekly cron recommended).

## Active Development Tasks
- [x] Scaffold full deliverable set
- [x] Define 4 sub-skills
- [ ] Expand SECOND-KNOWLEDGE-BRAIN with first live crawl
- [ ] Add regression cases from real user runs

## Related Root Docs
- `PROJECT-detail.md` — full technical spec
- `PROJECT-DEVELOPMENT-PHASE-TRACKING.md` — phase roadmap
- `SECOND-KNOWLEDGE-BRAIN.md` — self-improving knowledge base
