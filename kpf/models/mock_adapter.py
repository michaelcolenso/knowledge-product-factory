import json


class MockAdapter:
    def generate(self, system_prompt: str, user_prompt: str, temperature: float = 0.2) -> str:
        marker = (system_prompt + "\n" + user_prompt).lower()
        if "repair" in marker or "validator" in marker:
            return user_prompt
        if "discovery" in marker:
            return json.dumps({"niches": [{"name": "therapist insurance credentialing", "audience": "private practice therapists", "problem_summary": "credentialing delays hurt cash flow", "format_fit": "playbook", "feasible_in_weeks": 3}]})
        return "{}"
