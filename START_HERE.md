# Agentic KPF - START HERE
## Implementation Package for AI Agents

---

## 👋 Welcome, Fellow Agent

This package contains everything you need to implement and execute the **Agentic Knowledge Product Factory (KPF)**—a workflow system for researching, validating, and creating knowledge products.

Unlike traditional software that calls APIs, **you** execute this system using your tools (web search, browsing, reasoning, writing).

---

## 📚 Package Contents

### Essential Reading (Read in Order)

| Document | Purpose | Read Time |
|----------|---------|-----------|
| **1. AGENTIC_README.md** | System overview and philosophy | 5 min |
| **2. AGENTIC_KPF.md** | Complete workflow documentation (16 phases) | 15 min |
| **3. AGENT_IMPLEMENTATION_GUIDE.md** | How to configure and implement | 20 min |
| **4. QUICK_REFERENCE_CARD.md** | Keep visible while executing | 2 min |

### Reference Materials

| Document | Purpose | When to Use |
|----------|---------|-------------|
| **TEMPLATE_LIBRARY.md** | Copy-paste templates for all artifacts | During execution |
| **SAMPLE_RUN_WALKTHROUGH.md** | See exactly how to execute | Before first run |
| **PROMPTS.md** | Phase-by-phase instructions | During execution |
| **AGENTIC_QUICKSTART.md** | Quick execution guide | Quick refresher |

### Original Implementation

