---
name: exam-prep
description: "Generate hands-on project-based exam prep from an official exam guide. Use when: certification study, exam preparation, project-based learning, building a capstone project, generating lab exercises, converting exam objectives into projects. Works for any cert: AWS, Azure, GCP, Kubernetes, CKA, CKAD, CKS, CompTIA, HashiCorp, and more. Produces one Jupyter notebook mini-project per exam domain plus a final capstone notebook."
argument-hint: "Paste exam guide text, a URL, or attach the exam guide file. Optionally specify depth: quick | standard | deep (default: deep)"
---

# Exam Prep

Convert any official exam guide into a structured, hands-on, project-based study plan. Produces one Jupyter notebook per exam domain (mini-project + lab exercises) and a final capstone notebook that ties all domains together.

## When to Use

- You have an official exam guide, candidate handbook, or exam objectives page and want to build a hands-on study plan from it
- You want project-based learning instead of passive reading or flashcard drilling
- You want a capstone project that exercises every domain in a single realistic scenario
- You are prepping for any cloud, DevOps, sysadmin, data, or developer certification

## Depth Levels

| Depth | Exercises per domain | Capstone |
|---|---|---|
| `quick` | 1 exercise | Single scenario, no stretch goals |
| `standard` | 3 exercises | Multi-milestone scenario |
| `deep` *(default)* | 5 exercises + stretch goals | Full scenario with bonus challenges per milestone |

## Procedure

Follow these steps exactly, in order.

---

### Step 1 — Overwrite Guard

Before creating any files, check if a `<exam-code>-prep/` directory already exists in the workspace root (e.g., `saa-c03-prep/`, `az-900-prep/`). You won't know the exam code until Step 2, so hold this check until after parsing.

- If the directory **exists**: ask the user — *"A `<exam-code>-prep/` directory already exists. Would you like to: (a) overwrite it, (b) merge new content alongside existing files, or (c) abort?"*
- Do **NOT** create any files until the user confirms.
- If abort: stop and describe what would have been generated without creating anything.
- If merge: skip generating any notebook that already exists; only create missing ones.
- If the directory does **not** exist: proceed immediately.

---

### Step 2 — Parse the Exam Guide

Accept the exam guide in any of these forms:
- **Pasted text**: content included directly in the chat message
- **URL**: fetch the page and extract the exam objectives section
- **Attached file**: read the file (PDF text, markdown, or plain text)

From the content, extract and record:
1. **Exam name** (e.g., "AWS Certified Solutions Architect – Associate")
2. **Cert code** (e.g., `SAA-C03`) — used for the output folder name; normalize to lowercase with hyphens (e.g., `saa-c03-prep/`)
3. **Provider** (e.g., AWS, Microsoft, CNCF, CompTIA)
4. **Domains / sections** — in order, each with:
   - Domain name
   - Weighting (% of exam) if listed
   - Sub-objectives / task statements
5. **Exam details** (if present): number of questions, passing score, exam duration

If the exam code cannot be determined, ask the user: *"What is the exam code or short name? (e.g., SAA-C03, AZ-900, CKA)"*

---

### Step 3 — Language Detection

Select the primary language for all lab code cells based on exam context:

| Exam type | Primary language |
|---|---|
| Cloud platform (AWS, Azure, GCP), data, ML, developer | **Python** (use provider SDK where applicable: boto3, azure-sdk, google-cloud) |
| Sysadmin, ops, networking, infrastructure, Linux | **Bash / shell** (use `%%bash` magic or `!` prefix in code cells) |
| Kubernetes / container orchestration | **Bash / shell** + YAML manifests in fenced code blocks |
| Multi-domain exams with both types | Use the language most appropriate per domain; note in each notebook header |

Record the detected language. It will be noted in the `README.md`.

---

### Step 4 — Generate Output Folder and README

Create the output directory: `<exam-code>-prep/` in the workspace root.

Create `<exam-code>-prep/README.md` with:
- Exam name, cert code, provider
- Detected primary language for labs
- Depth level in use
- Domain map table: domain number, domain name, % weighting (if known), linked notebook filename
- Capstone notebook link
- Prerequisites: tools to install (Python, Jupyter, relevant SDK/CLI, kubectl, etc.)
- How to use: *"Open notebooks in order. Run all cells top-to-bottom. Complete the TODO exercises before moving to the next notebook."*
- Estimated study time per depth level
- **Recommended Resources** section — comprehensive and categorized (see format below; always required)

#### Recommended Resources Format (REQUIRED — always include all relevant categories)

The Recommended Resources section **must always be present** in every generated README, organized by category. Include every category relevant to the exam; skip only categories with no applicable resources.

```markdown
## Recommended Resources

### 📋 Official Exam Resources
| Resource | URL |
|----------|-----|
| Official Exam Guide | <url> |
| Official Exam Blueprint / Objectives | <url> |
| Candidate Handbook | <url> |
| Sample Questions | <url> |

### 📚 Official Documentation
| Resource | URL |
|----------|-----|
| Primary Technology Docs | <url> |
| CLI / API Reference | <url> |
| Architecture / Design Guides | <url> |

### 🎓 Training & Courses
| Resource | URL |
|----------|-----|
| Official Training / Learning Path | <url> |
| Recommended Course (Udemy / Coursera / A Cloud Guru / etc.) | <url> |
| YouTube Playlist / Conference Talks | <url> |

### 📝 Cheat Sheets & Quick Reference
| Resource | URL |
|----------|-----|
| Community Cheat Sheet | <url> |
| Key Commands / Concepts Summary | <url> |

### 🛠️ Key Docs by Exam Domain
| Domain | Topic | URL |
|--------|-------|-----|
| Domain N | <topic> | <url> |

### 🧪 Practice Exams & Labs
| Resource | URL |
|----------|-----|
| Official Practice Exam | <url> |
| Community Practice Tests | <url> |
| Hands-on Labs / Sandboxes | <url> |

### 🏘️ Community & Support
| Resource | URL |
|----------|-----|
| Official Forum / Slack / Discord | <url> |
| GitHub Study Resources | <url> |
| Study Group / Subreddit | <url> |
```

