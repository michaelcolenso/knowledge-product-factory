Design the personalization specification for this knowledge product.

Schema to output:
{schema_json}

Requirements:
- input_fields: The specific buyer inputs that drive personalization (e.g., "practice_state", "specialization", "panel_targets")
- generation_logic: Rules for transforming inputs into customized outputs (e.g., "If practice_state=CA, include DMHC requirements section")
- outputs: What gets personalized in the final product (e.g., "State-specific compliance checklist", "Personalized panel priority list")
- update_strategy: How buyers can re-run personalization when their situation changes

Only include personalization if it meaningfully improves buyer outcomes. If the product doesn't benefit from personalization, output empty lists and note why in update_strategy.
