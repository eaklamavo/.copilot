---
name: learn-from-project
description: "Generate a beginner-to-intermediate study plan from any project. Use when: creating a curriculum, learning from a codebase, building a code-along course, generating lessons, creating a capstone project, rebuilding a project step-by-step. Analyzes workspace tech stack and produces Jupyter notebook lessons."
argument-hint: "Target audience level and focus areas (e.g. 'beginner Python developer, focus on API layer')"
---

# Learn From Project

Generate a structured, beginner-to-intermediate study plan by analyzing the current workspace project. The output is a set of Jupyter notebook (`.ipynb`) lessons organized into phases, culminating in a capstone project that mirrors rebuilding the workspace project from scratch.

## When to Use

- You want to learn how a project works by rebuilding it step-by-step
- You need to create a teaching curriculum from an existing codebase
- You want code-along Jupyter notebooks that progressively build up to a working project
- You want a capstone project that ties all lessons together

## Procedure

Follow these steps exactly, in order.

### Step 1 — Overwrite Guard

Before doing anything else, check if a `study-plan/` directory already exists in the workspace root.

- If it **does exist**, ask the user: _"A `study-plan/` directory already exists. Would you like to: (a) overwrite it, (b) merge new content alongside existing files, or (c) abort?"_
- Do **NOT** create any files until the user confirms.
- If the user says abort, stop and explain what would have been generated.
- If it does not exist, proceed.

### Step 2 — Discovery

Thoroughly explore the workspace to understand the project:

1. **Read the README** (if present) for project purpose and setup instructions.
2. **Read dependency files** to identify the tech stack:
   - Python: `requirements.txt`, `Pipfile`, `pyproject.toml`, `setup.py`, `setup.cfg`
   - Node.js: `package.json`
   - Go: `go.mod`
   - Rust: `Cargo.toml`
   - Java: `pom.xml`, `build.gradle`
   - Ruby: `Gemfile`
   - .NET: `*.csproj`, `*.sln`
3. **Read deployment/infra files**: `Dockerfile`, `docker-compose.yml`, `Jenkinsfile`, `manifests/`, `.github/workflows/`, `terraform/`, `Makefile`
4. **Read the source tree**: list all directories and files to understand the architecture (modules, layers, entry points).
5. **Read key source files**: entry point(s), configuration, models/schemas, core business logic, utilities, tests.

Produce a mental inventory of:
- **Primary language** and version
- **Frameworks** (web, CLI, data, ML, etc.)
- **External services/APIs** (databases, LLM providers, message queues, etc.)
- **Data models** (ORM, Pydantic, TypeScript interfaces, etc.)
- **Deployment tech** (Docker, Kubernetes, serverless, CI/CD)
- **Testing framework** (if present)
- **Configuration approach** (env vars, config files, etc.)

### Step 3 — Phase Mapping

Map discovered technologies to ordered learning phases. Load [plan-guidelines.md](./references/plan-guidelines.md) for detailed heuristics.

**General ordering principle** (beginner → intermediate):

1. **Language Foundations** — stdlib, environment setup, project structure, packaging, config, logging, error handling
2. **Data Models & Core Logic** — schemas, validation, ORM, type systems, business rules
3. **Integration Layer** — external APIs, databases, LLM clients, message queues, SDKs
4. **Framework / UI** — web framework, CLI, frontend, templating, routing, state management
5. **Deployment & Infrastructure** — Docker, CI/CD, Kubernetes, cloud deploy
6. **Capstone** — full project rebuild from scratch

Adapt the number of phases and their content to what the project actually uses. Skip phases for tech the project doesn't use. Add sub-phases for complex areas.

Target **3–6 lessons per phase**. Each lesson should produce one or more actual project files.

### Step 4 — Generate the Study Plan README

Create `study-plan/README.md` with:
- Project name and one-line description
- Prerequisites (tools to install, accounts to create, prior knowledge assumed)
- Table of all phases and lessons with links to the `.ipynb` files
- Estimated total lesson count
- How to use the notebooks (install Jupyter, run cells top-to-bottom)

### Step 5 — Generate Lesson Notebooks

For each lesson, create a Jupyter notebook (`.ipynb`) at:
```
study-plan/phase-N-<slug>/lesson-N.M-<slug>.ipynb
```

Use [lesson-template.md](./assets/lesson-template.md) as the structural guide for cell layout. Each notebook must:

1. **Alternate markdown and code cells** — explanation, then runnable code, then more explanation.
2. **Be runnable top-to-bottom** — imports at the top, each code cell builds on the previous.
3. **Produce an actual project file** — the code-along steps write the same code that exists in the workspace project.
4. **Include exercises** — dedicated code cells with `# TODO:` comments for the learner to complete.
5. **Explain concepts in beginner-friendly language** — avoid jargon without defining it first.
6. **Link to next lesson** — final markdown cell points to the next notebook.

When generating `.ipynb` content:
- Use proper notebook JSON format (nbformat 4, nbformat_minor 5).
- Set `kernelspec` to match the project's primary language.
- Markdown cells use standard markdown (headers, bold, code fences, bullet lists).
- Code cells contain runnable code with inline comments.
- For non-code topics (Docker, K8s, CI), use markdown cells with command examples in fenced code blocks, and code cells with `%%bash` magic or `!` shell commands where appropriate. If shell magic is not applicable, use markdown cells with ``` fenced commands and clearly label them as "run in your terminal".

### Step 6 — Generate Capstone Notebook

Create `study-plan/capstone/capstone-project.ipynb` using [capstone-template.md](./assets/capstone-template.md) as the structural guide.

The capstone must:
- State the objective: rebuild the entire project from scratch
- List every file to create, in dependency order (files with no internal dependencies first)
- Provide a code cell stub for each file with `# TODO:` scaffolding
- Include a verification checklist (markdown cell with checkboxes)
- Include stretch goals for learners who finish early

### Step 7 — Final Summary

After generating all files, print a summary to the user:
- Total phases and lessons generated
- Path to the study plan directory
- Suggested starting point (first lesson of Phase 1)
- Reminder to install Jupyter if not already installed

## Important Rules

- **Never hardcode a specific tech stack.** Always derive phases from what you discover in the workspace.
- **Every lesson must map to real project files.** No abstract exercises disconnected from the project.
- **Maintain dependency order.** A lesson should never reference code from a later lesson.
- **Code-along code must match the project.** The code the learner writes should be the same code (or functionally equivalent) to what exists in the workspace.
- **Use the learner's language level.** Beginner phases assume no prior knowledge of the framework. Intermediate phases can assume earlier lessons were completed.
- **Notebooks must be self-contained.** Each notebook should run independently with only the standard project dependencies installed.
