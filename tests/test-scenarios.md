# Test Scenarios — Podcast / Talkshow Content & Script Producer (Skill #156)

These scenarios validate the harness end-to-end: stage order, framework grounding, scoring with citations, gates, roadmap, and graceful degradation.

## How to Use These Scenarios

Each scenario includes:
- **User input**: The trigger request
- **Expected behavior**: What the harness should do
- **Validation criteria**: Specific checks to verify correctness
- **Expected outputs**: Sample deliverable structure

Run scenarios in sequence. Each scenario tests different aspects of the harness. If any scenario fails, diagnose the failure and fix before proceeding.

---

## Scenario 1: Episode Plan (Happy Path)

### User Input
"Outline an episode on remote work productivity for intermediate professionals. Target length: 45 minutes. Format: Solo with storytelling elements."

### Expected Behavior
Harness runs full pipeline: intake → framework selection → research → scoring → challenge → roadmap → synthesis.

### Validation Criteria
- [ ] **Stage Order**: sub-intake → sub-framework-selector → (research) → sub-scoring-engine → (challenge) → sub-improvement-roadmap → synthesis
- [ ] **Framework Named**: At least one of Story Circle or Segment pacing selected
- [ ] **Scores Cited**: Every dimension score includes source citation
- [ ] **Roadmap Prioritized**: Recommendations have effort/impact classification
- [ ] **Limitations Stated**: Limitations section present and non-empty
- [ ] **Quality Gates Pass**: All four gates (citation, challenge, traceability, limitation) checked and passed
- [ ] **Deliverable Complete**: All 7 sections present (Executive Summary through Sources)

### Expected Output Structure
```json
{
  "executive_summary": {
    "overall_grade": "B",
    "headline_findings": ["Strong narrative arc", "Hook needs improvement"],
    "immediate_actions": ["Replace opening", "Add signposting"]
  },
  "dimension_scores": [
    {"dimension": "Episode structure & arc", "score": 85, "citation": "..."},
    {"dimension": "Hook / cold open", "score": 68, "citation": "..."},
    ...
  ],
  "improvement_roadmap": [
    {"priority": 1, "recommendation": "...", "effort": "Low", "impact": "High", "traceability": "..."}
  ]
}
```

### Edge Cases Tested
- Standard episode planning workflow
- All stages execute successfully
- Framework selection logic works
- Scoring rubric applied correctly
- Roadmap generation with prioritization

---

## Scenario 2: Interview Script (Framework-Specific)

### User Input
"Prep interview questions for a tech founder guest. She built a AI company from scratch. Expert interview style. Focus on her journey and practical advice."

### Expected Behavior
Harness selects interview-specific frameworks (Three-act interview structure, Question laddering) and scores host-guest dynamics dimension heavily.

### Validation Criteria
- [ ] **Framework Specificity**: Selected frameworks include Three-act interview structure or Question laddering
- [ ] **Dimension Weighting**: Host-guest dynamics scored with interview-specific rubric
- [ ] **Question Laddering**: Recommendations include question-laddering improvements if score <90
- [ ] **Guest Profile Utilized**: Intake captured guest expertise and roadmap leverages it
- [ ] **Quality Gates Pass**: All gates pass with interview-specific considerations

### Expected Output Structure
```json
{
  "selected_frameworks": [
    {"name": "Three-act interview structure", "relevance_score": 95},
    {"name": "Question laddering (open→probing)", "relevance_score": 90}
  ],
  "dimension_scores": [
    {"dimension": "Host–guest dynamics & questions", "score": 72, "weaknesses": ["Limited laddering"]}
  ],
  "improvement_roadmap": [
    {"priority": 1, "recommendation": "Upgrade questions to laddering structure", "dimension_affected": "Host–guest dynamics & questions"}
  ]
}
```

### Edge Cases Tested
- Framework selection adapts to request type
- Dimension scoring uses request-specific rubric
- Roadmap recommendations are format-appropriate

---

## Scenario 3: Cold Open (Single-Dimension Focus)

### User Input
"Write a gripping cold open for my episode about the future of work. Current opening is 'Welcome back to another episode of [show name]. I'm [host], and today we're talking about the future of work.' This needs to be much stronger."

### Expected Behavior
Harness focuses heavily on Hook/cold open dimension, provides specific cold open alternatives with scoring rationale.

