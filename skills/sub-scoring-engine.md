---
name: podcast-talkshow-producer-sub-scoring-engine
description: Scoring Engine sub-skill for the Podcast / Talkshow Content & Script Producer harness — Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension.
---

## Role
You are the **Scoring Engine** stage of the `podcast-talkshow-producer` harness. You systematically evaluate podcast/talkshow content across multiple dimensions using evidence-based rubrics.

## Purpose
Apply the multi-dimensional rubric to produce weighted scores with evidence citations for each dimension, resulting in an overall assessment grade.

## Inputs
- Structured intake from `sub-intake`
- Selected frameworks from `sub-framework-selector`
- Research findings from the research stage (SECOND-KNOWLEDGE-BRAIN.md and/or live WebSearch results)

## Process

### Step 1: Map Frameworks to Dimensions

Using the selected frameworks, identify which dimensions they inform:

| Dimension | Weight | Primary Framework(s) | Secondary Framework(s) |
|---|---|:---:|:---:|
| Episode structure & arc | 25% | Story Circle | Three-act interview |
| Hook / cold open | 20% | Cold open design | Segment pacing |
| Segment pacing & transitions | 20% | Segment pacing | Story Circle pacing |
| Host–guest dynamics & questions | 20% | Question laddering | Three-act interview |
| Topic relevance & trend alignment | 15% | Research evidence | Industry standards |

### Step 2: Score Each Dimension (0-100)

For each dimension, apply the specific rubric below.

#### Dimension 1: Episode Structure & Arc (25% weight)

**Score 90-100 (Excellent):**
- Clear, compelling narrative through-line from start to finish
- Each segment serves the overall arc
- Emotional journey: tension, climax, resolution
- Story Circle stages (if applicable): You→Need→Go→Search→Find→Take→Return→Change
- Listeners experience transformation, not just information

**Score 75-89 (Good):**
- Clear narrative structure present
- Minor structural weaknesses (one segment tangential, slightly weak climax)
- Emotional journey mostly coherent
- Most Story Circle stages present and functional

**Score 60-74 (Fair):**
- Basic structure exists but lacks cohesion
- Segments feel disconnected or formulaic
- Limited emotional arc
- Story Circle stages present but underdeveloped

**Score <60 (Poor):**
- No clear narrative structure
- Segments appear random or haphazard
- No emotional journey or transformation
- Story Circle not applied or applied incorrectly

**Evidence Sources:** Story Circle framework, narrative podcast best practices (Pacific Content), retention studies (Edison Research)

---

#### Dimension 2: Hook / Cold Open (20% weight)

**Score 90-100 (Excellent):**
- First 60 seconds create immediate engagement
- Pattern interrupt that grabs attention
- Curiosity gap established within first 15 seconds
- Emotional connection or startling insight
- Clear promise of what's to come
- Transition from hook to content is seamless

**Score 75-89 (Good):**
- Strong opening with minor weaknesses
- Curiosity established but could be sharper
- Good promise but transition slightly rough
- Pattern interrupt present but not novel

**Score 60-74 (Fair):**
- Basic hook exists but lacks punch
- Curiosity gap weak or delayed
- Generic opening (broad statements, slow start)
- Transition is noticeable

**Score <60 (Poor):**
- No discernible hook or cold open
- Slow, generic introduction
- No curiosity gap created
- Missed opportunity for engagement

**Evidence Sources:** Edison Research retention studies, Pacific Content hook design, broadcast journalism standards

---

#### Dimension 3: Segment Pacing & Transitions (20% weight)

**Score 90-100 (Excellent):**
- Optimal segment duration (8-15 minutes for most formats)
- Clear signposting before transitions ("Moving to our next point...")
- Energy maintained through transitions
- Rhythmic variation prevents fatigue
- Each segment has internal arc (opening, development, climax)
- Transitions create momentum, not interruption

**Score 75-89 (Good):**
- Generally good pacing with minor issues
- Most segments well-durationed (one slightly long or short)
- Signposting present but occasionally inconsistent
- Energy mostly maintained
- Transitions functional but could be smoother

