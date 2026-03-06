# Agentic KPF Quickstart

## For AI Agents Executing This Workflow

### Your Role
You are the orchestrator. You execute each phase using your tools (search, browse, reason, write).

### Execution Pattern

```
PHASE X: [Name]
Objective: [What to accomplish]
Tools: [Which tools to use]
Process: [Step-by-step]
Gate: [Decision criteria]
Output: [What to produce]
```

### State Tracking

Maintain a running state block in your context:

```yaml
Current Run:
  run_id: "2026-03-06_therapist-insurance-credentialing"
  mode: "validate"
  niche: "therapist insurance credentialing"
  phase: "scoring"
  
Artifacts Created:
  - run_config
  - discovery_report
  - spending_signals
  - pain_map
  - competitor_map
  - opportunity_score
  
Gates Passed:
  - spending: true
  - pain: true
  
Current Score: 23
Decision: CREATE
```

### Tool Usage

**Web Search** (most common):
- Use for: Finding communities, spending signals, pain points, competitors
- Pattern: Search → Analyze results → Extract evidence → Document with URLs

**Browser Visit** (for deep dives):
- Use for: Competitor pricing, sales pages, forum threads
- Pattern: Visit → Read → Extract key info → Document

**File Write** (persistence):
- Use for: Saving artifacts, updating memory
- Pattern: Generate JSON → Save to run directory

### Gate Decision Format

Always state gates explicitly:

```
=== GATE X: [Name] ===
Criteria: [What must be true]
Evidence: [What you found]
Decision: [PASS / FAIL / REVISE]
Reasoning: [Why]
Next Action: [Proceed / Stop / Go back]
```

### Example Execution

**User**: "Validate 'notion templates for therapists'"

**Your Response**:

```
I'll execute Agentic KPF in VALIDATE mode for "notion templates for therapists".

---
PHASE 1: INTAKE
Objective: Validate niche and set up run

Niche: "notion templates for therapists"
Validation: ✓ Specific (tool + audience)
Constraints: 3 weeks, $79-199, formats: notion_system/template_library
Run ID: 2026-03-06_notion-templates-therapists

Creating run directory...
✓ Run directory created: runs/2026-03-06_notion-templates-therapists/

Saving run_config.json...
✓ Phase 1 complete

---
PHASE 2: DISCOVERY
Objective: Find communities and initial evidence

Searching for communities...
[Tool: web_search "therapists notion templates reddit"]
Results:
- r/psychotherapy (180k members)
- r/therapists (95k members)
- r/privatepractice (45k members)

Searching for spending signals...
[Tool: web_search "therapist notion template paid"]
Results:
- "I bought a $47 Notion template for my practice" (r/privatepractice)
- "Spent $97 on a practice management template, worth it" (comment)
- "Looking for Notion templates, budget $50-100" (thread)

Searching for pain points...
[Tool: web_search "therapist practice management overwhelmed"]
Results:
- "Can't keep track of client notes and appointments"
- "Documentation taking too much time"
- "Need a system for my private practice"

Documenting findings...
✓ Phase 2 complete
Saved: discovery_report.json

---
PHASE 3: SPENDING ANALYSIS
Objective: Quantify willingness to pay

Signals extracted:
1. $47 - Notion template purchase (happy)
2. $97 - Practice management template (happy)
3. $50-100 budget mentioned (intent)

Quantified: 2/3 with $ amounts

=== GATE 1: SPENDING EVIDENCE ===
Criteria: 3+ signals, 2+ quantified
Evidence: 3 signals found, 2 with $ amounts ($47, $97)
Decision: PASS
Reasoning: Clear willingness to pay $47-97 for templates
Next Action: Proceed to pain mapping

✓ Phase 3 complete
Saved: spending_signals.json

---
[Continue through remaining phases...]

---
FINAL REPORT

Niche: Notion templates for therapists
Mode: VALIDATE
Score: 21/25
Decision: CREATE

Key Findings:
- Strong communities (320k+ total members)
- Clear spending ($47-97 price range)
- Specific pain (practice management overwhelm)
- Moderate competition (differentiation possible)

Recommendation: Proceed to BUILD mode
```

### Decision Rules

**Always stop and report if**:
- Gate fails with no path to recovery
- User asks you to stop
- Evidence is clearly insufficient

**You may override if**:
- Strong qualitative evidence despite low quantitative
- Unique insight not captured by scoring
- User provides additional context

(But document why you overrode)

### Artifact Quality

Every artifact should be:
- **Complete**: All required fields
- **Sourced**: Include URLs for evidence
- **Honest**: Don't inflate scores or findings
- **Actionable**: Clear what to do next

### Memory Updates

After each run, update:
- `winning_niches.json` (if passed)
- `failed_niches.json` (if failed)
- `format_performance.json` (track which formats work)
- `search_patterns.json` (save successful queries)

### Common Patterns

**Weak spending signals?**:
- Search for time costs ("spent 10 hours")
- Search for hiring patterns ("hired someone to")
- Search for tool purchases ("bought software")

**Vague pain points?**:
- Search for "how do I" + niche
- Search for "struggling with" + niche
- Search for "frustrated" + niche

**Too much competition?**:
- Look for underserved sub-niches
- Check for recent complaints about existing solutions
- Identify format gaps (everyone does courses, no one does X)

### Quick Commands

When user says:
- "Discover niches" → Run Phase 1-2 only
- "Validate [niche]" → Run Phase 1-6
- "Build [niche]" → Run Phase 1-13
- "Full run [niche]" → Run all phases

### Success Metrics

A successful agentic run:
1. All phases documented
2. Gates explicitly decided
3. Artifacts saved to disk
4. Clear go/no-go recommendation
5. Evidence cited with sources

---

Ready to execute. What's your command?
