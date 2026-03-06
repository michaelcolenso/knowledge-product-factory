# Agentic KPF Template Library
## Copy-Paste Templates for Common Artifacts

---

## 1. Discovery Report Template

```json
{
  "niche": "[NICHE_NAME]",
  "run_id": "[RUN_ID]",
  "discovery_date": "YYYY-MM-DD",
  "summary": "[2-3 sentence summary of findings]",
  "communities": [
    {
      "name": "[Community Name]",
      "type": "reddit | forum | facebook_group | other",
      "member_count": number or null,
      "relevance": "High | Medium | Low"
    }
  ],
  "spending_signals_found": [
    {
      "quote": "[Exact quote]",
      "source": "[Site name]",
      "url": "[Full URL]",
      "amount_usd": number or null,
      "amount_range": "string or null",
      "purchase_type": "service | course | tool | template | time_investment | revenue_share | lost_revenue",
      "job_to_be_done": "[What they wanted to achieve]",
      "satisfaction": "happy | neutral | frustrated"
    }
  ],
  "pain_patterns_found": [
    {
      "type": "information_gap | frustration | time_loss | money_risk | competitor_failure",
      "quote": "[Exact quote]",
      "source": "[Site name]",
      "url": "[Full URL]",
      "frequency_estimate": 1-100
    }
  ],
  "key_insights": [
    "[Insight 1]",
    "[Insight 2]",
    "[Insight 3]"
  ],
  "initial_confidence": "high | medium | low"
}
```

---

## 2. Spending Signals Template

```json
{
  "niche": "[NICHE_NAME]",
  "signals": [
    {
      "community": "[Where found]",
      "quote": "[Exact quote with $ or time]",
      "purchase_type": "service | course | tool | template | time_investment | revenue_share | lost_revenue | opportunity_cost",
      "amount_usd": number or null,
      "amount_range": "string or null",
      "time_cost": "string or null (e.g., '20-30 hours')",
      "job_to_be_done": "[What they wanted]",
      "satisfaction": "happy | neutral | frustrated",
      "date": "YYYY-MM-DD",
      "source": "[Site name]",
      "url": "[Full URL]"
    }
  ],
  "signal_count": number,
  "passes_threshold": boolean,
  "quantified_count": number,
  "price_range": "[e.g., '150-2000']",
  "key_insight": "[One sentence summary]"
}
```

---

## 3. Pain Map Template

```json
{
  "niche": "[NICHE_NAME]",
  "core_question": "[The recurring question people ask]",
  "patterns": [
    {
      "type": "information_gap | frustration | time_loss | money_risk | competitor_failure",
      "quote": "[Exact quote]",
      "source": "[Site name]",
      "url": "[Full URL]",
      "frequency_estimate": 1-100
    }
  ],
  "current_workarounds": [
    "[Workaround 1]",
    "[Workaround 2]",
    "[Workaround 3]"
  ],
  "time_wasted": "[Quantified time cost]",
  "money_risked": "[Quantified money cost]",
  "emotional_state": "[How they feel - use their words]",
  "ideal_solution_language": "[Exact words they use to describe ideal solution]"
}
```

---

## 4. Competitor Map Template

```json
{
  "niche": "[NICHE_NAME]",
  "alternatives": [
    {
      "name": "[Competitor name]",
      "category": "free | course | consultant | service | software | platform | community",
      "price": "[Price or 'Free']",
      "weaknesses": [
        "[Weakness 1]",
        "[Weakness 2]",
        "[Weakness 3]"
      ]
    }
  ],
  "market_gap_summary": "[What's missing in the market]",
  "switching_reason": "[Why someone would choose your product over alternatives]"
}
```

---

