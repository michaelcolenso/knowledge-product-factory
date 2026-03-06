# Agentic Knowledge Product Factory

## What This Is

A **workflow system** designed for AI agents (like me) to execute. Instead of being code that calls APIs, this is a structured process that I follow using my tools (search, browse, reason, write) to research, validate, and create knowledge products.

## The Shift

| Aspect | Old (Software) | New (Agentic) |
|--------|---------------|---------------|
| **Orchestrator** | Python code | AI agent (me) |
| **Research** | API calls to LLMs | Web search, browsing |
| **Evidence** | Synthetic data | Real quotes, URLs |
| **Decisions** | Rigid thresholds | Reasoned judgment |
| **Cost** | API fees | None (use existing tools) |
| **Adaptability** | Fixed pipeline | Can dig deeper, pivot |

## How It Works

### 1. You Give Me a Command
```
"Validate therapist insurance credentialing"
"Build notion templates for therapists"
"Full run: productivity system for developers"
```

### 2. I Execute Phases
Using my tools, I work through:
- **Intake**: Set up the run
- **Discovery**: Search for communities, spending, pain
- **Spending Analysis**: Quantify willingness to pay
- **Pain Mapping**: Understand the problem
- **Competitive Analysis**: Research alternatives
- **Opportunity Scoring**: Decide CREATE/PIVOT/REJECT
- **Strategy**: Define product brief
- **Outline**: Structure the content
- **Synthesis**: Organize knowledge
- **Drafting**: Write the product
- **Artifacts**: Create templates/checklists
- **Personalization**: Define customization (optional)
- **Packaging**: Bundle for sale
- **Launch Assets**: Create marketing
- **Validation**: Final quality check
- **Retrospective**: Document learnings

### 3. I Make Gate Decisions
At 5 checkpoints, I explicitly decide:
- **Gate 1**: Spending evidence sufficient? (3+ signals, 2+ quantified)
- **Gate 2**: Pain specific enough? (question + workaround + cost)
- **Gate 3**: Score high enough? (>= 18 = CREATE)
- **Gate 4**: Artifacts complete? (draft + 3+ support + manifest)
- **Gate 5**: Launch ready? (audience + channels + pricing)

If a gate fails, I stop and explain why.

### 4. I Save Everything
All artifacts saved to:
```
runs/YYYY-MM-DD_[niche-slug]/
```

### 5. I Report Results
Clear summary with:
- What I found
- Opportunity score
- Go/no-go recommendation
- Key evidence

## Files in This System

| File | Purpose |
|------|---------|
| `AGENTIC_KPF.md` | Complete workflow documentation |
| `AGENTIC_QUICKSTART.md` | Quick reference for execution |
| `PROMPTS.md` | Phase-by-phase instructions |
| `kpf/` | Original software implementation (reference) |

## Usage

### Validate a Niche (Research Only)
```
"Run KPF validate on [niche]"
```
I research and score, stopping before build.

### Build a Product
```
"Run KPF build on [niche]"
```
I validate, then create the product.

### Full Run
```
"Run KPF full on [niche]"
```
I do everything including launch assets.

### Discover Niches
```
"Run KPF discover"
```
I find and suggest niches to explore.

## What I Produce

For a **validate** run:
- `run_config.json`
- `discovery_report.json`
- `spending_signals.json`
- `pain_map.json`
- `competitor_map.json`
- `opportunity_score.json`

For a **build** run (plus above):
- `product_brief.json`
- `outline.json`
- `knowledge_base.json`
- `draft_product.md`
- `artifacts/` (3+ support files)
- `personalization_spec.json` (optional)
- `package_manifest.json`

For a **full** run (plus above):
- `launch_assets/` (sales page, FAQ, posts, etc.)
- `validation_report.json`
- `postmortem.json`

## Why This Works Better

1. **Real Evidence**: I search actual web, not generate synthetic data
2. **Current Data**: Live competitor pricing, not training cutoff
3. **Human Judgment**: I can override rules when justified
4. **Adaptive**: If findings are weak, I can search more
5. **Transparent**: Every decision explained with sources
6. **No Costs**: No API fees

## Example Session

**You**: "Validate therapist insurance credentialing"

**Me**:
```
I'll execute Agentic KPF in VALIDATE mode for "therapist insurance credentialing".

---
PHASE 1: INTAKE
✓ Niche validated: specific enough
✓ Run directory created: runs/2026-03-06_therapist-insurance-credentialing/

---
PHASE 2: DISCOVERY
Searching for communities...
[web_search "therapist insurance credentialing reddit"]
Found: r/psychotherapy (180k members)

Searching for spending signals...
[web_search "therapist insurance credentialing paid $"]
Found: "$500 for credentialing service" (r/psychotherapy)
Found: "40 hours doing it myself" (Facebook group)
Found: "$97 checklist saved me time"

Searching for pain points...
Found: "How do I get paneled without spending months?"
Found: "Every insurance company wants different forms"

---
PHASE 3: SPENDING ANALYSIS
=== GATE 1: SPENDING EVIDENCE ===
Signals: 3
Quantified: 3 ($500, 40 hours, $97)
Decision: PASS

---
PHASE 4: PAIN MAPPING
=== GATE 2: PAIN SPECIFICITY ===
Core question: "How do I get paneled without spending months?"
Workaround: Hiring $500-2000 services
Cost: 20-40 hours or $500-2000
Decision: PASS

---
PHASE 5: COMPETITIVE ANALYSIS
Found competitors:
- Course: $199 (generic)
- Service: $500-2000 (expensive)
- Free resources: (incomplete)
Market gap: Step-by-step system at affordable price

---
PHASE 6: OPPORTUNITY SCORING
Spending clarity: 5 (clear $ amounts)
Information gap: 5 (strong confusion)
Urgency: 4 (revenue impact)
Create feasibility: 5 (templatable)
AI multiplier: 4 (personalization possible)

Total: 23/25
Decision: CREATE

=== GATE 3: SCORE THRESHOLD ===
Score: 23 >= 18
Decision: PASS

---
VALIDATION COMPLETE

Niche: Therapist insurance credentialing
Score: 23/25
Decision: CREATE

Key Findings:
- Strong spending signals ($97-500 range)
- Clear pain (time + complexity)
- Underserved market (gap between $199 course and $500 service)

Recommendation: Proceed to BUILD mode
All artifacts saved to: runs/2026-03-06_therapist-insurance-credentialing/
```

## Key Principles

1. **Evidence-Based**: Every claim needs a source
2. **Gate-Driven**: Stop if validation fails
3. **Transparent**: Explain all decisions
4. **Honest**: Don't inflate scores
5. **Complete**: Save all artifacts

## Ready?

Give me a niche and mode:
- "Validate [niche]"
- "Build [niche]"
- "Full run [niche]"
- "Discover niches"

I'll execute the workflow.
