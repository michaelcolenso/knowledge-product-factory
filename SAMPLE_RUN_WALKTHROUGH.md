# Sample Run Walkthrough
## See Exactly How to Execute Agentic KPF

---

## Scenario

**User says:** `"Full run: notion templates for therapists"`

This walkthrough shows exactly what you should do, step by step.

---

## Your Response Structure

```
[ACKNOWLEDGE REQUEST]
[CREATE DIRECTORY]
[EXECUTE PHASES]
[REPORT RESULTS]
```

---

## Step-by-Step Execution

### Step 1: Acknowledge and Parse

```
I'll execute Agentic KPF in FULL mode for "notion templates for therapists".

Mode: full
Niche: notion templates for therapists
```

### Step 2: Create Directory

```python
# Execute this command
mkdir -p /mnt/okcomputer/output/kpf/runs/2026-03-06_notion-templates-therapists
```

### Step 3: Phase 1 - Intake

**Your output:**
```
---
## PHASE 1: INTAKE

**Objective**: Validate niche and set up run

**Niche**: "notion templates for therapists"

**Validation**: ✓ Specific (tool + audience)

**Constraints**:
- Max creation weeks: 3
- Price range: $79-199
- Allowed formats: playbook, template_library, notion_system, checklist_pack

**Run ID**: 2026-03-06_notion-templates-therapists

**Mode**: full

Saving run_config.json...
✓ Phase 1 complete
```

**Save file:**
```json
{
  "run_id": "2026-03-06_notion-templates-therapists",
  "mode": "full",
  "niche": "notion templates for therapists",
  "target_audience": "therapists who want to organize their practice with Notion",
  "constraints": {
    "max_creation_weeks": 3,
    "allowed_formats": ["playbook", "template_library", "notion_system", "checklist_pack"],
    "price_floor": 79,
    "price_ceiling": 199
  },
  "strict_mode": true,
  "with_personalization": true
}
```

### Step 4: Phase 2 - Discovery

**Execute searches:**
```
[Tool: web_search "notion templates therapists reddit"]
[Tool: web_search "therapist notion workspace"]
[Tool: web_search "private practice notion template"]
[Tool: web_search "therapist notion paid"]
[Tool: web_search "therapist practice management overwhelmed"]
```

**Your output:**
```
---
## PHASE 2: DISCOVERY

**Objective**: Find communities, spending signals, and pain points

Searching for communities...
✓ Found: r/notion (300k+), r/productivity (2M), r/psychotherapy (180k)

Searching for spending signals...
✓ Found: "$47 for therapist template pack" (Etsy)
✓ Found: "Spent $97 on practice management template"
✓ Found: "Notion is free but took 10 hours to set up"

Searching for pain points...
✓ Found: "Can't keep track of client notes and appointments"
✓ Found: "Documentation taking too much time"
✓ Found: "Need a system for my private practice"

Documenting findings...
✓ Phase 2 complete
```

**Save file:** discovery_report.json

### Step 5: Phase 3 - Spending Analysis

**Your output:**
```
---
## PHASE 3: SPENDING ANALYSIS

**Objective**: Quantify willingness to pay

Signals extracted:
1. $47 - Therapist template pack (Etsy)
2. $97 - Practice management template
3. 10 hours - DIY Notion setup time
4. $29/month - Practice management software alternative

Quantified: 4/4 with $ amounts or time costs

=== GATE 1: SPENDING EVIDENCE ===
Criteria: 3+ signals, 2+ quantified
Evidence: 4 signals found, 4 quantified
Decision: PASS
Reasoning: Clear willingness to pay $47-97 for templates
Next Action: Proceed to pain mapping

✓ Phase 3 complete
```

**Save file:** spending_signals.json

### Step 6: Phase 4 - Pain Mapping

**Your output:**
```
---
## PHASE 4: PAIN MAPPING

**Objective**: Map pain points and consequences

Core question: "How do I organize my therapy practice without spending hours on setup or paying monthly fees?"

Current workarounds:
1. Expensive practice management software ($29-99/month)
2. Spreadsheets (disorganized, limited)
3. Paper files (outdated, hard to search)
4. DIY Notion (10+ hours learning curve)

Time wasted: 10+ hours for DIY setup
Money risked: $348-1,188/year for practice management software
Emotional state: Overwhelmed, wants simple solution

=== GATE 2: PAIN SPECIFICITY ===
Criteria: Question + workaround + cost
Evidence: All three documented
Decision: PASS
Reasoning: Clear pain with quantified consequences
Next Action: Proceed to competitive analysis

✓ Phase 4 complete
```

**Save file:** pain_map.json

### Step 7: Phase 5 - Competitive Analysis

**Execute searches:**
```
[Tool: web_search "therapist practice management software"]
[Tool: web_search "notion templates for therapists"]
[Tool: web_search "therapy notes vs simplepractice"]
```

