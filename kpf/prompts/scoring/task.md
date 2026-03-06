Score this knowledge product opportunity across five dimensions using the provided research data.

Schema to output:
{schema_json}

Scoring rules (integer 1-5 only):

spending_clarity:
- 5: Multiple quantified dollar amounts, clear active budget, buyer described purchase
- 4: Clear spending with 1-2 amounts quantified
- 3: Spending implied but not quantified
- 2: Vague interest, no clear budget
- 1: No evidence of spending

information_gap:
- 5: Specific recurring question with no good answer anywhere
- 4: Good answers exist but are hard to find or incomplete
- 3: Partial answers exist in scattered places
- 2: Decent answers exist with minor gaps
- 1: Well-covered topic

urgency:
- 5: Time-sensitive consequence (compliance, revenue loss, career risk) for wrong answer
- 4: Clear professional consequence but not immediate
- 3: Some consequence but manageable delay
- 2: Nice-to-have, no real urgency
- 1: Evergreen topic with no urgency

create_feasibility:
- 5: Buildable in 1-2 weeks with available information
- 4: Buildable in 2-3 weeks
- 3: Buildable in 3-4 weeks with research
- 2: Would need 4-8 weeks or expert access
- 1: Not feasible without months of research

ai_multiplier:
- 5: AI reduces creation from months to days (structured data, clear process)
- 4: AI reduces from weeks to days
- 3: AI helps but human expertise still bottleneck
- 2: AI has limited leverage (needs primary research)
- 1: AI adds little value

Decision rules:
- total >= 18 → CREATE
- total 13-17 → PIVOT
- total < 13 → REJECT

justification: One sentence per dimension explaining the score based on specific evidence from the data provided.
