# Agentic KPF - AI-Agent-Executed Knowledge Product Factory

## Philosophy Shift

**OLD**: CLI tool orchestrates API calls to LLMs  
**NEW**: AI Agent (you) executes workflow using tools (search, browse, reason, write)

## Why Agentic?

1. **Real Research**: Search for actual spending signals, not synthetic data
2. **Live Competitive Analysis**: Browse current competitor offerings
3. **Human Judgment**: Apply reasoning at gates, not rigid thresholds
4. **Adaptive**: Change course based on findings
5. **No API Costs**: Use existing tool access
6. **Transparent**: Every decision is visible and explainable

---

## Agentic Workflow

### Phase 1: INTAKE (Agent Setup)

**Your Role**: Configuration validator and run initializer

**Process**:
1. Accept user niche (e.g., "therapist insurance credentialing")
2. Validate niche specificity (reject if too vague)
3. Set constraints (max weeks, price range, formats)
4. Create run directory structure
5. Initialize state tracking

**Tools**: None (internal reasoning)

**Output**: `run_config.json`

---

### Phase 2: DISCOVERY (Niche Research)

**Your Role**: Research analyst finding evidence

**Process**:
1. **Search for communities** where this niche congregates:
   - Reddit (r/psychotherapy, r/therapists)
   - Facebook groups
   - Forums
   - LinkedIn groups

2. **Search for spending signals**:
   - "[niche] paid $" 
   - "[niche] spent $"
   - "[niche] worth every penny"
   - "[niche] too expensive"
   - "hired [niche] consultant"

3. **Search for pain points**:
   - "[niche] frustrated"
   - "[niche] struggling with"
   - "how do I [niche]"
   - "[niche] help needed"

4. **Document findings** with URLs and quotes

**Tools**: Web Search

**Output**: `discovery_report.json` with:
- Communities found
- Spending signals (with URLs)
- Pain patterns (with URLs)
- Initial confidence assessment

---

### Phase 3: SPENDING ANALYSIS

**Your Role**: Evidence analyst quantifying willingness to pay

**Process**:
1. Review discovery findings
2. Extract concrete spending examples:
   - Dollar amounts mentioned
   - Time costs described
   - Purchase types (courses, services, tools)
3. Categorize satisfaction (happy/neutral/frustrated)
4. Identify jobs-to-be-done

**Gate 1 - Spending Evidence**:
- PASS: Found 3+ concrete spending signals with $ amounts or time costs
- FAIL: Only vague interest, no quantified spending
- ACTION: If FAIL, stop and report "Insufficient spending evidence"

**Tools**: None (analyze collected data)

**Output**: `spending_signals.json`

---

### Phase 4: PAIN MAPPING

**Your Role**: Pain researcher mapping problems

**Process**:
1. Search for specific questions being asked repeatedly
2. Identify current workarounds (what people do now)
3. Quantify consequences:
   - Time wasted
   - Money risked
   - Emotional state
4. Capture exact user language

**Gate 2 - Pain Specificity**:
- PASS: Found specific recurring question + documented workaround + quantified cost
- FAIL: Pain is vague or consequences unclear
- ACTION: If FAIL, stop and report "Pain not specific enough"

**Tools**: Web Search (targeted)

**Output**: `pain_map.json`

---

### Phase 5: COMPETITIVE ANALYSIS

**Your Role**: Competitive intelligence researcher

**Process**:
1. Search for existing solutions:
   - "[niche] course"
   - "[niche] template"
   - "[niche] service"
   - "[niche] tool"

2. Browse competitor offerings:
   - Visit sales pages
   - Note pricing
   - Identify weaknesses
   - Read reviews if available

3. Map alternatives:
   - Free resources
   - Paid courses
   - Consultants/services
   - Software tools

**Tools**: Web Search, Browser Visit

**Output**: `competitor_map.json`

---

### Phase 6: OPPORTUNITY SCORING

**Your Role**: Investment analyst making go/no-go decision

**Process**:
Score 1-5 on each dimension:

1. **Spending Clarity**: How clear is the willingness to pay?
   - 5: Multiple $500+ purchases documented
   - 3: Some $50-200 purchases
   - 1: No spending evidence

2. **Information Gap**: How strong is the knowledge need?
   - 5: Recurring unanswered questions, confusion
   - 3: Some questions but partial solutions exist
   - 1: Information readily available

3. **Urgency**: How pressing is the problem?
   - 5: Revenue-impacting, time-sensitive
   - 3: Important but not urgent
   - 1: Nice-to-have

4. **Create Feasibility**: Can we create this in 2-4 weeks?
   - 5: Clear scope, templatable
   - 3: Moderate complexity
   - 1: Too complex or vague

5. **AI Multiplier**: Can AI enhance this product?
   - 5: Strong personalization/generation opportunity
   - 3: Some AI enhancement possible
   - 1: No AI leverage

