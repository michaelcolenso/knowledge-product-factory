The following JSON is malformed or does not match the required schema. Fix it to be valid JSON matching this exact structure:

{schema_json}

Rules:
- satisfaction must be exactly "happy", "neutral", or "frustrated"
- signal_count must equal the actual number of items in the signals array
- passes_threshold must be a boolean
- amount_usd must be an integer or null (not a string)
- Return only the corrected JSON object with no other text