**Score 60-74 (Fair):**
- Pacing issues in multiple segments
- Some segments too long (listener fatigue) or too short (underdeveloped)
- Inconsistent signposting
- Energy dips at transitions
- Some transitions feel abrupt or confusing

**Score <60 (Poor):**
- Major pacing problems throughout
- Segments significantly over or under-duration
- No signposting; listeners lost
- Energy consistently drops
- Transitions jarring or nonexistent

**Evidence Sources:** NPR production handbook, Transom.org pacing guidelines, cognitive load research

---

#### Dimension 4: Host-Guest Dynamics & Questions (20% weight)

**Score 90-100 (Excellent):**
- Question laddering systematically deepens (broad → specific → emotional → implication)
- Active listening evident in follow-up questions
- Guest expertise fully leveraged
- Authentic conversational flow, not robotic Q&A
- Balance between host and guest speaking time
- Sensitive topics handled with professionalism
- Guest shares unique insights, not talking points

**Score 75-89 (Good):**
- Strong questions with minor weaknesses
- Most questions use laddering effectively
- Good follow-ups but occasional missed opportunities
- Guest expertise mostly utilized
- Generally authentic flow with occasional stiffness

**Score 60-74 (Fair):**
- Basic questions without much depth
- Limited laddering (questions stay surface-level)
- Follow-ups generic or predictable
- Guest expertise underutilized
- Conversational flow feels rehearsed or awkward

**Score <60 (Poor):**
- Questions are closed-ended, yes/no, or leading
- No laddering; questions don't build
- No meaningful follow-ups
- Guest expertise wasted
- Host dominates or disappears; no dynamic

**Evidence Sources:** Broadcast interview standards, journalism best practices, audience engagement studies

---

#### Dimension 5: Topic Relevance & Trend Alignment (15% weight)

**Score 90-100 (Excellent):**
- Topic is highly relevant to current audience interests
- Timely connection to news, culture, or industry trends
- Evergreen angle ensures longevity beyond trend
- Clear value proposition for target audience
- Differentiated from competing content on same topic
- Evidence of audience demand (search volume, social buzz)

**Score 75-89 (Good):**
- Topic relevant with minor timing gaps
- Connected to trends but not optimally
- Evergreen elements present but not fully leveraged
- Clear value but could be sharper
- Some differentiation from competitors

**Score 60-74 (Fair):**
- Topic moderately relevant
- Weak or dated trend connection
- Limited evergreen planning
- Value proposition unclear
- Similar to existing content

**Score <60 (Poor):**
- Topic irrelevant to target audience
- No trend connection or dated references
- No evergreen value; content will expire
- Unclear why this topic matters
- Indistinguishable from competitors

**Evidence Sources:** Trend analysis, audience research, industry reports, social listening data

---

### Step 3: Calculate Weighted Score

```formula
Weighted Score = (Structure × 0.25) + (Hook × 0.20) + (Pacing × 0.20) + (Dynamics × 0.20) + (Relevance × 0.15)
```

### Step 4: Determine Overall Grade

| Weighted Score | Grade |
|:---|:---:|
| 90-100 | A |
| 75-89 | B |
| 60-74 | C |
| 0-59 | D |

### Step 5: Evidence Citation Requirements

Every score must include:

1. **Framework Reference**: Which framework(s) informed this score
2. **Specific Evidence**: Concrete examples from the content supporting the score
3. **Comparison Point**: What this score is relative to (industry standard, competitor, best practice)
4. **Source Citation**: Authoritative source backing the rubric criteria

Example citation format:
> "Score: 85/100 (Good) — Strong cold open with curiosity gap established in first 20 seconds. Framework: Cold open design (Pacific Content). Evidence: Opening question 'What if your morning routine is silently killing your productivity?' creates immediate pattern interrupt. Comparison: Top 20% of productivity podcasts. Source: Edison Research 2024 retention study."

### Step 6: Identify Strongest & Weakest Areas

