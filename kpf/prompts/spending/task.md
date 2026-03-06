Synthesize spending signals for this niche. Find evidence that people in this niche actively spend on solving information problems.

Schema to output:
{schema_json}

Requirements:
- Capture at least 3 distinct spending signals
- At least 2 signals must have quantified dollar amounts (amount_usd) or time costs (time_cost)
- Each signal must have a clear job_to_be_done - what they're trying to accomplish
- Reject vague signals like "people discuss this a lot" - require evidence of actual spending behavior
- signal_count must equal the number of signals in the list
- passes_threshold: true only if signal_count >= 3 AND at least 2 are quantified

Examples of strong signals:
- "r/therapists: Just paid $2,500 for a credentialing consultant. Took 4 months. Worth every penny."
- "Spent 3 hours last week searching for which forms to submit. Finally gave up and hired someone."

Examples of weak signals (do not include):
- "People are interested in this topic"
- "Many posts ask about this"
