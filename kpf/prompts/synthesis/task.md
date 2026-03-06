Synthesize a knowledge base for this product from the provided research data. Transform all upstream artifacts into structured, actionable facts.

Schema to output:
{schema_json}

Source data to synthesize from:
- Spending signals (what buyers value and pay for)
- Pain map (specific problems and consequences)
- Competitor map (what gaps exist in current solutions)
- Opportunity score (what dimensions matter most)
- Product brief (what problem this product solves)
- Outline (what sections need content)

Requirements:
- facts: At least 10 specific, actionable claims. Each fact must be:
  - claim: Specific and implementable ("File Form X before Form Y or your application will be rejected")
  - support: Evidence from the research data
  - confidence: low/medium/high based on evidence quality
- decisions: 5+ specific decision points the target user must make (not generic advice)
- pitfalls: 5+ specific mistakes with real consequences
- contradictions: Things where your research sources disagree or where the answer is genuinely unclear

Quality bar:
- Strong fact: "CAQH credentialing takes 60-90 days for panel approval - apply to 5+ panels simultaneously to hit revenue targets within 6 months"
- Weak fact (reject): "Insurance credentialing is a complex process that requires attention to detail"
