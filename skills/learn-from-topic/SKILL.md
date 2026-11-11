---
name: learn-from-topic
description: "Generate a beginner-to-intermediate study plan for any topic or technology without needing a workspace project. Use when: studying a tool, framework, language, or domain from scratch; creating a topic-based curriculum; generating hands-on Jupyter notebook lessons for topics like HELM, Kubernetes, Terraform, Python async, design patterns, DevOps, or any technical/soft-skill domain. Sources knowledge from official docs, user-provided URLs, GitHub repos, and built-in knowledge. Produces phased Jupyter notebook lessons and a capstone project."
argument-hint: "Topic name and optional resources (e.g. 'HELM — https://helm.sh/docs' or 'Python async, no docs')"
---

# Learn From Topic

Generate a structured, beginner-to-intermediate study plan for **any topic or technology** — no workspace project required. The output is a set of Jupyter notebook (`.ipynb`) lessons organized into phases, culminating in a capstone project where the learner applies everything they have learned.

## When to Use

- You want to learn a specific tool, framework, language, or domain from scratch
- You need a curriculum for a topic with no existing codebase to reference
- You want hands-on Jupyter notebooks for topics like HELM, Kubernetes, Terraform, Python async, system design, DevOps practices, software architecture, agile, etc.
- You want code-along lessons that progressively build toward a real-world application or scenario

## Difference From `learn-from-project`

| | `learn-from-project` | `learn-from-topic` |
|---|---|---|
| **Input** | Existing workspace codebase | Topic name + optional docs/URLs |
| **Discovery** | Analyzes workspace files | Sources from docs, URLs, built-in knowledge |
| **Capstone** | Rebuild the workspace project | Build a real-world scenario from scratch |
| **Scope** | Project-specific | Any topic or domain |

---

## Procedure

Follow these steps exactly, in order.

### Step 1 — Overwrite Guard

Before doing anything else, check if a `study-plan/` directory already exists in the workspace root.

- If it **does exist**, ask the user: _"A `study-plan/` directory already exists. Would you like to: (a) create a new subdirectory `study-plan/topic-<slug>/` alongside existing content, (b) overwrite everything, or (c) abort?"_
- Do **NOT** create any files until the user confirms.
- If the user says abort, stop and explain what would have been generated.
- If it does not exist, all output goes into `study-plan/topic-<slug>/` where `<slug>` is the kebab-case topic name (e.g., `study-plan/topic-helm/`).

### Step 2 — Knowledge Gathering

Collect knowledge about the topic using all available sources:

#### 2a — Parse User Input

Extract from the user's request:
- **Topic name** — the primary subject (e.g., "HELM", "Kubernetes", "Python async", "design patterns")
- **Subtopic or focus area** — any stated constraints (e.g., "HELM for Kubernetes deployments", "Python async for web scrapers")
- **Audience level** — if stated (defaults to beginner-to-intermediate)
- **Provided URLs or repos** — any documentation links, GitHub repos, or reference materials supplied by the user

If the topic is unclear or no resources are provided, ask:
> _"What topic would you like to study? You can also paste any official docs URLs, GitHub repo links, or reference materials to improve accuracy. (Optional — I can proceed with built-in knowledge if you don't have any.)"_

#### 2b — Fetch Provided Resources

If the user provided URLs or GitHub repos:
1. Fetch each URL and extract the key content (table of contents, concept list, API reference, quickstart sections).
2. Identify: core concepts, key commands/APIs, common patterns, recommended practices, official learning paths.
3. Note the **authoritative source name** for citation in notebooks (e.g., "Helm Official Docs — https://helm.sh/docs").

Regardless of whether the user provided resources:
1. Always build a comprehensive, **categorized Recommended Resources** section for the README (see Step 4).
2. Gather authoritative links across all categories: official docs, GitHub repos, cheat sheets, tutorials, practice tools, community sites, and relevant books/courses for the topic.

#### 2c — Build a Topic Knowledge Inventory

Produce a structured inventory of everything to teach. Organize into:

- **Core concepts** — the fundamental ideas the learner must understand (e.g., for HELM: charts, releases, repositories, values, templates)
- **Key skills / commands / APIs** — hands-on things the learner must be able to do (e.g., `helm install`, `helm upgrade`, `helm template`, writing `values.yaml`)
- **Common patterns** — recurring real-world usage patterns (e.g., environment-specific value overrides, chart dependencies, hooks)
- **Gotchas / best practices** — things beginners commonly get wrong
- **Prerequisites** — what the learner needs to know before starting (e.g., for HELM: basic Kubernetes concepts, `kubectl` basics)
- **Real-world capstone scenario** — a specific, realistic task that uses the full topic (e.g., for HELM: deploy a multi-service application with a custom Helm chart, environment overrides, and upgrade workflow)

### Step 3 — Phase Mapping