### Validation Criteria
- [ ] **Framework Selection**: Cold open/hook design framework selected
- [ ] **Specific Alternatives**: Output includes 2-3 specific cold open options
- [ ] **Hook Scoring**: Cold open options scored against hook rubric
- [ ] **Recommendation Specificity**: Roadmap includes exact replacement text
- [ ] **Pattern Interrupt**: At least one option uses pattern-interrupt technique

### Expected Output Structure
```json
{
  "selected_frameworks": [
    {"name": "Cold open / hook design", "relevance_score": 100}
  ],
  "dimension_scores": [
    {"dimension": "Hook / cold open", "score": 45, "weaknesses": ["Generic opening", "No curiosity gap"]}
  ],
  "improvement_roadmap": [
    {
      "priority": 1,
      "recommendation": "Replace with: 'By 2030, 50% of jobs as we know them will cease to exist. Today, you discover which ones — and how to make sure yours isn't one of them.'",
      "dimension_affected": "Hook / cold open",
      "expected_score": 92
    }
  ]
}
```

### Edge Cases Tested
- Single-dimension focus
- Specific deliverable (cold open alternatives)
- Direct text replacement recommendations

---

## Scenario 4: Series Arc (Multi-Episode Planning)

### User Input
"Plan a 6-episode season on personal finance for beginners. Each episode should build on the last. Target audience: people who've never budgeted before."

### Expected Behavior
Harness applies Story Circle at season level, ensures episode-to-episode continuity, scores topic relevance for series-wide appeal.

### Validation Criteria
- [ ] **Season-Level Framework**: Story Circle applied to season arc, not just episode
- [ ] **Continuity Elements**: Recommendations include recurring segments or themes
- [ ] **Episode Progression**: Output shows listener journey across episodes
- [ ] **Topic Relevance**: Trend alignment considers season-wide appeal
- [ ] **Scope Management**: Intake captured all 6 episodes and roadmap addresses series cohesion

### Expected Output Structure
```json
{
  "selected_frameworks": [
    {"name": "Story Circle (Dan Harmon)", "relevance_score": 90, "application": "Season-level narrative arc"},
    {"name": "Topic relevance & trend alignment", "relevance_score": 85, "application": "Season-wide appeal"}
  ],
  "dimension_scores": [
    {"dimension": "Episode structure & arc", "score": 78, "note": "Season arc needs strengthening"}
  ],
  "improvement_roadmap": [
    {"priority": 2, "recommendation": "Add recurring 'Money Win of the Week' segment for continuity"},
    {"priority": 3, "recommendation": "Map 6-episode listener journey: Awareness → Assessment → Budgeting → Saving → Investing → Mastery"}
  ]
}
```

### Edge Cases Tested
- Multi-episode scope
- Season-level framework application
- Continuity and progression considerations

---

## Scenario 5: Degraded Mode (Offline/No Research)

### User Input
"Plan an episode on mindful leadership. I'm offline right now, so work with what you have. Don't search the web."

### Expected Behavior
Harness falls back to SECOND-KNOWLEDGE-BRAIN.md (or frameworks if brain unavailable), flags limitations explicitly, proceeds with framework-based analysis only.

### Validation Criteria
- [ ] **Degradation Flagged**: Output explicitly states "Research unavailable" or "Working in degraded mode"
- [ ] **Framework Proceed**: Analysis continues with frameworks
- [ ] **Limitation Section**: Prominent limitation about trend alignment scoring
- [ ] **Quality Gates**: Pass despite degraded mode (frameworks sufficient for basic assessment)
- [ ] **User Transparency**: User knows which findings are framework-only vs. evidence-backed

### Expected Output Structure
```json
{
  "selected_frameworks": [
    {"name": "Story Circle (Dan Harmon)", "relevance_score": 85}
  ],
  "research_status": "Degraded mode — WebSearch unavailable; using framework-based analysis only",
  "limitations": {
    "research_availability": "Unavailable per user request",
    "affected_dimensions": ["Topic relevance & trend alignment — scored as 'Framework-only, limited by data availability'"],
    "certainty_level": "Medium — framework-based conclusions strong; trend alignment uncertain"
  },
  "dimension_scores": [
    {"dimension": "Episode structure & arc", "score": 82, "certainty": "High — framework-backed"},
    {"dimension": "Topic relevance & trend alignment", "score": 70, "certainty": "Low — no live data"}
  ]
}
```

### Edge Cases Tested
- Graceful degradation when research unavailable
- Framework-only analysis
- Explicit limitation statement
- User-requested offline mode

---

## Scenario 6: Minimal Input (Intake Clarification)

