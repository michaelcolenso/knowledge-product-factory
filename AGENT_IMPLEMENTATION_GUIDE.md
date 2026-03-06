# Agentic KPF Implementation Guide
## For AI Agents Executing This System

---

## Table of Contents

1. [System Overview](#system-overview)
2. [Prerequisites](#prerequisites)
3. [Configuration](#configuration)
4. [Implementation](#implementation)
5. [Execution Workflow](#execution-workflow)
6. [Phase-by-Phase Instructions](#phase-by-phase-instructions)
7. [Gate Decision Framework](#gate-decision-framework)
8. [Error Handling](#error-handling)
9. [Best Practices](#best-practices)
10. [Examples](#examples)
11. [Troubleshooting](#troubleshooting)

---

## System Overview

### What Is Agentic KPF?

Agentic KPF is a **workflow system executed by AI agents** (like you) to research, validate, and create knowledge products. Unlike traditional software that calls APIs, you use your tools (web search, browsing, reasoning, writing) to execute each phase.

### Core Philosophy

1. **Real Evidence**: Search for actual data, not generate synthetic content
2. **Gate-Driven**: Stop at validation checkpoints if criteria aren't met
3. **Transparent**: Every decision explained with sources
4. **Honest**: Don't inflate scores or findings
5. **Complete**: Save all artifacts to disk

### The 16 Phases

```
INTAKE → DISCOVERY → SPENDING → PAIN → COMPETITORS → SCORING →
STRATEGY → OUTLINE → SYNTHESIS → DRAFTING → ARTIFACTS →
PERSONALIZATION → PACKAGING → LAUNCH → VALIDATION → RETROSPECTIVE
```

### Execution Modes

- **DISCOVER**: Phases 1-2 only (find niches)
- **VALIDATE**: Phases 1-6 (research and score)
- **BUILD**: Phases 1-13 (create product)
- **LAUNCH**: Phases 1-15 (include marketing)
- **FULL**: All 16 phases (complete end-to-end)

---

## Prerequisites

### Required Tools

You MUST have access to:
- ✅ **Web Search** - Primary research tool
- ✅ **Browser Visit** - Deep dives on competitor sites
- ✅ **File Write** - Save artifacts to disk
- ✅ **Reasoning/Analysis** - Score opportunities, make decisions

### Optional Tools

- 📎 **Image Generation** - For product mockups (not required)
- 📎 **Code Execution** - For data analysis (not required)

### Required Knowledge

You should understand:
- Pydantic schemas (for artifact structure)
- JSON format (for artifacts)
- Markdown (for content)
- Basic business concepts (pricing, positioning, etc.)

---

## Configuration

### 1. Set Up Directory Structure

Before your first run, create this structure:

```
/mnt/okcomputer/output/kpf/
├── runs/                          # All run outputs go here
│   └── YYYY-MM-DD_[niche-slug]/  # Individual run directories
├── memory/                        # Persistent learning
│   ├── winning_niches.json
│   ├── failed_niches.json
│   ├── search_patterns.json
│   └── format_performance.json
└── templates/                     # Reusable templates (optional)
```

### 2. Create Memory Files

Initialize these files (they'll be updated after each run):

**winning_niches.json**:
```json
{
  "niches": [],
  "metadata": {
    "version": "1.0.0",
    "last_updated": null,
    "description": "Record of niches that passed validation"
  }
}
```

**failed_niches.json**:
```json
{
  "niches": [],
  "metadata": {
    "version": "1.0.0",
    "last_updated": null,
    "description": "Record of niches that failed validation"
  }
}
```

**search_patterns.json**:
```json
{
  "patterns": [],
  "metadata": {
    "version": "1.0.0",
    "last_updated": null
  }
}
```

**format_performance.json**:
```json
{
  "formats": {
    "playbook": {"uses": 0, "successes": 0, "avg_score": 0},
    "template_library": {"uses": 0, "successes": 0, "avg_score": 0},
    "notion_system": {"uses": 0, "successes": 0, "avg_score": 0},
    "sop": {"uses": 0, "successes": 0, "avg_score": 0},
    "checklist_pack": {"uses": 0, "successes": 0, "avg_score": 0},
    "decision_framework": {"uses": 0, "successes": 0, "avg_score": 0},
    "research_brief": {"uses": 0, "successes": 0, "avg_score": 0}
  }
}
```

### 3. Set Default Constraints

Create a constraints file:

```json
{
  "max_creation_weeks": 3,
  "allowed_formats": ["playbook", "template_library", "notion_system", "checklist_pack"],
  "price_floor": 79,
  "price_ceiling": 199
}
```

---

## Implementation

### Artifact Schema Definitions

Every artifact must follow these exact schemas:

#### run_config.json
```json
{
  "run_id": "string (YYYY-MM-DD_niche-slug)",
  "mode": "discover | validate | build | launch | full",
  "niche": "string (the topic)",
  "target_audience": "string (specific segment)",
  "constraints": {
    "max_creation_weeks": 3,
    "allowed_formats": ["array of strings"],
    "price_floor": 79,
    "price_ceiling": 199
  },
  "strict_mode": true,
  "with_personalization": false
}
```

#### spending_signals.json
```json
{
  "niche": "string",
  "signals": [
    {
      "community": "string (where found)",
      "quote": "string (exact quote)",
      "purchase_type": "service | course | tool | time_investment | revenue_share | lost_revenue",
      "amount_usd": number or null,
      "time_cost": "string or null",
      "job_to_be_done": "string",
      "satisfaction": "happy | neutral | frustrated",
      "date": "YYYY-MM-DD",
      "source": "string",
      "url": "string"
    }
  ],
  "signal_count": number,
  "passes_threshold": boolean,
  "quantified_count": number,
  "price_range": "string"
}
```

#### pain_map.json
```json
{
  "niche": "string",
  "core_question": "string (the recurring question)",
  "patterns": [
    {
      "type": "information_gap | frustration | time_loss | money_risk | competitor_failure",
      "quote": "string",
      "source": "string",
      "url": "string",
      "frequency_estimate": number (1-100)
    }
  ],
  "current_workarounds": ["array of strings"],
  "time_wasted": "string",
  "money_risked": "string",
  "emotional_state": "string",
  "ideal_solution_language": "string"
}
```

#### opportunity_score.json
```json
{
  "scores": {
    "spending_clarity": 1-5,
    "information_gap": 1-5,
    "urgency": 1-5,
    "create_feasibility": 1-5,
    "ai_multiplier": 1-5
  },
  "total": number (5-25),
  "decision": "CREATE | PIVOT | REJECT",
  "confidence": "low | medium | high",
  "justification": {
    "spending_clarity": "string",
    "information_gap": "string",
    "urgency": "string",
    "create_feasibility": "string",
    "ai_multiplier": "string"
  }
}
```

#### product_brief.json
```json
{
  "opportunity_name": "string",
  "target_user": "string",
  "format": "string",
  "core_promise": "string",
  "price": number,
  "price_justification": "string",
  "ai_leverage": "string",
  "differentiator": "string",
  "deliverables": ["array of strings"],
  "distribution_channels": ["array of strings"]
}
```

#### validation_report.json
```json
{
  "status": "PASS | REVISE | FAIL",
  "checks": {
    "spending_evidence": boolean,
    "pain_specificity": boolean,
    "score_threshold": boolean,
    "artifact_completeness": boolean,
    "launch_readiness": boolean
  },
  "gate_verification": {
    "gate_1_spending": {"passed": boolean, "evidence": "string"},
    "gate_2_pain": {"passed": boolean, "evidence": "string"},
    "gate_3_score": {"passed": boolean, "evidence": "string"},
    "gate_4_artifacts": {"passed": boolean, "evidence": "string"},
    "gate_5_launch": {"passed": boolean, "evidence": "string"}
  },
  "issues": ["array of strings"],
  "required_revisions": ["array of strings"],
  "overall_assessment": "string",
  "recommendation": "string"
}
```

---

## Execution Workflow

### Starting a Run

When user says: `"[mode] [niche]"`

Example: `"Full run: productivity system for developers"`

1. **Parse the request**:
   - Mode: full
   - Niche: "productivity system for developers"

2. **Create run directory**:
   ```
   /mnt/okcomputer/output/kpf/runs/YYYY-MM-DD_[niche-slug]/
   ```

3. **Start Phase 1 (Intake)**

### State Tracking

Maintain this in your context throughout the run:

```yaml
Current Run:
  run_id: "YYYY-MM-DD_niche-slug"
  mode: "full"
  niche: "the niche"
  current_phase: "intake"
  
Artifacts Created:
  - run_config
  - discovery_report
  - [etc]
  
Gates Passed:
  - gate_1: true/false
  - gate_2: true/false
  - [etc]
  
Current Score: XX
Decision: CREATE/PIVOT/REJECT
```

### Phase Execution Pattern

For EACH phase, follow this exact pattern:

```
---
## PHASE X: [PHASE NAME]

**Objective**: [What to accomplish]

**Process**:
[Step-by-step actions]

**Tools**: [Which tools to use]

**Output**: [What to produce]

[EXECUTE PHASE]

[SAVE ARTIFACT]

[REPORT COMPLETION]
```

---

## Phase-by-Phase Instructions

### PHASE 1: INTAKE

**Objective**: Validate niche and set up run

**Process**:
1. Validate niche specificity (at least 2-3 words, clear topic)
2. Set constraints (max weeks, price range, formats)
3. Generate run_id: `YYYY-MM-DD_[slugified-niche]`
4. Create run directory
5. Save run_config.json

**Tools**: None (internal reasoning)

**Validation Rules**:
- Reject niches < 5 characters
- Warn if < 2 words
- Accept if 2+ words, clear topic

**Output**: run_config.json

**Example**:
```
Niche: "productivity system for developers"
Validation: ✓ Specific (topic + audience)
Run ID: 2026-03-06_productivity-system-developers
```

---

### PHASE 2: DISCOVERY

**Objective**: Find communities, spending signals, pain points

**Process**:
1. Search for communities (Reddit, forums, Facebook groups)
2. Search for spending signals ("paid", "cost", "$", "spent")
3. Search for pain points ("frustrated", "struggling", "help")
4. Document findings with URLs

**Search Queries to Run** (adjust for niche):
```
"[niche] reddit"
"[niche] forum"
"[niche] paid $"
"[niche] cost"
"[niche] spent"
"[niche] frustrated"
"[niche] struggling"
"[niche] help"
"best [niche]"
"[niche] worth it"
```

**Tools**: Web Search (primary), Browser Visit (if needed)

**Output**: discovery_report.json

**Quality Standards**:
- Minimum 3 communities found
- Minimum 3 spending signals
- Minimum 3 pain patterns
- All findings must have source URLs

---

### PHASE 3: SPENDING ANALYSIS

**Objective**: Extract and quantify spending signals

**Process**:
1. Review discovery findings
2. Extract concrete spending examples
3. Categorize by type (service, course, tool, time, etc.)
4. Note satisfaction level
5. Identify jobs-to-be-done

**Gate 1 - Spending Evidence**:
- PASS: 3+ signals AND 2+ quantified (with $ or time)
- FAIL: < 3 signals OR < 2 quantified

**If FAIL**: Stop and report to user

**Tools**: None (analysis only)

**Output**: spending_signals.json

---

### PHASE 4: PAIN MAPPING

**Objective**: Map pain points and consequences

**Process**:
1. Identify core recurring question
2. Document current workarounds
3. Quantify time wasted
4. Quantify money risked
5. Capture emotional state
6. Note ideal solution language

**Gate 2 - Pain Specificity**:
- PASS: Core question + workarounds + quantified costs
- FAIL: Any missing element

**If FAIL**: Stop and report to user

**Tools**: None (analysis only)

**Output**: pain_map.json

---

### PHASE 5: COMPETITIVE ANALYSIS

**Objective**: Map competitive landscape

**Process**:
1. Search for existing solutions
2. Identify competitors by category (free, course, service, software)
3. Note pricing
4. Identify weaknesses
5. Find market gap

**Search Queries**:
```
"[niche] course"
"[niche] template"
"[niche] service"
"[niche] tool"
"best [niche] 2025"
"[niche] vs"
```

**Tools**: Web Search, Browser Visit (for pricing pages)

**Output**: competitor_map.json

---

### PHASE 6: OPPORTUNITY SCORING

**Objective**: Score and decide CREATE/PIVOT/REJECT

**Scoring Rubric** (1-5 each):

1. **Spending Clarity**
   - 5: Multiple $500+ purchases documented
   - 4: Some $200-500 purchases
   - 3: $50-200 purchases
   - 2: Some spending but unclear amounts
   - 1: No spending evidence

2. **Information Gap**
   - 5: Recurring confusion, no good solutions
   - 4: Clear questions, partial solutions
   - 3: Some questions, okay solutions
   - 2: Most info available
   - 1: Info readily available, well-solved

3. **Urgency**
   - 5: Revenue-impacting, time-sensitive
   - 4: Important business impact
   - 3: Moderate impact
   - 2: Nice-to-have
   - 1: Low priority

4. **Create Feasibility**
   - 5: Clear scope, highly templatable
   - 4: Well-defined, some complexity
   - 3: Moderate complexity
   - 2: Complex, hard to scope
   - 1: Too vague or complex

5. **AI Multiplier**
   - 5: Strong personalization/generation opportunity
   - 4: Good AI enhancement possible
   - 3: Some AI leverage
   - 2: Minimal AI value
   - 1: No AI leverage

**Calculate**: Sum all scores (max 25)

**Decision**:
- CREATE: Score >= 18
- PIVOT: Score 14-17
- REJECT: Score < 14

**Gate 3 - Score Threshold**:
- PASS: Total >= 18 AND decision = CREATE
- FAIL: Score < 18 OR decision = REJECT

**If FAIL**: Stop and report to user

**Tools**: None (reasoning only)

**Output**: opportunity_score.json

---

### PHASE 7: STRATEGY

**Objective**: Define product strategy

**Process**:
1. Define target user (specific segment)
2. Choose product format (playbook, templates, etc.)
3. Craft core promise (transformation statement)
4. Set pricing (based on spending signals, competitors)
5. Define differentiator
6. Document AI leverage
7. List deliverables
8. Choose distribution channels

**Pricing Guidelines**:
- Must be between price_floor and price_ceiling (default $79-199)
- Base on spending signals found
- Position below services, above DIY opportunity cost

**Tools**: None (strategic reasoning)

**Output**: product_brief.json

---

### PHASE 8: OUTLINE

**Objective**: Create content structure

**Process**:
1. Create section-level structure
2. Map key deliverables per section
3. Ensure scope fits constraints (2-4 weeks)
4. Identify artifact references

**Tools**: None (planning)

**Output**: outline.json

---

### PHASE 9: SYNTHESIS

**Objective**: Organize knowledge

**Process**:
1. Transform research into structured facts
2. Note contradictions
3. Mark confidence levels
4. Document key decisions
5. List pitfalls

**Tools**: None (synthesis)

**Output**: knowledge_base.json

---

### PHASE 10: DRAFTING

**Objective**: Write main product content

**Process**:
1. Write following outline
2. Include examples
3. Step-by-step instructions
4. Action items
5. No filler, maintain useful density

**Length Guidelines**:
- Playbook: 50-100 pages
- SOP: 20-40 pages
- Research brief: 15-30 pages

**Tools**: None (writing)

**Output**: draft_product.md

---

### PHASE 11: ARTIFACTS

**Objective**: Create support materials

**Process**:
1. Create minimum 3 support artifacts:
   - Checklists (process tracking)
   - Templates (fill-in-blank)
   - Scripts (email/copy)
   - Calculators (decision tools)
   - Worksheets (exercises)

2. Create artifact_manifest.json

**Tools**: None (creation)

**Output**: 
- artifact_manifest.json
- Individual artifact files

---

### PHASE 12: PERSONALIZATION (Optional)

**Objective**: Define personalization if applicable

**Skip if**: Format doesn't benefit from personalization

**Process**:
1. Define input fields
2. Design generation logic
3. Specify outputs
4. Document update strategy

**Tools**: None (specification)

**Output**: personalization_spec.json

---

### PHASE 13: PACKAGING

**Objective**: Define buyer-facing package

**Process**:
1. Define product name, version, tier
2. List included files
3. Add delivery notes
4. Define bonuses

**Gate 4 - Artifact Completeness**:
- PASS: draft_product.md exists AND 3+ artifacts AND package_manifest.json
- FAIL: Missing any component

**If FAIL**: Go back and create missing pieces

**Tools**: None (organization)

**Output**: package_manifest.json

---

### PHASE 14: LAUNCH ASSETS

**Objective**: Create marketing materials

**Required Assets**:
1. **Sales Page** - Full landing page copy
2. **Launch Posts** (3-5) - Social media content
3. **Email Sequence** (3-5 emails) - Welcome series
4. **FAQ** - 10-15 common questions
5. **Objection Handling** - Responses to common objections

**Tools**: None (copywriting)

**Output**: launch_assets/ directory

---

### PHASE 15: VALIDATION

**Objective**: Final quality check

**Check All Gates**:
1. Spending evidence: 3+ signals, 2+ quantified?
2. Pain specific: Question + workaround + cost?
3. Score >= 18 and CREATE?
4. Artifacts complete: Draft + 3+ artifacts + manifest?
5. Launch ready: Audience + channels + pricing?

**Gate 5 - Launch Readiness**:
- PASS: All checks pass
- REVISE: Minor issues but fixable
- FAIL: Major problems

**Tools**: None (review)

**Output**: validation_report.json

---

### PHASE 16: RETROSPECTIVE

**Objective**: Document learnings

**Process**:
1. Document what worked
2. Document what didn't work
3. List surprises
4. Capture lessons learned
5. Update memory files

**Memory Updates Required**:
- winning_niches.json (if passed)
- failed_niches.json (if failed)
- search_patterns.json (save successful queries)
- format_performance.json (track format success)

**Tools**: File write

**Output**: postmortem.json

---

## Gate Decision Framework

### Gate Decision Format

Always state gates explicitly:

```
=== GATE X: [NAME] ===
Criteria: [What must be true]
Evidence: [What you found]
Decision: [PASS / FAIL / REVISE]
Reasoning: [Why]
Next Action: [Proceed / Stop / Go back]
```

### When to STOP

STOP the pipeline and report to user if:
- Any gate FAILS with no path to recovery
- Score < 14 (REJECT decision)
- User explicitly asks to stop
- Evidence is clearly insufficient after multiple searches

### When to PROCEED

PROCEED if:
- Gate PASSES
- Gate is REVISE but issues are minor and fixable

### When to OVERRIDE

You may OVERRIDE a failing gate ONLY if:
- Strong qualitative evidence despite low quantitative
- Unique insight not captured by scoring
- User provides additional context

**Must document WHY you overrode**

---

## Error Handling

### Common Issues and Solutions

**Issue: No search results**
- Try different query variations
- Use broader terms
- Search for related topics
- Try "how to [niche]" or "[niche] guide"

**Issue: Weak spending signals**
- Search for time costs ("spent 10 hours")
- Search for hiring patterns ("hired someone to")
- Search for tool purchases ("bought software")
- Look for opportunity costs

**Issue: Vague pain points**
- Search "how do I [niche]"
- Search "struggling with [niche]"
- Search "frustrated [niche]"
- Look for forum question threads

**Issue: Too much competition**
- Look for underserved sub-niches
- Check for recent complaints about existing solutions
- Identify format gaps
- Consider B2B vs B2C angle

**Issue: Can't decide on score**
- Default to conservative scoring
- Consider confidence level
- If borderline (17-18), lean toward CREATE if other factors strong

---

## Best Practices

### Research Best Practices

1. **Always cite sources** - Every finding needs a URL
2. **Quote exact language** - Use their words, not yours
3. **Search multiple angles** - Don't rely on single query
4. **Check dates** - Prefer recent information
5. **Look for patterns** - Single data point ≠ trend

### Writing Best Practices

1. **Use their language** - From pain research
2. **Be specific** - Numbers, examples, steps
3. **No filler** - Every sentence should add value
4. **Action-oriented** - Clear next steps
5. **Scannable** - Headers, bullets, short paragraphs

### Decision Best Practices

1. **Be honest** - Don't inflate scores
2. **Document reasoning** - Explain why you decided
3. **Err conservative** - Better to catch weak product early
4. **Consider user context** - They may have insights you don't
5. **When in doubt, search more** - Don't guess

### File Best Practices

1. **Save after EVERY phase** - Don't batch saves
2. **Use exact filenames** - Consistency matters
3. **Pretty-print JSON** - Human-readable
4. **Include metadata** - Dates, sources, confidence
5. **Create RUN_SUMMARY.md** - Final overview

---

## Examples

### Example 1: Validate Mode

**User**: "Validate productivity system for developers"

**Your Response**:
```
I'll execute Agentic KPF in VALIDATE mode for "productivity system for developers".

---
PHASE 1: INTAKE
✓ Niche validated
✓ Run directory created: runs/2026-03-06_productivity-system-developers/

---
PHASE 2: DISCOVERY
[Execute searches...]
✓ Communities: r/productivity (2M), r/webdev (1M), Hacker News
✓ Spending signals: 4 found
✓ Pain patterns: 5 found

---
PHASE 3: SPENDING ANALYSIS
=== GATE 1: SPENDING EVIDENCE ===
Signals: 4
Quantified: 3
Decision: PASS

[Continue through Phase 6...]

---
VALIDATION COMPLETE

Score: 20/25
Decision: CREATE

Recommendation: Proceed to BUILD
```

### Example 2: Full Run

**User**: "Full run: notion templates for therapists"

**Your Response**:
```
Executing Agentic KPF FULL mode for "notion templates for therapists".

[Execute all 16 phases...]

---
RUN COMPLETE

All 16 phases executed
All 5 gates passed
24 artifacts created
Opportunity Score: 22/25

Product: Notion Template System for Therapists
Price: $97
Status: Ready for launch
```

---

## Troubleshooting

### Pipeline Stuck?

If you can't find evidence:
1. Try 3+ different search queries
2. Broaden the niche slightly
3. Check related topics
4. If still nothing, report: "Insufficient evidence found"

### Unclear How to Score?

When scoring is ambiguous:
1. Review the rubric
2. Compare to previous runs
3. Default to lower score
4. Document uncertainty

### User Wants to Override?

If user says "I know this niche, trust me":
1. Acknowledge their expertise
2. Still execute minimum research
3. Document their input
4. Adjust scoring if justified
5. Explain your final decision

### Run Failed a Gate?

When reporting failure:
1. State which gate failed
2. Explain why
3. Provide evidence
4. Suggest alternatives
5. Offer to try different niche

---

## Quick Reference

### Command Patterns

| User Says | Mode | Stop After |
|-----------|------|------------|
| "Discover niches" | discover | Phase 2 |
| "Validate [niche]" | validate | Phase 6 |
| "Build [niche]" | build | Phase 13 |
| "Launch [niche]" | launch | Phase 15 |
| "Full run [niche]" | full | Phase 16 |

### Gate Summary

| Gate | Criteria | Fail Action |
|------|----------|-------------|
| 1 - Spending | 3+ signals, 2+ quantified | Stop, report |
| 2 - Pain | Question + workaround + cost | Stop, report |
| 3 - Score | >= 18, CREATE | Stop, report |
| 4 - Artifacts | Draft + 3+ artifacts + manifest | Go back |
| 5 - Launch | Audience + channels + pricing | Revise |

### Scoring Thresholds

| Total | Decision |
|-------|----------|
| >= 18 | CREATE |
| 14-17 | PIVOT |
| < 14 | REJECT |

---

## Final Notes

### What Success Looks Like

A successful run:
- ✅ All phases documented
- ✅ Gates explicitly decided with reasoning
- ✅ All artifacts saved to disk
- ✅ Evidence cited with URLs
- ✅ Clear recommendation
- ✅ Memory files updated

### What Failure Looks Like

A failed run (still valuable!):
- ✅ Research conducted
- ✅ Gate failed with clear reason
- ✅ User informed why
- ✅ Alternative suggestions provided
- ✅ Memory files updated (failed_niches.json)

### Remember

- **Evidence > Opinion**: Always search first
- **Gates Matter**: Don't skip validation
- **Be Honest**: Don't inflate scores
- **Save Everything**: Artifacts are the output
- **Learn**: Update memory after each run

---

## Ready to Execute

When user gives you a command:

1. Parse mode and niche
2. Create run directory
3. Execute phases sequentially
4. Make gate decisions explicitly
5. Save artifacts after each phase
6. Report results clearly

**Start with Phase 1. Work through to completion.**

Good luck!
