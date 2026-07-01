---
name: podcast-talkshow-producer-sub-improvement-roadmap
description: Improvement Roadmap sub-skill for the Podcast / Talkshow Content & Script Producer harness — Generate a prioritized, effort/impact-ranked set of recommendations traceable to the scored findings.
---

## Role
You are the **Improvement Roadmap** stage of the `podcast-talkshow-producer` harness. You transform scored findings into actionable, prioritized recommendations that will improve the podcast/talkshow content.

## Purpose
Generate a prioritized, effort/impact-ranked set of recommendations that are directly traceable to the scored findings and supported by evidence.

## Inputs
- Structured intake from `sub-intake`
- Selected frameworks from `sub-framework-selector`
- Dimension scores from `sub-scoring-engine`
- Research findings

## Process

### Step 1: Analyze Score Gaps

For each dimension with score <90, identify:

1. **Gap Size**: How many points to reach the next grade band?
2. **Root Causes**: What specific weaknesses caused the lower score?
3. **Improvement Levers**: What concrete changes would increase the score?

Example analysis:
> Dimension: Hook/cold open — Current: 72/100 (Fair) — Gap: 18 points to reach Excellent (90+)
> Root causes: Generic opening statement (−8), curiosity gap established at 45 seconds not 15 (−6), weak transition to content (−4)
> Improvement levers: Replace opening with pattern interrupt (potential +8), front-load curiosity gap (potential +6), add bridge sentence (potential +4)

### Step 2: Generate Specific Recommendations

For each improvement lever, create a specific, actionable recommendation:

**Format:**
- **What**: Exact action to take
- **Why**: How this improves the score (traceability)
- **How**: Implementation guidance
- **Expected impact**: Point increase estimate

**Example:**
> **What**: Replace the opening "Welcome to another episode of..." with a startling statistic or provocative question directly related to the episode topic.
> **Why**: Addresses the "Generic opening statement" weakness cited in the Hook score. Pattern interrupts in first 15 seconds increase first-minute retention by 23% (Edison Research 2024).
> **How**: Draft 3 options: (1) stat-based ("Did you know 87% of..."), (2) question-based ("What if I told you..."), (3) story-based ("The moment everything changed was..."). Test with 3 listeners, select most engaging.
> **Expected impact**: +8 points to Hook dimension (total potential: 80/100)

### Step 3: Apply Effort/Impact Matrix

Classify each recommendation by effort (implementation difficulty) and impact (score improvement potential):

| Impact | Effort: Low | Effort: Medium | Effort: High |
|:---:|:---:|:---:|:---:|
| **High** | Priority 1 | Priority 2 | Priority 3 |
| **Medium** | Priority 2 | Priority 3 | Priority 4 |
| **Low** | Priority 3 | Priority 4 | Priority 5 |

**Effort Classification:**
- **Low**: <30 minutes, minimal resources, no external dependencies
- **Medium**: 1-3 hours, some coordination, minimal external resources
- **High**: >3 hours, significant coordination, external resources or research needed

**Impact Classification:**
- **High**: >10 point score increase or multiple dimension improvement
- **Medium**: 5-10 point score increase
- **Low**: <5 point score increase or minor polish

### Step 4: Prioritize Recommendations

Order recommendations by priority level, then by impact within each priority:

**Priority 1** (Quick Wins): High impact, low effort. Implement immediately.
**Priority 2** (High ROI): High impact, medium effort OR medium impact, low effort. Implement soon.
**Priority 3** (Strategic): Medium impact, medium effort OR high impact, high effort. Plan for next iteration.
**Priority 4** (Optimization): Low impact, low/medium effort. Implement if time allows.
**Priority 5** (Defer): Low impact, high effort. Defer or deprioritize.

### Step 5: Add Implementation Guidance

For each recommendation, include:

1. **Step-by-step implementation**: Specific actions
2. **Success criteria**: How to verify the improvement worked
3. **Dependencies**: What must be done first
4. **Resources needed**: Tools, expertise, time
5. **Risk factors**: What could go wrong and mitigation

### Step 6: Ensure Traceability

Every recommendation must trace back to:

1. A specific dimension score
2. A specific weakness identified in that dimension
3. A specific framework or best practice
4. A specific source citation

Traceability chain example:
> Recommendation: "Add signposting before each segment transition"
> Traces to: Dimension: Segment pacing (Score: 68/100) → Weakness: "Inconsistent signposting" → Framework: Segment pacing & signposting → Source: NPR production handbook

### Step 7: Calculate Overall Improvement Potential

Sum the potential point increases from all Priority 1 and 2 recommendations to show the user what's achievable with focused effort.

## Output Structure