**Calculate**: Total score (max 25)

**Gate 3 - Score Threshold**:
- CREATE (proceed): Score >= 18
- PIVOT (reconsider): Score 14-17
- REJECT (stop): Score < 14

**Decision**: Use judgment - if total >= 18, proceed to build

**Tools**: None (reasoning only)

**Output**: `opportunity_score.json`

---

### Phase 7: STRATEGY (Product Brief)

**Your Role**: Product strategist defining the offer

**Process**:
1. Define target user (specific segment)
2. Choose product format based on:
   - What the pain requires (step-by-step = playbook)
   - What formats performed well historically
   - Create feasibility

3. Set pricing based on:
   - Competitor price anchors
   - Spending signals found
   - Value delivered

4. Craft core promise (transformation statement)
5. Define differentiator (why this over competitors)
6. Choose distribution channels (where target users are)

**Tools**: None (strategic reasoning)

**Output**: `product_brief.json`

---

### Phase 8: OUTLINE

**Your Role**: Content architect structuring the product

**Process**:
1. Create section-level structure
2. Map key deliverables per section
3. Ensure scope is buildable in 2-4 weeks
4. Identify artifact references (what templates/checklists needed)

**Tools**: None (planning)

**Output**: `outline.json`

---

### Phase 9: SYNTHESIS (Knowledge Base)

**Your Role**: Research synthesizer organizing facts

**Process**:
1. Transform research into structured facts
2. Note contradictions (conflicting information)
3. Mark confidence levels (high/medium/low)
4. Document key decisions made
5. List pitfalls to avoid

**Tools**: None (synthesis)

**Output**: `knowledge_base.json`

---

### Phase 10: DRAFTING

**Your Role**: Content writer creating the product

**Process**:
1. Write main product content following outline
2. Include:
   - Clear explanations
   - Step-by-step instructions
   - Real examples
   - Action items
3. Maintain useful density (no filler)
4. Write in user's language (from pain research)

**Tools**: None (writing)

**Output**: `draft_product.md`

---

### Phase 11: ARTIFACTS

**Your Role**: Template creator building support materials

**Process**:
Create at least 3 support artifacts:
- Checklists (process steps)
- Templates (fill-in-the-blank)
- Scripts (email/copy templates)
- Calculators (decision tools)
- Worksheets (exercises)

**Tools**: None (creation)

**Output**: 
- `artifact_manifest.json`
- Individual artifact files

---

### Phase 12: PERSONALIZATION (Optional)

**Your Role**: Personalization engineer

**Process**:
1. Define input fields (what user provides)
2. Design generation logic (how inputs transform outputs)
3. Specify outputs (what gets personalized)
4. Document update strategy

**Skip if**: Format doesn't benefit from personalization

**Tools**: None (specification)

**Output**: `personalization_spec.json`

---

### Phase 13: PACKAGING

**Your Role**: Product packager

**Process**:
1. Define buyer-facing product stack:
   - Main product
   - Bonuses
   - Support artifacts
2. Create package manifest
3. Define delivery method
4. Set version

**Gate 4 - Artifact Completeness**:
- PASS: Main draft exists + 3+ support artifacts + package manifest
- FAIL: Missing key components
- ACTION: If FAIL, go back and create missing artifacts

**Tools**: None (organization)

**Output**: `package_manifest.json`

---

### Phase 14: LAUNCH ASSETS

**Your Role**: Copywriter creating marketing materials

**Process**:
1. **Sales Page**:
   - Headline (problem + solution)
   - Problem agitation
   - Solution presentation
   - Features/benefits
   - Pricing
   - Guarantee
   - CTA

2. **Gumroad Listing**:
   - Short description
   - What's included
   - Who it's for

3. **Lead Magnet**:
   - Hook/headline
   - Quick win content
   - Upgrade CTA

4. **Launch Posts** (3-5):
   - Problem awareness
   - Solution reveal
   - Social proof
   - Urgency/scarcity
   - Final call

5. **FAQ**: Common questions and answers
6. **Objection Handling**: Price, time, "not for me"

**Tools**: None (copywriting)

**Output**: `launch_assets/` directory with all materials

---

### Phase 15: VALIDATION

**Your Role**: Quality assurance reviewer

**Process**:
Check all gates:
1. Spending evidence documented? (3+ signals, 2+ quantified)
2. Pain specific? (question + workaround + cost)
3. Score >= 18 and decision = CREATE?
4. Artifacts complete? (draft + 3+ support + manifest)
5. Launch ready? (audience + channels + pricing)

**Gate 5 - Launch Readiness**:
- PASS: All checks pass
- REVISE: Some issues but fixable
- FAIL: Fundamental problems

**Tools**: None (review)

**Output**: `validation_report.json`

---