Map the knowledge inventory to ordered learning phases. Load [plan-guidelines.md](../learn-from-project/references/plan-guidelines.md) for sizing, ordering, and naming rules. Adapt these rules for topic-based plans:

**General ordering principle** (beginner → intermediate → applied):

1. **Foundations** — What is this topic? Why does it exist? Core terminology, mental model, environment setup, first working example.
2. **Core Mechanics** — The primary features, commands, APIs, or constructs. Cover each major concept with hands-on practice.
3. **Patterns & Composition** — How components work together. Layering, configuration, orchestration, customization, extension.
4. **Real-World Workflows** — Production-grade usage: CI/CD integration, security, troubleshooting, best practices, automation.
5. **Deployment / Operations** (if applicable) — Running in real environments: cloud, on-prem, multi-environment, monitoring.
6. **Capstone** — Full end-to-end application of the topic in a realistic scenario.

**Topic-specific phase examples:**

| Topic | Phase 1 | Phase 2 | Phase 3 | Phase 4 | Capstone |
|-------|---------|---------|---------|---------|----------|
| **HELM** | Intro, charts, install | Templates, values, hooks | Chart dependencies, OCI registries | CI/CD, versioning, security | Deploy multi-service app with custom chart |
| **Kubernetes** | Pods, deployments | Services, configmaps, secrets | Ingress, RBAC, namespaces | Monitoring, autoscaling | Full app deployment |
| **Terraform** | Providers, resources, state | Variables, modules | Workspaces, remote state | CI/CD, GitOps | Multi-environment infra |
| **Python async** | `asyncio` basics, coroutines | Tasks, event loop, gather | `aiohttp`, async DB | Testing, performance | Async web scraper / API client |
| **Design Patterns** | Creational patterns | Structural patterns | Behavioral patterns | Applying in real code | Refactor a real-world design challenge |

Adapt phases to exactly what the topic requires. Skip phases for aspects not relevant to the topic. Split thick phases into sub-phases.

Target **3–6 lessons per phase**. Each lesson must result in working code, a config file, a YAML manifest, or a demonstrable command sequence.

### Step 4 — Generate the Study Plan README

Create `study-plan/topic-<slug>/README.md` with:

- Topic name and one-line description
- Prerequisites (tools to install, accounts to create, prior knowledge assumed)
- **Recommended Resources** section (see format below — **always required**, always comprehensive and categorized)
- Table of all phases and lessons with links to the `.ipynb` files
- Estimated total lesson count and approximate time to complete
- Capstone overview (what will be built)
- How to use the notebooks (install Jupyter, run cells top-to-bottom)

#### Recommended Resources Format (REQUIRED — always include all relevant categories)

The Recommended Resources section **must always be present**, comprehensive, and organized into these categories. Include every category that is relevant to the topic; skip only categories with no applicable resources.

```markdown
## Recommended Resources

### 📋 Official Specification / Exam Guide
| Resource | URL |
|----------|-----|
| Official Docs / Spec | <url> |
| Changelog / Release Notes | <url> |

### 📚 Core Documentation
| Resource | URL |
|----------|-----|
| Getting Started Guide | <url> |
| Full Reference Docs | <url> |
| API / CLI Reference | <url> |
| Architecture Overview | <url> |

### 🎓 Training & Courses
| Resource | URL |
|----------|-----|
| Official Tutorial / Learn Path | <url> |
| Community Course (Udemy / Coursera / etc.) | <url> |
| YouTube Playlist / Conference Talks | <url> |

### 📝 Cheat Sheets & Quick Reference
| Resource | URL |
|----------|-----|
| Official Cheat Sheet | <url> |
| Community Cheat Sheet | <url> |
| Key Commands / API Summary | <url> |

### 🛠️ Key Docs by Phase/Feature
| Phase | Feature | URL |
|-------|---------|-----|
| Phase N | <feature> | <url> |

### 🧪 Practice & Sandboxes
| Resource | URL |
|----------|-----|
| Interactive Playground / Lab | <url> |
| Practice Exercises / Challenges | <url> |
| Sample Projects / Templates | <url> |

### 🏘️ Community & Support
| Resource | URL |
|----------|-----|
| Official Forum / Slack / Discord | <url> |
| GitHub Repository | <url> |
| Stack Overflow Tag | <url> |
| Blog / Newsletter | <url> |
```

**Rules for the Recommended Resources section:**
- **Always generate this section** — never omit it even when no user resources were provided.
- Use real, verified URLs sourced from fetched pages or built-in knowledge. Do not fabricate URLs.
- If a URL cannot be verified, write `— search: "<search term>"` instead of guessing.
- Populate the **Key Docs by Phase** subsection with a direct link for every major service or tool introduced in each phase.
- Include at least one free resource in every category.

### Step 5 — Generate Lesson Notebooks

For each lesson, create a Jupyter notebook at:
```
study-plan/topic-<slug>/phase-N-<slug>/lesson-N.M-<slug>.ipynb
```