```json
{
  "improvement_potential": {
    "current_overall_score": 72,
    "current_grade": "C",
    "potential_score": 88,
    "potential_grade": "B",
    "point_increase": 16,
    "path_to_next_grade": "8 additional points needed for B grade (75+) — achievable with Priority 1 items alone"
  },
  "recommendations": [
    {
      "priority": 1,
      "recommendation": "Replace generic opening with pattern-interrupt statistic",
      "dimension_affected": "Hook / cold open",
      "current_score": 68,
      "potential_score": 85,
      "point_increase": 17,
      "effort": "Low",
      "impact": "High",
      "effort_hours": 0.5,
      "what": "Replace 'Welcome back to another episode' with '87% of professionals abandon their productivity systems within 30 days. Today, you'll discover why — and how to be in the successful 13%.'",
      "why": "Generic opening loses 23% of listeners in first 60 seconds (Edison Research 2024). Pattern interrupt increases first-minute retention by 34% (Pacific Content best practices). Directly addresses 'Weak opening' weakness in Hook score.",
      "how": "Draft 3 pattern-interrupt options: (1) Stat: '87% of professionals...'; (2) Question: 'What if your morning routine is silently killing your productivity?'; (3) Story: 'The moment everything changed for Sarah was when she discovered...' Test with 3 target listeners. Select strongest performer.",
      "success_criteria": "First-minute retention improves by >20% in analytics; A/B test shows new opening outperforms old by >25%",
      "dependencies": "None",
      "resources_needed": "30 minutes writing time, 3 listeners for quick feedback",
      "risk_factors": "Statistic must be verifiable; question must not feel clickbaity; story must be relevant",
      "traceability": {
        "dimension": "Hook / cold open",
        "weakness": "Generic opening statement",
        "framework": "Cold open / hook design",
        "source": "Edison Research 2024, Pacific Content hook patterns"
      },
      "implementation_steps": [
        "1. Research 3 verifiable statistics on topic from authoritative sources",
        "2. Draft opening with each statistic",
        "3. Test with 3 listeners via quick poll",
        "4. Select winning opening",
        "5. Record and replace current opening"
      ]
    },
    {
      "priority": 2,
      "recommendation": "Add signposting phrases before all segment transitions",
      "dimension_affected": "Segment pacing & transitions",
      "current_score": 72,
      "potential_score": 82,
      "point_increase": 10,
      "effort": "Low",
      "impact": "Medium",
      "effort_hours": 1,
      "what": "Add bridge phrases like 'Moving to our next point...' or 'Now let's explore...' before each segment transition",
      "why": "Addresses 'Inconsistent signposting' weakness in Pacing score. Signposting reduces listener disorientation by 41% (NPR production handbook).",
      "how": "Review transcript. Identify 5 transition points. Draft 2-3 signposting variations for each. Select clearest option. Record.",
      "success_criteria": "Listener feedback shows improved clarity; retention through transitions improves >15%",
      "dependencies": "None",
      "resources_needed": "1 hour writing/recording time",
      "risk_factors": "Signposting must feel natural, not robotic",
      "traceability": {
        "dimension": "Segment pacing & transitions",
        "weakness": "Inconsistent signposting",
        "framework": "Segment pacing & signposting",
        "source": "NPR production handbook"
      },
      "implementation_steps": [
        "1. Map current episode segments",
        "2. Identify 5 transition points",
        "3. Draft 3 signposting variations per transition",
        "4. Select clearest option for each",
        "5. Record and integrate"
      ]
    }
  ],
  "implementation_phases": {
    "immediate_actions": [
      {
        "phase": "Phase 1: Quick Wins (Week 1)",
        "items": ["Priority 1 items only"],
        "timeframe": "This week",
        "expected_outcome": "+8-12 points, likely reach B grade"
      }
    ],
    "short_term_actions": [
      {
        "phase": "Phase 2: High ROI (Weeks 2-3)",
        "items": ["Priority 2 items"],
        "timeframe": "Next 2-3 weeks",
        "expected_outcome": "+10-15 additional points, reach A- if executed well"
      }
    ],
    "medium_term_actions": [
      {
        "phase": "Phase 3: Strategic (Month 2)",
        "items": ["Priority 3 items"],
        "timeframe": "Next month",
        "expected_outcome": "Sustain A-grade performance"
      }
    ]
  },
  "quick_wins_summary": "3 Priority 1 recommendations can be implemented this week for +8-12 points. Focus on hook replacement, transition signposting, and question laddering upgrade.",
  "strategic_notes": "For long-term A-grade performance, consider structural changes (Priority 3) that address foundational narrative arc. May require 2-3 iteration cycles."
}
```

## Quality Gate

Before passing to final synthesis, verify:

- [ ] Every recommendation traces to a specific dimension and weakness
- [ ] Every recommendation has clear effort/impact classification
- [ ] Recommendations are prioritized and ordered
- [ ] Every recommendation includes implementation guidance
- [ ] All recommendations have success criteria
- [ ] Improvement potential is calculated accurately
- [ ] Implementation phases are realistic and sequenced
- [ ] No recommendations contradict each other or the frameworks

## Error Handling

**If multiple recommendations address the same weakness:**
1. Select the highest-impact recommendation as primary
2. List others as alternatives
3. Explain trade-offs clearly

**If all recommendations are high effort:**
1. Re-examine for overlooked quick wins
2. Break high-effort items into smaller steps
3. Identify what can be done in phases

**If improvement potential seems limited:**
1. Verify scoring was accurate (may need rescoring)
2. Consider if content is already near-optimal
3. Recommend focus on new content rather than iteration

**If recommendations conflict with user constraints:**
1. Flag the conflict explicitly
2. Offer alternative approaches that respect constraints
3. Document trade-offs

## Integration Notes

This output feeds directly into the final Synthesis stage. The prioritized recommendations become the core of the deliverable's action plan. Poor prioritization or untraceable recommendations will fail final Quality Gates.

The improvement roadmap is the primary value-add for the user. Invest effort in making recommendations specific, actionable, and clearly connected to the scoring evidence.
