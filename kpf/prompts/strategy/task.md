Design the product brief for this knowledge product based on the validated opportunity data.

Schema to output:
{schema_json}

Requirements:
- opportunity_name: Clear, specific name (e.g., "Therapist Insurance Panel Accelerator")
- target_user: Specific person description (e.g., "Solo practice therapist, 0-2 years in private practice, credentialing with their first 3 insurance panels")
- format: Must be one of: playbook, SOP, template_library, decision_framework, checklist_pack, notion_system, research_brief
- core_promise: Single outcome in buyer language (e.g., "Get credentialed with 3 insurance panels in 90 days without hiring a consultant")
- price: Integer USD price between price_floor and price_ceiling from constraints
- ai_leverage: How AI made this product possible or faster to create
- differentiator: What makes this different from the best existing alternative (be specific)
- deliverables: List of every item included (e.g., "28-page credentialing playbook", "CAQH setup checklist", "Panel comparison spreadsheet")
- distribution_channels: Where to find the first 100 buyers (e.g., "r/therapists", "Private Practice Boot Camp Facebook group", "therapist email lists via Headway")

Constraints to respect from the run config:
- Respect price_floor and price_ceiling
- Respect max_creation_weeks (product scope must be achievable in that time)
- Format must be in allowed_formats if specified