## 5. Opportunity Score Template

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
  "decision": "CREATE | PIVOT | REJECT",
  "confidence": "low | medium | high",
  "justification": {
    "spending_clarity": "[Why you scored this]",
    "information_gap": "[Why you scored this]",
    "urgency": "[Why you scored this]",
    "create_feasibility": "[Why you scored this]",
    "ai_multiplier": "[Why you scored this]"
  },
  "key_insights": [
    "[Insight 1]",
    "[Insight 2]"
  ]
}
```

---

## 6. Product Brief Template

```json
{
  "opportunity_name": "[Product name]",
  "target_user": "[Specific segment]",
  "format": "playbook | template_library | notion_system | sop | checklist_pack | decision_framework | research_brief",
  "core_promise": "[Transformation statement - what they'll achieve]",
  "price": number,
  "price_justification": "[Why this price]",
  "ai_leverage": "[How AI enhances the product]",
  "differentiator": "[Why choose this over competitors]",
  "deliverables": [
    "[Deliverable 1]",
    "[Deliverable 2]",
    "[Deliverable 3]"
  ],
  "distribution_channels": [
    "[Channel 1]",
    "[Channel 2]",
    "[Channel 3]"
  ],
  "success_metrics": {
    "user_goal": "[What success looks like for user]",
    "financial_goal": "[Revenue target]",
    "impact_goal": "[Users helped target]"
  }
}
```

---

## 7. Outline Template

```json
{
  "product_title": "[Title]",
  "subtitle": "[Subtitle]",
  "sections": [
    {
      "title": "[Section title]",
      "goal": "[What this section achieves]",
      "bullets": [
        "[Point 1]",
        "[Point 2]",
        "[Point 3]"
      ],
      "artifacts_referenced": ["template_name"]
    }
  ],
  "estimated_pages": number,
  "estimated_templates": number,
  "estimated_checklists": number,
  "creation_timeline": "[e.g., '3 weeks']"
}
```

---

## 8. Knowledge Base Template

```json
{
  "niche": "[NICHE_NAME]",
  "facts": [
    {
      "claim": "[Statement]",
      "support": "[Evidence]",
      "confidence": "low | medium | high"
    }
  ],
  "decisions": [
    "[Decision 1]",
    "[Decision 2]"
  ],
  "pitfalls": [
    "[Pitfall 1]",
    "[Pitfall 2]"
  ],
  "contradictions": [
    {
      "issue": "[Conflicting information]",
      "resolution": "[How to reconcile]"
    }
  ]
}
```

---

## 9. Artifact Manifest Template

```json
{
  "items": [
    {
      "name": "[Artifact name]",
      "file_name": "[filename.ext]",
      "purpose": "[What it's for]",
      "format": "markdown | csv | pdf | other"
    }
  ],
  "total_count": number,
  "categories": {
    "checklists": number,
    "templates": number,
    "trackers": number,
    "scripts": number
  }
}
```

---

## 10. Package Manifest Template

```json
{
  "product_name": "[Product name]",
  "version": "1.0.0",
  "tier": "basic | pro | complete",
  "included_files": [
    "[File 1]",
    "[File 2]"
  ],
  "delivery_notes": [
    "[Note 1]",
    "[Note 2]"
  ],
  "bonuses": [
    "[Bonus 1]",
    "[Bonus 2]"
  ],
  "guarantee": "[Money-back guarantee terms]"
}
```

---

## 11. Validation Report Template

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
    "gate_1_spending": {
      "passed": boolean,
      "criteria": "string",
      "evidence": "string"
    },
    "gate_2_pain": {
      "passed": boolean,
      "criteria": "string",
      "evidence": "string"
    },
    "gate_3_score": {
      "passed": boolean,
      "criteria": "string",
      "evidence": "string"
    },
    "gate_4_artifacts": {
      "passed": boolean,
      "criteria": "string",
      "evidence": "string"
    },
    "gate_5_launch": {
      "passed": boolean,
      "criteria": "string",
      "evidence": "string"
    }
  },
  "issues": [],
  "required_revisions": [],
  "overall_assessment": "string",
  "confidence": "low | medium | high",
  "recommendation": "PROCEED TO LAUNCH | NEEDS REVISION | DO NOT LAUNCH"
}
```

---

## 12. Postmortem Template