**Your output:**
```
---
## PHASE 5: COMPETITIVE ANALYSIS

**Objective**: Map competitive landscape

Competitors found:
- SimplePractice: $39-99/month
- TherapyNotes: $49-99/month
- Notion (DIY): Free but time-intensive
- Etsy templates: $10-50 (limited scope)

Market gap: No comprehensive Notion system specifically for therapists at one-time price

✓ Phase 5 complete
```

**Save file:** competitor_map.json

### Step 8: Phase 6 - Opportunity Scoring

**Your output:**
```
---
## PHASE 6: OPPORTUNITY SCORING

**Objective**: Score and decide CREATE/PIVOT/REJECT

Scoring:
1. Spending Clarity: 4/5 (clear $47-97 range)
2. Information Gap: 5/5 (no good Notion resources for therapists)
3. Urgency: 4/5 (practice organization is important)
4. Create Feasibility: 5/5 (clear scope, templates exist)
5. AI Multiplier: 4/5 (personalization possible)

Total: 22/25
Decision: CREATE
Confidence: high

=== GATE 3: SCORE THRESHOLD ===
Criteria: Total >= 18 AND decision = CREATE
Evidence: Score 22/25, decision = CREATE
Decision: PASS
Reasoning: Strong opportunity across all dimensions
Next Action: Proceed to strategy

✓ Phase 6 complete
```

**Save file:** opportunity_score.json

### Step 9: Phase 7 - Strategy

**Your output:**
```
---
## PHASE 7: STRATEGY

**Objective**: Define product strategy

Target user: Solo private practice therapists who want to organize with Notion

Format: Notion system + template library

Core promise: "Organize your entire therapy practice in Notion in under 2 hours (without the learning curve or monthly fees)"

Price: $79 (below $348/year software, above $10-50 templates)

Differentiator: "Unlike practice management software that costs $348+/year, this is a one-time purchase. Unlike DIY Notion that takes 10+ hours, this is plug-and-play."

Deliverables:
- Complete Notion workspace for therapy practice
- Client management database
- Session notes template
- Appointment tracker
- Billing tracker
- HIPAA compliance guide

Distribution:
- Reddit (r/psychotherapy, r/notion)
- Therapy Facebook groups
- Email partnerships

✓ Phase 7 complete
```

**Save file:** product_brief.json

### Step 10: Phase 8 - Outline

**Your output:**
```
---
## PHASE 8: OUTLINE

**Objective**: Create content structure

Product: "Therapy Practice OS for Notion"

Sections:
1. Getting Started (setup in 30 minutes)
2. Client Management (database + views)
3. Session Notes (templates + organization)
4. Appointments & Scheduling
5. Billing & Invoicing
6. HIPAA Compliance Guide
7. Customization Instructions

Estimated: 40 pages + Notion templates

✓ Phase 8 complete
```

**Save file:** outline.json

### Step 11: Phase 9 - Synthesis

**Your output:**
```
---
## PHASE 9: SYNTHESIS

**Objective**: Organize knowledge

Facts documented:
- Therapists spend $348-1,188/year on practice management
- DIY Notion takes 10+ hours to set up
- Etsy templates are limited (just one page)
- HIPAA compliance is major concern
- Most therapists want simple, all-in-one solution

Decisions:
- Format: Notion system (not just templates)
- Price: $79 (one-time)
- Include HIPAA guide (major concern)
- Make it plug-and-play (not DIY)

Pitfalls to avoid:
- Don't make it too complex
- Don't ignore HIPAA
- Don't price too high

✓ Phase 9 complete
```

**Save file:** knowledge_base.json

### Step 12: Phase 10 - Drafting

**Your output:**
```
---
## PHASE 10: DRAFTING

**Objective**: Write main product content

Writing "Therapy Practice OS for Notion"...
- Introduction (why Notion for therapists)
- Setup guide (30 minutes)
- Client management system
- Session notes templates
- Appointment tracking
- Billing workflow
- HIPAA compliance guide
- Customization instructions

Length: 45 pages

✓ Phase 10 complete
```

**Save file:** draft_product.md (45 pages)

### Step 13: Phase 11 - Artifacts

**Your output:**
```
---
## PHASE 11: ARTIFACTS

**Objective**: Create support materials

Creating:
1. Client database template (Notion)
2. Session notes template (Notion)
3. Appointment tracker (Notion)
4. Billing tracker (Notion)
5. HIPAA checklist (PDF)
6. Setup checklist (PDF)
7. Customization guide (PDF)

Total: 7 artifacts

✓ Phase 11 complete
```

**Save files:** artifact_manifest.json + 7 artifact files

### Step 14: Phase 12 - Personalization

**Your output:**
```
---
## PHASE 12: PERSONALIZATION

**Objective**: Define personalization

Input fields:
- State (for HIPAA variations)
- Practice type (solo/group)
- Specialties

Outputs:
- State-specific HIPAA notes
- Customized template views
- Specialty-specific fields

✓ Phase 12 complete
```

**Save file:** personalization_spec.json

### Step 15: Phase 13 - Packaging