### User Input
"Help me with my podcast episode."

### Expected Behavior
Harness sub-intake asks targeted clarifying questions, does not proceed until sufficient information gathered.

### Validation Criteria
- [ ] **Questions Asked**: sub-intake asks 3-5 specific questions (topic, audience, format, goals)
- [ ] **No Assumptions**: Harness does NOT make assumptions or proceed with placeholders
- [ ] **Question Quality**: Questions are specific, targeted, and clearly necessary
- [ ] **Wait for Response**: Harness waits for user input before proceeding to next stage

### Expected Interaction Flow
```
User: "Help me with my podcast episode."
Harness: "To create the best episode plan, I need some details:
1. What's the episode topic?
2. Who's your target audience?
3. What format (solo, interview, panel)?
4. What's the primary goal?
5. Any constraints I should know about?"
[User responds...]
Harness: [Proceeds to framework selection]
```

### Edge Cases Tested
- Minimal input handling
- Clarification question quality
- No premature stage progression

---

## Scenario 7: Conflicting Evidence (Challenge Stage)

### User Input
"Outline an episode on the effectiveness of remote work vs. office work. There's a lot of debate on this topic."

### Expected Behavior
Harness research finds conflicting evidence, challenge stage actively tests assumptions, output presents both sides with certainty grading.

### Validation Criteria
- [ ] **Conflict Detected**: Research stage identifies conflicting sources
- [ ] **Challenge Stage**: Challenge stage explicitly tests assumptions about remote work effectiveness
- [ ] **Both Sides Presented**: Output acknowledges both pro-remote and pro-office evidence
- [ ] **Certainty Graded**: Overall certainty reduced from High to Medium or Low
- [ ] **Limitation Stated**: Clear statement about evidence conflict

### Expected Output Structure
```json
{
  "challenge_stage": {
    "assumptions_tested": ["Remote work is universally beneficial", "Office work is obsolete"],
    "disconfirming_evidence": ["Study X shows collaboration decline in fully remote teams", "Study Y shows productivity gains in office settings for creative work"],
    "alternative_interpretations": ["Effectiveness may depend on role type", "Hybrid may outperform both extremes"],
    "overall_certainty": "Medium — evidence mixed; recommendation is conditional on role type"
  },
  "limitations": {
    "evidence_conflict": "Strong evidence on both sides; no consensus in literature",
    "recommendation_condition": "Episode should present balanced view, not one-sided conclusion"
  }
}
```

### Edge Cases Tested
- Conflicting evidence handling
- Challenge stage thoroughness
- Certainty grading
- Balanced presentation

---

## Regression Test Framework

### Adding Real User Runs
When real users run the harness, add their cases here:

```markdown
### Regression Case #[N]: [Brief Description]
**Date:** YYYY-MM-DD
**User Input:** "[Actual user input]"
**Actual Output:** [Key findings from output]
**Status:** Pass/Fail
**Notes:** [Any issues or learnings]
```

### Regression Checklist
For each regression case, verify:
- [ ] Output quality equals or exceeds initial run
- [ ] No regressions in scoring accuracy
- [ ] Framework selection remains consistent for similar inputs
- [ ] Roadmap recommendations remain actionable

---

## Automated Testing (Future Enhancement)

Potential automation paths:
1. **Mock WebSearch responses** for consistent research testing
2. **Assertion-based validation** of output structure
3. **Score calculation verification** via automated checks
4. **Quality gate automated enforcement**

Current state: Manual validation per scenario above is required.

---

## Test Execution Log

Keep a log of test runs:

| Date | Scenario | Result | Notes |
|:---|:---|:---:|:---|
| 2026-07-01 | Scenario 1 | [ ] | Initial test run |
| 2026-07-01 | Scenario 2 | [ ] | |
| 2026-07-01 | Scenario 3 | [ ] | |
| 2026-07-01 | Scenario 4 | [ ] | |
| 2026-07-01 | Scenario 5 | [ ] | |
| 2026-07-01 | Scenario 6 | [ ] | |
| 2026-07-01 | Scenario 7 | [ ] | |

---

## Continuous Validation

After any code changes to:
- Sub-skills (sub-*.md)
- Main harness (main.md)
- Knowledge base (SECOND-KNOWLEDGE-BRAIN.md)
- Knowledge updater (knowledge_updater.py)

Re-run all 7 scenarios to ensure no regressions. Any failure requires diagnosis and fix before considering changes complete.