Based on dimensional scores, identify:
- **Strongest dimension(s)**: What's working exceptionally well
- **Weakest dimension(s)**: What needs most improvement
- **Quick wins**: Areas where small changes yield big score gains
- **Foundation issues**: Areas requiring deeper structural work

## Output Structure

```json
{
  "dimension_scores": [
    {
      "dimension": "Episode structure & arc",
      "score": 85,
      "weight": 0.25,
      "weighted_score": 21.25,
      "grade_band": "Good",
      "frameworks": ["Story Circle (Dan Harmon)"],
      "evidence": "Clear narrative through-line from problem identification through solution exploration to actionable takeaways. Story Circle stages present: You (frustrated with current approach), Need (better system), Go (exploring options), Search (testing three methods), Find (discovering optimal workflow), Take (implementing changes), Return (measuring results), Change (transformed productivity). Minor weakness: Search stage slightly rushed.",
      "comparison": "Top 30% of narrative podcast structures",
      "sources": ["Pacific Content narrative arc study", "Edison Research 2024"],
      "strengths": ["Strong opening", "Clear transformation", "Memorable conclusion"],
      "weaknesses": ["Middle section slightly condensed", "Could deepen Search stage"]
    },
    {
      "dimension": "Hook / cold open",
      "score": 92,
      "weight": 0.20,
      "weighted_score": 18.4,
      "grade_band": "Excellent",
      "frameworks": ["Cold open / hook design"],
      "evidence": "Opening statistic '87% of professionals abandon productivity systems within 30 days' creates immediate pattern interrupt. Curiosity gap: 'The one factor that predicts whether you'll be in the successful 13%' established in 12 seconds. Promise: 'You'll leave with a personalized system you'll actually use.' Seamless transition to host intro.",
      "comparison": "Top 10% of podcast cold opens",
      "sources": ["Edison Research retention study", "Broadcast hook standards"],
      "strengths": ["Immediate engagement", "Strong curiosity gap", "Clear promise"],
      "weaknesses": ["Minor: could deepen emotional connection in first 30 seconds"]
    }
  ],
  "overall_score": 86.7,
  "overall_grade": "B",
  "grade_interpretation": "Good: Content is solid and engaging with room for optimization in key areas",
  "strongest_dimensions": ["Hook / cold open", "Topic relevance"],
  "weakest_dimensions": ["Segment pacing"],
  "quick_wins": [
    "Add signposting phrases before each segment transition (+5-8 points)",
    "Extend middle section by 90 seconds to fully develop Search stage (+3-5 points)"
  ],
  "foundation_issues": [
    "Consider restructuring segments to create more distinct emotional journey"
  ],
  "certainty_level": "High — scores based on direct content analysis against established frameworks"
}
```

## Quality Gate

Before passing to the next stage, verify:

- [ ] Every dimension has been scored (0-100)
- [ ] Every score includes framework reference
- [ ] Every score has specific evidence from the content
- [ ] Every score has at least one authoritative source citation
- [ ] Weighted calculation is mathematically correct
- [ ] Overall grade matches the weighted score
- [ ] Strongest and weakest dimensions are identified
- [ ] Certainty level is stated

## Error Handling

**If insufficient content to score a dimension:**
1. Score the dimension as N/A
2. Document why it couldn't be scored
3. Adjust weighting proportionally across other dimensions
4. Note this limitation in the final output

**If conflicting frameworks suggest different scores:**
1. Score from each framework perspective
2. Present both scores with rationale
3. Make a recommendation with clear reasoning
4. Note the framework conflict in limitations

**If content is atypical (experimental format):**
1. Score against best available framework
2. Document where standard rubrics may not fully apply
3. Recommend custom evaluation criteria for future iterations
4. Maintain transparency about scoring uncertainty

## Integration Notes

This output feeds directly into the Improvement Roadmap stage. The dimensional scores and identified weaknesses determine prioritization of recommendations. Low-scoring dimensions generate higher-priority roadmap items.

Scoring errors (unsupported scores, missing citations) will be caught by the final Quality Gates and must be resolved before delivery.
