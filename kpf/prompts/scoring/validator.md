The following JSON is malformed or does not match the required schema. Fix it to be valid JSON matching this exact structure:

{schema_json}

Rules:
- All score values must be integers between 1 and 5 (not strings, not floats)
- total must equal the sum of all five dimension scores
- decision must be exactly "CREATE", "PIVOT", or "REJECT"
- confidence must be exactly "low", "medium", or "high"
- justification must be a dict with string keys and string values
- Return only the corrected JSON object with no other text