**Your output:**
```
---
## PHASE 13: PACKAGING

**Objective**: Define buyer-facing package

Product: Therapy Practice OS for Notion v1.0

Includes:
- 45-page setup guide (PDF)
- Complete Notion workspace (duplicate link)
- 5 database templates
- HIPAA compliance guide
- Setup checklist
- Customization guide

Bonuses:
- Email templates for clients
- Intake form template
- Progress note examples

Price: $79
Guarantee: 30-day money-back

=== GATE 4: ARTIFACT COMPLETENESS ===
Criteria: Draft + 3+ artifacts + manifest
Evidence: 45-page draft, 7 artifacts, manifest complete
Decision: PASS
Reasoning: All components present
Next Action: Proceed to launch assets

✓ Phase 13 complete
```

**Save file:** package_manifest.json

### Step 16: Phase 14 - Launch Assets

**Your output:**
```
---
## PHASE 14: LAUNCH ASSETS

**Objective**: Create marketing materials

Creating:
1. Sales page (full landing page)
2. Launch posts (5 social posts)
3. Email sequence (5 emails)
4. FAQ (15 questions)
5. Objection handling (10 objections)

✓ Phase 14 complete
```

**Save files:** launch_assets/ directory with all materials

### Step 17: Phase 15 - Validation

**Your output:**
```
---
## PHASE 15: VALIDATION

**Objective**: Final quality check

Checking all gates:
✓ Gate 1: Spending evidence (4 signals, 4 quantified)
✓ Gate 2: Pain specificity (question + workarounds + costs)
✓ Gate 3: Score threshold (22/25, CREATE)
✓ Gate 4: Artifacts complete (draft + 7 artifacts + manifest)
✓ Gate 5: Launch ready (audience + channels + pricing)

=== GATE 5: LAUNCH READINESS ===
Criteria: Audience + channels + pricing
Evidence: All present and documented
Decision: PASS
Reasoning: Product is complete and ready for market
Next Action: Proceed to retrospective

✓ Phase 15 complete
```

**Save file:** validation_report.json

### Step 18: Phase 16 - Retrospective

**Your output:**
```
---
## PHASE 16: RETROSPECTIVE

**Objective**: Document learnings

What worked:
- Strong spending signals found quickly
- Clear pain points (overwhelmed by practice management)
- Market gap clearly identified
- Notion is hot topic with therapists

What didn't:
- Could have found more direct therapist testimonials

Surprises:
- Etsy templates exist but are very limited
- HIPAA is major concern (should emphasize in marketing)

Lessons:
- One-time vs recurring pricing is strong differentiator
- Plug-and-play positioning beats DIY

Updating memory files...
✓ Phase 16 complete
```

**Save file:** postmortem.json
**Update:** memory files

### Step 19: Final Report

**Your output:**
```
---
## RUN COMPLETE

**Niche**: Notion templates for therapists
**Mode**: Full
**Score**: 22/25
**Decision**: CREATE
**Status**: ✅ ALL GATES PASSED

**Artifacts Created**: 24 files
**Product**: Therapy Practice OS for Notion
**Price**: $79
**Status**: Ready for launch

**Key Findings**:
- Strong spending signals ($47-97 range)
- Clear pain (overwhelmed by practice management)
- Market gap (no comprehensive Notion system for therapists)
- High feasibility (Notion + templates)

**Recommendation**: PROCEED TO LAUNCH

All files saved to: runs/2026-03-06_notion-templates-therapists/
```

---

## Summary of Execution

| Step | Action | Output |
|------|--------|--------|
| 1 | Parse request | Mode + niche identified |
| 2 | Create directory | Run folder created |
| 3 | Phase 1 | run_config.json |
| 4 | Phase 2 | discovery_report.json |
| 5 | Phase 3 | spending_signals.json + Gate 1 PASS |
| 6 | Phase 4 | pain_map.json + Gate 2 PASS |
| 7 | Phase 5 | competitor_map.json |
| 8 | Phase 6 | opportunity_score.json + Gate 3 PASS |
| 9 | Phase 7 | product_brief.json |
| 10 | Phase 8 | outline.json |
| 11 | Phase 9 | knowledge_base.json |
| 12 | Phase 10 | draft_product.md |
| 13 | Phase 11 | artifact_manifest.json + 7 artifacts |
| 14 | Phase 12 | personalization_spec.json |
| 15 | Phase 13 | package_manifest.json + Gate 4 PASS |
| 16 | Phase 14 | launch_assets/ directory |
| 17 | Phase 15 | validation_report.json + Gate 5 PASS |
| 18 | Phase 16 | postmortem.json + memory updates |
| 19 | Final report | Summary to user |

---

## Key Takeaways

1. **Execute sequentially** - Don't skip phases
2. **Save after each phase** - Don't batch saves
3. **State gates explicitly** - Use the format
4. **Cite sources** - Every finding needs a URL
5. **Be honest** - Don't inflate scores
6. **Report clearly** - User should understand results

---

*This is what successful execution looks like*