Use [lesson-template.md](../learn-from-project/assets/lesson-template.md) as the structural guide for cell layout. Each notebook must:

1. **Alternate markdown and code cells** — explanation, then runnable code, then more explanation.
2. **Be runnable top-to-bottom** — imports and setup at the top, each code cell builds on the previous.
3. **Produce something tangible** — a working command output, a rendered template, a deployed resource, a written config file, a passing test. Every lesson ends with the learner having _something to show_.
4. **Include exercises** — dedicated code/bash cells with `# TODO:` or `# TASK:` comments for the learner to complete.
5. **Explain concepts in beginner-friendly language** — define every term on first use; use analogies.
6. **Cite sources** — for concepts drawn from docs, add a markdown note: _"Reference: [Source Name](URL)"_
7. **Link to next lesson** — final markdown cell points to the next notebook.

**Topic-specific notebook rules:**

- **CLI / DevOps tools** (HELM, kubectl, Terraform): Use `%%bash` magic cells or `!command` for interactive terminal exercises. For YAML/HCL content, use `%%writefile <filename>` to write files to disk so the learner can inspect them.
- **Infrastructure-as-Code topics**: Always include a "what this produces" markdown cell showing the expected state after running the commands.
- **Conceptual topics** (design patterns, architecture): Use Python (or the learner's preferred language) to implement and demonstrate patterns as runnable code.
- **Non-runnable steps** (e.g., cloud console actions, browser-based tasks): Use markdown cells with numbered instructions and screenshots described in text.

When generating `.ipynb` content:
- Use proper notebook JSON format (nbformat 4, nbformat_minor 5).
- For CLI/DevOps topics with no natural kernel language, default to `bash` kernel or `python3` with `!`/`%%bash` cells.
- Markdown cells use standard markdown (headers, bold, code fences, bullet lists).
- Code cells contain runnable code with inline comments.

### Step 6 — Generate Capstone Notebook

Create `study-plan/topic-<slug>/capstone/capstone-project.ipynb` using [capstone-template.md](../learn-from-project/assets/capstone-template.md) as the structural guide.

The capstone must:
- State the **real-world scenario objective** derived from the knowledge inventory (not "rebuild the project" — instead: a task the learner would actually do on the job)
- List every artifact to create or action to perform, in dependency order
- Provide a stub cell for each step with `# TODO:` scaffolding
- Reference the lesson where each concept was taught (e.g., _"Refer to Lesson 2.3 for template syntax"_)
- Include a verification checklist (markdown cell with checkboxes confirming the scenario is complete)
- Include **stretch goals** that extend beyond the core scenario (e.g., add CI/CD, add tests, add monitoring, deploy to cloud)

**Capstone scenario examples by topic:**

| Topic | Capstone Scenario |
|-------|------------------|
| **HELM** | Author a production-grade Helm chart for a 2-service app (frontend + backend), support dev/staging/prod value overrides, publish to OCI registry, write a CI workflow that lints + packages the chart |
| **Kubernetes** | Deploy a multi-tier application (web + DB + cache) with RBAC, secrets management, horizontal pod autoscaling, and ingress |
| **Terraform** | Provision a multi-environment (dev/prod) cloud infrastructure with a VPC, compute, managed database, and remote state backend |
| **Python async** | Build a concurrent web scraper that fetches 100+ URLs in parallel, stores results in an async-compatible database, and exposes a REST endpoint |
| **Design Patterns** | Refactor a deliberately badly-designed e-commerce order system, applying at least 5 patterns and documenting each decision |

### Step 7 — Final Summary

After generating all files, print a summary to the user:
- Topic name and scope covered
- Total phases and lessons generated
- Path to the study plan directory (e.g., `study-plan/topic-helm/`)
- Suggested starting point (first lesson of Phase 1)
- Recommended resources to bookmark (official docs, community resources)
- Reminder to install Jupyter if not already installed: `pip install notebook` or `pip install jupyterlab`

---

## Important Rules

- **Never hallucinate APIs, commands, or config syntax.** If uncertain about a specific value or option, say so in a notebook comment and point the learner to the official docs to verify.
- **Every lesson must produce something tangible.** No abstract theory-only notebooks.
- **Maintain dependency order.** A lesson should never reference a concept from a later lesson.
- **Use the learner's language level.** Beginner phases assume zero prior knowledge of the topic. Intermediate phases can assume earlier lessons were completed.
- **Notebooks must be self-contained.** Each notebook should run independently if the environment is set up (all installs and setup at the top).
- **Cite sources.** When drawing from official docs, reference the source in relevant markdown cells.
- **Adapt to the topic's primary medium.** For CLI/YAML topics, YAML and bash cells are first-class. For language topics, code cells are primary. Never force a Python-only format onto a non-Python topic.
- **Always include a comprehensive, categorized Recommended Resources section in the README.** This is mandatory for every study plan regardless of whether the user provided URLs. Populate all relevant categories with real, verified links.