**Rules:**
- Always generate this section — never omit it.
- Use real, verified URLs sourced from fetched exam guide pages and built-in knowledge.
- If a URL cannot be verified, write `— search: "<search term>"` rather than guessing.
- Populate **Key Docs by Exam Domain** with a direct link for every major service or topic covered in each domain notebook.

---

### Step 5 — Generate Per-Domain Notebooks

For each domain, create one notebook:

```
<exam-code>-prep/<N>-<domain-slug>.ipynb
```

Where `<N>` is the domain number (01, 02, …) and `<domain-slug>` is a lowercase hyphenated version of the domain name (e.g., `01-security-identity-compliance.ipynb`).

Each notebook must contain these sections **in order**:

#### 1. Title cell (markdown)
```
# Domain <N>: <Domain Name>
**Exam**: <Exam Name> (<Cert Code>)  
**Weighting**: <X>% of exam  
**Depth**: <depth level>
```

#### 2. Domain overview (markdown)
- What this domain covers
- Why it matters for the exam (what the exam tests you on)
- Key services, tools, or concepts to know

#### 3. Key concepts (markdown + code)
For each major sub-objective:
- One markdown cell explaining the concept in plain language
- One runnable code cell demonstrating it (or a `%%bash` cell with CLI commands)
- Inline comments in code cells explaining each step

#### 4. Mini hands-on project (markdown header, then alternating markdown + code cells)
A small, self-contained real-world scenario scoped to this domain. The project should:
- Be completable in 15–30 minutes (`quick`/`standard`) or 30–60 minutes (`deep`)
- Produce tangible output (a deployed resource, a script that runs, a config that applies)
- Reference the specific sub-objectives it covers (markdown cell at the start)

#### 5. Lab exercises (code cells with scaffolding)
One code cell per exercise, each with:
- A markdown cell above it: exercise title, objective, what the learner should produce
- A code cell with `# TODO:` scaffolding — partial code that the learner must complete
- A comment at the end: `# Expected output: <description>`

Exercise count by depth: `quick`=1, `standard`=3, `deep`=5.

For `deep` depth, add one extra code cell per exercise marked `# STRETCH GOAL:` with a more advanced variant.

#### 6. Self-assessment (markdown)
5 exam-style questions for the domain (multiple choice or short answer). Do NOT include answers inline — put answers in a collapsed markdown cell or a separate `## Answers` section at the bottom.

#### 7. Navigation (markdown)
```
---
**Next**: [Domain <N+1>: <Name>](./<N+1>-<slug>.ipynb)  
**Back**: [README](./README.md)
```
Last domain links to the capstone instead.

#### Notebook format rules
- Use proper nbformat 4 / nbformat_minor 5 JSON
- Set `kernelspec` to `python3` for Python notebooks; `bash` for shell-only notebooks
- All code cells must be runnable top-to-bottom with only standard dependencies installed
- For non-runnable operations (e.g., AWS console steps), use markdown cells with numbered steps and fenced code blocks labeled *"run in your terminal"*
- Never reference a later notebook's code from an earlier one

---

### Step 6 — Generate Capstone Notebook

Create `<exam-code>-prep/00-capstone.ipynb`.

The capstone must:

#### Opening (markdown)
- Title: `# Capstone Project: <Exam Name>`
- Scenario description: a realistic, end-to-end project that a professional in this role would actually build (e.g., for AWS SAA: a multi-tier web application with HA, security, storage, and monitoring)
- List of domains exercised and which milestone covers each
- Prerequisites: complete all domain notebooks first
- Estimated time by depth: `quick`=1–2 hrs, `standard`=3–4 hrs, `deep`=5–8 hrs

#### Milestones (one section per domain, in domain order)
Each milestone:
- Markdown header: `## Milestone <N>: <Domain Name>`
- Brief context connecting the domain skill to the overall scenario
- 1–3 code cells (scaffolded with `# TODO:`) building the relevant component
- Verification step: a code or bash cell that tests the component works

#### Integration section
- Markdown: how all components connect
- Code cells that wire the milestones together into a working whole

#### Stretch goals (depth `deep` only)
A markdown cell listing 3–5 bonus challenges that extend the capstone beyond exam objectives into real production concerns.

#### Final verification checklist (markdown)
Checkbox list of everything that should be working at the end.

---

### Step 7 — Final Summary

After all files are generated, print a summary:
- Exam name and cert code
- Output folder path
- Number of domain notebooks generated
- Primary language used for labs
- Depth level applied
- Suggested starting point: first domain notebook
- Reminder: install Jupyter (`pip install jupyterlab`) and any required SDKs/CLIs before running notebooks

---

## Important Rules

- **Never skip the overwrite guard.** Always check before writing files.
- **Derive everything from the exam guide.** Do not hardcode domain names, counts, or weightings — read them from the provided guide.
- **Every lab must be scoped to the domain.** No exercises that require knowledge from a later domain (except the capstone).
- **Notebooks must be self-contained.** Each domain notebook runs independently. The capstone may import/reference results from domain notebooks but must clearly state this as a prerequisite.
- **Keep code cells runnable.** If a step requires a live cloud account or kubectl cluster, add a markdown note saying so and provide a local simulation alternative where possible (e.g., LocalStack for AWS, kind for Kubernetes).
- **Match the real exam.** Sub-objectives, task statements, and weightings must come from the parsed guide — not invented.