```json
{
  "run_id": "[RUN_ID]",
  "completion_date": "YYYY-MM-DD",
  "niche": "[NICHE]",
  "mode": "discover | validate | build | launch | full",
  "final_status": "SUCCESS | PARTIAL | FAILED",
  "opportunity_score": number,
  "decision": "CREATE | PIVOT | REJECT",
  "what_worked": [
    "[What worked 1]",
    "[What worked 2]"
  ],
  "what_didnt_work": [
    "[What didn't 1]",
    "[What didn't 2]"
  ],
  "surprises": [
    "[Surprise 1]",
    "[Surprise 2]"
  ],
  "lessons_learned": [
    "[Lesson 1]",
    "[Lesson 2]"
  ],
  "memory_updates": {
    "winning_niches": {},
    "search_patterns": [],
    "format_performance": {}
  },
  "recommendations_for_future": [
    "[Recommendation 1]",
    "[Recommendation 2]"
  ]
}
```

---

## Sales Page Template (Markdown)

```markdown
# [Product Name]
## [Core Promise]

---

## The Problem

[Describe the pain in user's words]

---

## The Cost of Waiting

Every [time period] you wait costs you [quantified cost].

---

## Your Options

**Option 1: [DIY approach]**
- Cost: [Time/opportunity cost]
- Reality: [Problems with this approach]

**Option 2: [Expensive service]**
- Cost: [$ amount]
- Reality: [Problems with this approach]

**Option 3: [Alternative]**
- Cost: [Hidden costs]
- Reality: [Problems with this approach]

---

## Introducing: [Product Name]

[What it is and what it includes]

---

## What's Inside

- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

---

## What Makes This Different

[Differentiator statement]

---

## The Investment

**$[Price]**

Compare to:
- [Alternative 1]: $[Cost]
- [Alternative 2]: $[Cost]
- [Alternative 3]: $[Cost]

---

## 30-Day Money-Back Guarantee

[Guarantee terms]

---

## FAQ

**Q: [Question 1]?**
A: [Answer 1]

**Q: [Question 2]?**
A: [Answer 2]

---

## Ready to [Achieve Outcome]?

[Call to action]

**[GET INSTANT ACCESS - $[Price]]**
```

---

## Launch Post Templates

### Post 1: Problem Awareness
```
[Headline with quantified pain]

[Describe the problem in user's words]

[Quantify the cost of waiting]

There's a better way.

[Tease solution]

Link in [location].
```

### Post 2: Solution Reveal
```
[Headline with result]

[Your story/experience]

So I built [solution]:
✅ [Benefit 1]
✅ [Benefit 2]
✅ [Benefit 3]

Result: [Outcome]

[Call to action]
```

### Post 3: Social Proof
```
[Headline with testimonial]

What [users] are saying:

💬 "[Quote 1]" — [Name]
💬 "[Quote 2]" — [Name]

[Product] = $[Price]
[Outcome] = [Value]

[Call to action]
```

### Post 4: Urgency
```
[Headline with urgency]

[Why now matters]

[Quantified cost of waiting]

[Call to action with deadline]
```

### Post 5: Final Call
```
[Headline with two futures]

Two versions of you [timeframe] from now:

Version A: [Positive outcome]
Version B: [Negative outcome]

The difference? [Action]

[Call to action]
```

---

## FAQ Template

```markdown
# Frequently Asked Questions

## Product Questions

**Q: What exactly is included?**
A: [List deliverables]

**Q: What format are the materials?**
A: [Format details]

**Q: Is this a one-time fee or recurring?**
A: [Pricing clarification]

## Process Questions

**Q: How long does this take?**
A: [Timeline]

**Q: Does this work for [specific situation]?**
A: [Answer]

## Guarantee

**Q: Is there a guarantee?**
A: [Guarantee terms]
```

---

## Objection Handling Template

```markdown
# Objection: "[Objection]"

**Response:**

[Acknowledge concern]

[Reframe with data]

[Compare to alternatives]

[Remove risk with guarantee]

[Call to action]
```

---

## CSV Tracker Templates

### Application Tracker
```csv
Payer Name,Date Submitted,Submission Method,Confirmation Number,Contact Name,Contact Phone,Status,Last Follow-Up,Next Follow-Up Date,Notes,Approved Date,Effective Date
[Payer 1],,,,,,Not Started,,,,
[Payer 2],,,,,,Not Started,,,,
```

### Expiration Tracker
```csv
Item,Type,Issue Date,Expiration Date,Days Until Expiration,Renewal Started,Notes
[Item 1],[Type],,,,,
[Item 2],[Type],,,,,
```

---

*Copy these templates and fill in the blanks*
