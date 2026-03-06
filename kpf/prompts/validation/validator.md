The following JSON is malformed or does not match the required schema. Fix it to be valid JSON matching this exact structure:

{schema_json}

Rules:
- status must be exactly "PASS", "REVISE", or "FAIL"
- checks must be a dict mapping string keys to boolean values
- issues and required_revisions must be lists (can be empty)
- Return only the corrected JSON object with no other text
