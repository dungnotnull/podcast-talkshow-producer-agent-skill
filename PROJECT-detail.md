# PROJECT-detail.md — Podcast / Talkshow Content & Script Producer (Skill #156)

## Executive Summary
Produces in-depth podcast/talkshow content and scripts using compelling narrative structures and trending-topic intelligence. This skill is a full Claude harness in the **marketing-content-branding** cluster. It runs a research-first, framework-grounded workflow that scores the subject against named world-renowned methodologies and returns a prioritized improvement roadmap, while continuously updating its knowledge base.

## Problem Statement
Podcasts lose listeners to weak cold opens, flat segment pacing, and stale topics. This skill structures episodes around narrative arcs, writes interview/segment scripts, and scores retention potential against trend data.

## Target Users & Use Cases
Practitioners, reviewers, and decision-makers who need an expert-grade, evidence-based assessment in this domain. Trigger examples:
1. **Episode plan** — User: "Outline an episode on remote work" -> Skill builds arc/segments, scores pacing, suggests hook.
2. **Interview script** — User: "Prep questions for a founder guest" -> Skill ladders questions, scores depth, flags flow.
3. **Cold open** — User: "Write a gripping cold open" -> Skill drafts hook, scores first-minute retention.
4. **Series arc** — User: "Plan a 6-episode season" -> Skill maps season arc, topic trend fit.
5. **Degraded mode** — User: "Plan offline" -> Falls back to brain structures, flags trend data stale.

## Harness Architecture
```
/podcast-talkshow-producer (main.md)
   ├── sub-intake .................... Intake & Context Gathering
   ├── sub-framework-selector ........ Evaluation Framework Selector
   ├── sub-scoring-engine ............ Scoring Engine
   ├── sub-improvement-roadmap ....... Improvement Roadmap
   ├── [research] WebSearch/WebFetch + SECOND-KNOWLEDGE-BRAIN
   ├── [challenge] devil's-advocate assumption review
   └── synthesize ................... professional deliverable + quality gates
```

## Full Sub-Skill Catalog
### sub-intake — Intake & Context Gathering
- **Purpose:** Collect the structured inputs, scope, and goals needed to run the analysis; ask clarifying questions when key facts are missing.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-framework-selector — Evaluation Framework Selector
- **Purpose:** Pick the most appropriate named world-renowned framework(s) for the case and justify the choice.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-scoring-engine — Scoring Engine
- **Purpose:** Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.
### sub-improvement-roadmap — Improvement Roadmap
- **Purpose:** Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
- **Inputs:** case context from prior stage.
- **Outputs:** structured result passed to the next stage.
- **Tools:** Read, WebSearch/WebFetch (as needed).
- **Quality gate:** output is complete, evidence-cited, and consistent with frameworks before proceeding.

## Evaluation Frameworks (World-Renowned, Citable)
| Framework / Standard | Role in this skill |
|---|---|
| Story Circle (Dan Harmon) | Episode-level narrative arc. |
| Three-act interview structure | Setup, exploration, payoff for guest segments. |
| Cold open / hook design | First-60-seconds retention. |
| Segment pacing & signposting | Rhythm, transitions, listener orientation. |
| Question laddering (open→probing) | Eliciting depth from guests. |

## Scoring Model
| Dimension | Weight | What is assessed |
|---|---|---|
| Episode structure & arc | 25% | coherent narrative through-line |
| Hook / cold open | 20% | first-minute retention |
| Segment pacing & transitions | 20% | rhythm, signposting, energy |
| Host–guest dynamics & questions | 20% | question laddering, depth, flow |
| Topic relevance & trend alignment | 15% | timeliness, audience pull |
Each dimension is scored 0-100 with cited evidence; the weighted total yields an overall grade (A: 90+, B: 75-89, C: 60-74, D: <60).

## Skill File Format Specification
- Frontmatter: `name`, `description`.
- Required sections: Role & Persona, Workflow (Harness Flow), Sub-skills Available, Tools, Output Format, Quality Gates.

## E2E Execution Flow
1. Parse user request; if inputs are insufficient, `sub-intake` asks targeted questions.

3. `sub-framework-selector` picks framework(s) and justifies the choice.
4. Research stage gathers highest-tier evidence (see evidence hierarchy); degrade gracefully to SECOND-KNOWLEDGE-BRAIN if offline.
5. `sub-scoring-engine` scores each dimension with citations.
6. Challenge stage stress-tests conclusions.

8. `sub-improvement-roadmap` produces ranked actions.
9. Synthesize deliverable; run Quality Gates; present.

**Error handling:** missing inputs -> ask; conflicting evidence -> present both and grade certainty; tool failure -> fallback + explicit limitation notice.

## SECOND-KNOWLEDGE-BRAIN Integration
- Sources: https://blog.pacific-content.com, https://www.edisonresearch.com, https://transom.org, https://www.npr.org/sections/npr-extra
- ArXiv categories: cs.CL, cs.SD
- Crawl queries: podcast storytelling structure retention; talkshow interview question techniques; podcast cold open hook; trending podcast topics 2026
- Append format: dated entries with Title, Authors, Year, Venue, DOI/URL, key finding, relevance.

## Supporting Tools Spec
`tools/knowledge_updater.py`: inputs = source list + queries; outputs = appended SECOND-KNOWLEDGE-BRAIN entries; schedule = weekly cron; dedup by URL/DOI hash.

## Quality Gates (must all pass before final output)
- Every score cites at least one source or the chosen framework.
- Challenge stage completed; key assumptions tested.
- Roadmap items are prioritized by effort and impact and traceable to findings.
- Limitations and evidence certainty are stated explicitly.

## Test Scenarios
1. **Episode plan** — User: "Outline an episode on remote work" -> Skill builds arc/segments, scores pacing, suggests hook.
2. **Interview script** — User: "Prep questions for a founder guest" -> Skill ladders questions, scores depth, flags flow.
3. **Cold open** — User: "Write a gripping cold open" -> Skill drafts hook, scores first-minute retention.
4. **Series arc** — User: "Plan a 6-episode season" -> Skill maps season arc, topic trend fit.
5. **Degraded mode** — User: "Plan offline" -> Falls back to brain structures, flags trend data stale.

## Key Design Decisions
1. Framework-grounded scoring (no ad-hoc criteria).
2. Research-first with graceful degradation to the local knowledge brain.
3. Mandatory challenge stage to counter confirmation bias.
4. standard quality gates enforced before delivery.
5. Self-improving knowledge base via weekly crawl.