| Directory | Contents |
|-----------|----------|
| **kpf/** | Original software implementation (reference only) |

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Understand the System

Agentic KPF is a **16-phase workflow**:

```
INTAKE → DISCOVERY → SPENDING → PAIN → COMPETITORS → SCORING →
STRATEGY → OUTLINE → SYNTHESIS → DRAFTING → ARTIFACTS →
PERSONALIZATION → PACKAGING → LAUNCH → VALIDATION → RETROSPECTIVE
```

### Step 2: Learn the Gates

5 validation checkpoints where you decide PASS/FAIL:

| Gate | Criteria | If Fail |
|------|----------|---------|
| 1 - Spending | 3+ signals, 2+ quantified | STOP |
| 2 - Pain | Question + workaround + cost | STOP |
| 3 - Score | >= 18, decision=CREATE | STOP |
| 4 - Artifacts | Draft + 3+ artifacts + manifest | Go back |
| 5 - Launch | Audience + channels + pricing | Revise |

### Step 3: Know the Modes

| User Says | Mode | Stop After |
|-----------|------|------------|
| "Discover niches" | discover | Phase 2 |
| "Validate [niche]" | validate | Phase 6 |
| "Build [niche]" | build | Phase 13 |
| "Launch [niche]" | launch | Phase 15 |
| "Full run [niche]" | full | Phase 16 |

### Step 4: Execute Your First Run

When user says: `"Validate [niche]"`

1. Create directory: `runs/YYYY-MM-DD_[niche-slug]/`
2. Execute Phase 1 (Intake)
3. Execute Phase 2 (Discovery)
4. Execute Phase 3 (Spending) → Gate 1
5. Execute Phase 4 (Pain) → Gate 2
6. Execute Phase 5 (Competitors)
7. Execute Phase 6 (Scoring) → Gate 3
8. Report results

---

## 📖 Reading Guide

### If You Have 30 Minutes

Read in this order:
1. AGENTIC_README.md (5 min)
2. AGENTIC_KPF.md (15 min)
3. QUICK_REFERENCE_CARD.md (2 min)
4. SAMPLE_RUN_WALKTHROUGH.md (8 min)

### If You Have 1 Hour

Add these:
5. AGENT_IMPLEMENTATION_GUIDE.md (20 min)
6. TEMPLATE_LIBRARY.md (10 min)

### Before Your First Run

Review:
- QUICK_REFERENCE_CARD.md (keep visible)
- TEMPLATE_LIBRARY.md (copy-paste templates)
- SAMPLE_RUN_WALKTHROUGH.md (see example)

---

## 🎯 Core Principles

### 1. Evidence > Opinion

Always search for real data. Don't generate synthetic findings.

**Good**: "Found 4 spending signals: $47 template pack (Etsy), $97 practice management template..."

**Bad**: "People probably spend around $50 on this type of product."

### 2. Gates Matter

Don't skip validation. If a gate fails, stop and report.

### 3. Be Honest

Don't inflate scores or findings. Better to catch a weak product early.

### 4. Save Everything

Save artifacts after EVERY phase. Don't batch saves.

### 5. Cite Sources

Every finding needs a URL.

---

## 🛠️ Required Tools

You MUST have:
- ✅ **Web Search** - Primary research tool
- ✅ **File Write** - Save artifacts
- ✅ **Reasoning** - Score opportunities

Optional:
- 📎 **Browser Visit** - Deep dives

---

## 📂 Directory Structure

```
/mnt/okcomputer/output/kpf/
├── START_HERE.md                    ← You are here
├── AGENTIC_README.md                ← System overview
├── AGENTIC_KPF.md                   ← Complete workflow
├── AGENT_IMPLEMENTATION_GUIDE.md    ← Implementation guide
├── QUICK_REFERENCE_CARD.md          ← Quick reference
├── TEMPLATE_LIBRARY.md              ← Copy-paste templates
├── SAMPLE_RUN_WALKTHROUGH.md        ← Example execution
├── PROMPTS.md                       ← Phase instructions
├── AGENTIC_QUICKSTART.md            ← Quick start
├── runs/                            ← Run outputs
│   └── YYYY-MM-DD_[niche-slug]/    ← Individual runs
├── memory/                          ← Persistent learning
│   ├── winning_niches.json
│   ├── failed_niches.json
│   ├── search_patterns.json
│   └── format_performance.json
└── kpf/                             ← Original software
```

---

## 🎓 Learning Path

### Beginner

1. Read AGENTIC_README.md
2. Read QUICK_REFERENCE_CARD.md
3. Execute a VALIDATE mode run
4. Review SAMPLE_RUN_WALKTHROUGH.md

### Intermediate

5. Read AGENTIC_KPF.md
6. Execute a BUILD mode run
7. Review TEMPLATE_LIBRARY.md

### Advanced

8. Read AGENT_IMPLEMENTATION_GUIDE.md
9. Execute a FULL mode run
10. Customize templates for your style

---

## ✅ Pre-Flight Checklist

Before your first run:

- [ ] Read AGENTIC_README.md
- [ ] Read QUICK_REFERENCE_CARD.md
- [ ] Understand the 5 gates
- [ ] Know the 4 execution modes
- [ ] Have TEMPLATE_LIBRARY.md ready
- [ ] Create runs/ directory
- [ ] Create memory/ directory with JSON files

---

## 🆘 Getting Help

### If You're Stuck

1. Check QUICK_REFERENCE_CARD.md
2. Review SAMPLE_RUN_WALKTHROUGH.md
3. Look at TEMPLATE_LIBRARY.md for templates
4. Search for similar examples in memory/

### Common Issues

| Issue | Solution |
|-------|----------|
| No search results | Try broader terms, related topics |
| Weak spending signals | Look for time costs, hiring patterns |
| Can't decide score | Default conservative, document why |
| Gate failed | Stop and report clearly to user |

---

## 🎯 Success Metrics

A successful run:
- ✅ All phases executed
- ✅ Gates explicitly decided
- ✅ All artifacts saved
- ✅ Evidence cited with URLs
- ✅ Clear recommendation
- ✅ Memory files updated

---

## 🚀 Your First Command

Ready? Try this:

```
User: "Validate productivity system for developers"

You: [Execute phases 1-6]
      [Report opportunity score]
      [Give recommendation]
```

---

## 📞 Remember

> **Evidence > Opinion**
> **Gates Matter**
> **Be Honest**
> **Save Everything**

---

## 📄 Document Index

| Document | What It Contains |
|----------|------------------|
| START_HERE.md | This file - your entry point |
| AGENTIC_README.md | System overview and usage |
| AGENTIC_KPF.md | Complete 16-phase workflow |
| AGENT_IMPLEMENTATION_GUIDE.md | How to configure and implement |
| QUICK_REFERENCE_CARD.md | Quick reference (print this) |
| TEMPLATE_LIBRARY.md | Copy-paste artifact templates |
| SAMPLE_RUN_WALKTHROUGH.md | Example execution |
| PROMPTS.md | Phase-by-phase instructions |
| AGENTIC_QUICKSTART.md | Quick start guide |

---

**Ready to execute? Start with AGENTIC_README.md.**

*Good luck!*
