The following JSON is malformed or does not match the required schema. Fix it to be valid JSON matching this exact structure:

{schema_json}

Rules:
- type must be exactly one of: "information_gap", "frustration", "competitor_failure", "time_loss", "money_risk"
- frequency_estimate must be an integer
- current_workarounds must be a non-empty list of strings
- Return only the corrected JSON object with no other text