### Phase 16: RETROSPECTIVE

**Your Role**: Process improvement analyst

**Process**:
1. Document what worked
2. Document what didn't work
3. Update memory files:
   - Add niche to winning_niches.json (if passed)
   - Add niche to failed_niches.json (if failed)
   - Update format performance
   - Save search patterns that worked

**Tools**: File write

**Output**: `postmortem.json`

---

## Agent Execution Modes

### Mode: DISCOVER
Stop after: Phase 2 (Discovery)  
Use when: Exploring niches without commitment

### Mode: VALIDATE
Stop after: Phase 6 (Scoring)  
Use when: Testing if a niche is viable before building

### Mode: BUILD
Stop after: Phase 13 (Packaging)  
Use when: Creating the product but not launching yet

### Mode: LAUNCH
Stop after: Phase 15 (Validation)  
Use when: Product exists, need launch assets

### Mode: FULL
Stop after: Phase 16 (Retrospective)  
Use when: Complete end-to-end creation

---

## State Management (Agent Memory)

Since you're executing this, state is your context window + files:

**In Context** (keep track of):
- Current phase
- Key findings
- Decisions made
- Score totals

**On Disk** (save after each phase):
- All JSON artifacts
- Draft content
- Launch assets

**Memory Files** (update after each run):
- `winning_niches.json`
- `failed_niches.json`
- `search_patterns.json`
- `format_performance.json`

---

## Gate Enforcement (Agent Decisions)

At each gate, explicitly state:

```
GATE 1 - Spending Evidence
Signals found: 4
Quantified: 3 ($ amounts)
Decision: PASS
Reasoning: Clear willingness to pay $200-500 documented
```

If FAIL:
```
GATE 1 - Spending Evidence
Signals found: 2
Quantified: 0
Decision: FAIL
Reasoning: Only vague interest expressed, no documented spending
ACTION: Stop pipeline, report findings to user
```

---

## Tool Usage Strategy

**Web Search** (primary research tool):
- Find communities
- Find spending signals
- Find pain points
- Find competitors

**Browser Visit** (deep dive):
- Browse competitor sales pages
- Read forum threads
- Check pricing

**File Tools** (persistence):
- Save artifacts
- Update memory
- Create run directory

---

## Example Run

**User**: "Run KPF validate mode on 'therapist insurance credentialing'"

**Agent (you)**:
1. "Starting Phase 1: Intake"
   - Validate niche: "therapist insurance credentialing" (specific enough ✓)
   - Set constraints: 3 weeks, $79-199, formats: playbook/template_library
   - Create run directory: `runs/2026-03-06_therapist-insurance-credentialing/`

2. "Phase 2: Discovery - Searching for evidence..."
   - Search: "therapist insurance credentialing paid $"
   - Search: "therapist credentialing service cost"
   - Search: "r/psychotherapy insurance panel fee"
   - Found: 3 communities, 5 spending signals, 4 pain patterns

3. "Phase 3: Spending Analysis"
   - Signal 1: "$500 for credentialing service" (r/psychotherapy)
   - Signal 2: "40 hours doing it myself" (Facebook group)
   - Signal 3: "$97 checklist saved me time"
   - **GATE 1: PASS** (3 signals, 3 quantified)

4. "Phase 4: Pain Mapping"
   - Core question: "How do I get paneled without spending months?"
   - Workaround: Hiring $500-2000 services
   - Cost: 20-40 hours or $500-2000
   - **GATE 2: PASS**

5. "Phase 5: Competitive Analysis"
   - Competitor A: $199 course (weakness: generic)
   - Competitor B: $500 service (weakness: expensive)
   - Free resources: (weakness: incomplete)

6. "Phase 6: Opportunity Scoring"
   - Spending clarity: 5 (clear $ amounts)
   - Information gap: 5 (strong confusion)
   - Urgency: 4 (revenue impact)
   - Create feasibility: 5 (templatable)
   - AI multiplier: 4 (personalization possible)
   - **Total: 23**
   - **Decision: CREATE**
   - **GATE 3: PASS**

7. "Validation complete. Opportunity confirmed."
   - Save all artifacts to run directory
   - Report: "Therapist insurance credentialing scored 23/25. Proceed to build."

---

## Advantages of Agentic KPF

1. **Real Evidence**: Actual search results, not synthetic data
2. **Current Data**: Live competitor pricing, not training data
3. **Adaptive**: Can dig deeper if findings are weak
4. **Transparent**: Every decision explained
5. **No Costs**: No API fees
6. **Human Judgment**: Can override rigid rules when justified

---

## Implementation

To execute Agentic KPF:

1. Read the phase instructions
2. Execute tools as needed
3. Document findings
4. Make gate decisions
5. Save artifacts
6. Proceed or stop based on gates

The system is now **you following a structured workflow** rather than **code calling APIs**.
