# Agentic KPF Quick Reference Card
## Print This and Keep It Visible

---

## 5-Second Start

```
User says: "[mode] [niche]"
↓
Create: runs/YYYY-MM-DD_[niche-slug]/
↓
Start Phase 1
```

---

## The 16 Phases (In Order)

| # | Phase | Output | Gate? |
|---|-------|--------|-------|
| 1 | Intake | run_config.json | No |
| 2 | Discovery | discovery_report.json | No |
| 3 | Spending | spending_signals.json | ✅ Gate 1 |
| 4 | Pain | pain_map.json | ✅ Gate 2 |
| 5 | Competitors | competitor_map.json | No |
| 6 | Scoring | opportunity_score.json | ✅ Gate 3 |
| 7 | Strategy | product_brief.json | No |
| 8 | Outline | outline.json | No |
| 9 | Synthesis | knowledge_base.json | No |
| 10 | Drafting | draft_product.md | No |
| 11 | Artifacts | artifact_manifest.json | No |
| 12 | Personalization | personalization_spec.json | No |
| 13 | Packaging | package_manifest.json | ✅ Gate 4 |
| 14 | Launch | launch_assets/ | No |
| 15 | Validation | validation_report.json | ✅ Gate 5 |
| 16 | Retrospective | postmortem.json | No |

---

## Gate Decision Format (Copy-Paste)

```
=== GATE X: [NAME] ===
Criteria: [What must be true]
Evidence: [What you found]
Decision: [PASS / FAIL / REVISE]
Reasoning: [Why]
Next Action: [Proceed / Stop / Go back]
```

---

## Scoring Rubric (1-5)

| Score | Spending Clarity | Information Gap | Urgency | Feasibility | AI Multiplier |
|-------|------------------|-----------------|---------|-------------|---------------|
| 5 | Multiple $500+ | Recurring confusion, no solutions | Revenue-impacting, urgent | Clear scope, templatable | Strong personalization |
| 4 | Some $200-500 | Clear questions, partial solutions | Important business impact | Well-defined, some complexity | Good AI enhancement |
| 3 | $50-200 | Some questions, okay solutions | Moderate impact | Moderate complexity | Some AI leverage |
| 2 | Some spending, unclear | Most info available | Nice-to-have | Complex, hard to scope | Minimal AI value |
| 1 | No spending evidence | Info readily available, solved | Low priority | Too vague/complex | No AI leverage |

**Total >= 18 = CREATE**

---

## Search Query Templates

### Communities
```
"[niche] reddit"
"[niche] forum"
"[niche] facebook group"
"[niche] community"
```

### Spending
```
"[niche] paid $"
"[niche] cost"
"[niche] price"
"[niche] spent"
"[niche] worth it"
```

### Pain
```
"[niche] frustrated"
"[niche] struggling"
"[niche] help"
"how do I [niche]"
"[niche] problem"
```

### Competitors
```
"[niche] course"
"[niche] template"
"[niche] service"
"[niche] tool"
"best [niche]"
```

---

## Artifact Schemas (Quick Check)

### spending_signals.json
```json
{
  "niche": "string",
  "signals": [{"quote", "amount_usd", "time_cost", "source", "url"}],
  "signal_count": number,
  "passes_threshold": boolean
}
```

### opportunity_score.json
```json
{
  "scores": {
    "spending_clarity": 1-5,
    "information_gap": 1-5,
    "urgency": 1-5,
    "create_feasibility": 1-5,
    "ai_multiplier": 1-5
  },
  "total": number,
  "decision": "CREATE | PIVOT | REJECT"
}
```

---

## Mode Stop Points

| Mode | Stop After Phase | Output |
|------|------------------|--------|
| discover | 2 | discovery_report.json |
| validate | 6 | opportunity_score.json |
| build | 13 | package_manifest.json |
| launch | 15 | validation_report.json |
| full | 16 | postmortem.json |

---

## Common Issues (Quick Fix)

| Issue | Solution |
|-------|----------|
| No search results | Try broader terms, related topics |
| Weak spending | Look for time costs, hiring patterns |
| Vague pain | Search "how do I [niche]" |
| Too much competition | Look for sub-niches, format gaps |
| Can't decide score | Default conservative, document uncertainty |

---

## Pricing Guidelines

```
Price must be between $79-199 (default constraints)

Base price on:
- Spending signals found
- Competitor anchors
- Value delivered

Sweet spot: Below services, above DIY opportunity cost
```

---

## File Naming Convention

```
runs/YYYY-MM-DD_[kebab-case-niche]/
├── run_config.json
├── discovery_report.json
├── spending_signals.json
├── pain_map.json
├── competitor_map.json
├── opportunity_score.json
├── product_brief.json
├── outline.json
├── knowledge_base.json
├── draft_product.md
├── personalization_spec.json
├── package_manifest.json
├── validation_report.json
├── postmortem.json
├── artifacts/
│   └── artifact_manifest.json
└── launch_assets/
    ├── sales_page.md
    ├── launch_posts.md
    ├── faq.md
    └── objections.md
```

---

## Success Checklist

- [ ] All phases executed
- [ ] Gates explicitly decided
- [ ] All artifacts saved
- [ ] Evidence cited with URLs
- [ ] Clear recommendation
- [ ] Memory files updated
- [ ] RUN_SUMMARY.md created

---

## Emergency: When to STOP

STOP and report if:
- ❌ Gate fails with no recovery path
- ❌ Score < 14 (REJECT)
- ❌ User asks to stop
- ❌ Insufficient evidence after 3+ searches

---

## Remember

> **Evidence > Opinion**
> **Gates Matter**
> **Be Honest**
> **Save Everything**

---

*Keep this card visible while executing*
