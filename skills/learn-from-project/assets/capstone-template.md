# Capstone Notebook Template

Structural guide for generating the capstone `.ipynb` notebook. The capstone ties all lessons together by having the learner rebuild the entire project from scratch.

---

## Notebook Metadata

Same as lesson notebooks — match the project's primary language kernel.

---

## Cell Sequence

### Cell 1 — Title & Objective (Markdown)

```markdown
# Capstone Project — Rebuild {{Project Name}}

**Level: Intermediate**

## Objective

Rebuild the **{{project_name}}** application from scratch, applying everything you've learned across all {{N}} phases. You will create every file in the project, in the correct dependency order, and verify the application works end-to-end.

### What You'll Build
{{One paragraph describing the finished application and what it does.}}

### Rules
- Work through the steps in order — each step depends on the ones before it.
- Write the code yourself. Refer back to lessons if you get stuck, but try first.
- Run the verification check after each section before moving on.
- The stretch goals are optional — tackle them after the core project is complete.
```

### Cell 2 — Prerequisites & Setup (Markdown)

```markdown
## Prerequisites

Before starting, make sure you have:

- [ ] {{tool_1}} installed (e.g., Python 3.10+)
- [ ] {{tool_2}} installed (e.g., Docker Desktop)
- [ ] {{account_1}} set up (e.g., Groq API key)
- [ ] A fresh, empty project directory created
- [ ] A virtual environment activated (if applicable)

**Estimated time:** {{X}} hours
```

### Cell 3 — Setup Code (Code)

```python
# Capstone Setup
# Create the project directory structure

import os

# TODO: Create all directories needed for the project
# Hint: the project uses this structure:
# {{directory_tree}}
```

### Cells 4–N — Build Steps (repeating pattern of Markdown + Code)

For each file or group of related files to create:

**Markdown cell:**
```markdown
## Step {{X}}: {{File or Component Name}}

**File(s):** `{{file_path}}`
**Lesson reference:** Lesson {{N.M}} — {{Lesson Title}}

{{Brief reminder of what this file does and why it's needed. Do NOT re-teach the concept — just enough context to jog the learner's memory.}}
```

**Code cell:**
```python
# Step {{X}}: Create {{file_path}}
# TODO: Implement {{component_name}}
#
# Requirements:
# - {{requirement_1}}
# - {{requirement_2}}
# - {{requirement_3}}

{{minimal_scaffolding — imports and class/function signatures only}}
```

> **Rules for capstone code cells:**
> - Provide LESS scaffolding than lesson exercises — the learner should recall the implementation.
> - Include the function/class signatures but NOT the body.
> - List requirements as comments so the learner knows what to implement.
> - Group small related files (e.g., all `__init__.py` files) into one step.

### Verification Checkpoint Cells (after each major section)

**Markdown cell:**
```markdown
### Checkpoint {{X}}: Verify {{section_name}}

Run the cell below to verify your implementation so far.
```

**Code cell:**
```python
# Checkpoint {{X}}: Verify {{section_name}}
{{import_and_test_code}}

# Expected output: {{expected_output}}
print("✅ Checkpoint {{X}} passed!" if {{condition}} else "❌ Check your implementation")
```

### Cell N+1 — Final Verification Checklist (Markdown)

```markdown
## Verification Checklist

Confirm each item before considering the capstone complete:

- [ ] All project files created and importable without errors
- [ ] {{primary_command}} starts the application successfully
- [ ] {{core_feature_1}} works end-to-end
- [ ] {{core_feature_2}} works end-to-end
- [ ] {{output_artifact}} is generated correctly (e.g., CSV export, API response)
- [ ] Docker image builds successfully with `docker build -t {{image_name}} .`
- [ ] Container runs and serves the application on the expected port
- [ ] {{any_additional_verification}}
```

### Cell N+2 — Stretch Goals (Markdown)

```markdown
## Stretch Goals

Completed the core project? Try these extensions:

1. **{{stretch_1_title}}** — {{description}}
2. **{{stretch_2_title}}** — {{description}}
3. **{{stretch_3_title}}** — {{description}}
4. **{{stretch_4_title}}** — {{description}}

These go beyond what the original project implements and will deepen your understanding.
```

### Cell N+3 — Congratulations (Markdown)

```markdown
---

## Congratulations! 🎉

You've rebuilt **{{project_name}}** from scratch. You've demonstrated proficiency in:

{{bulleted_list_of_skills_covered_across_all_phases}}

**What's next?**
- Review any lessons you found challenging
- Attempt the stretch goals above
- Apply this pattern to learn from other projects using `/learn-from-project`
```

---

## Design Notes

### File ordering strategy
Use the project's import/dependency graph to determine the order:
1. **Zero-dependency files first** — `__init__.py`, config, logging, exceptions
2. **Data models** — schemas, types, interfaces
3. **Integration code** — API clients, database connections
4. **Business logic** — generators, processors, services (depend on models + integration)
5. **UI / entry point** — the main application file (depends on everything)
6. **Infrastructure** — Dockerfile, manifests, CI configs (depend on the whole project)

### Scaffolding depth
| Capstone section | Scaffolding level |
|-----------------|-------------------|
| Directory structure | Full (give the tree) |
| Config / logging / exceptions | Signatures + requirements list |
| Data models | Class name + field names, no implementations |
| Core logic | Function/method signatures only |
| UI / entry point | High-level flow comments only |
| Docker / K8s | Empty file with requirement comments |

### Checkpoint frequency
- After Phase 1 files: verify imports work
- After Phase 2 files: verify models can be instantiated
- After Phase 3 files: verify core logic runs (e.g., generate a question)
- After Phase 4 files: verify the full UI runs
- After Phase 5 files: verify Docker build succeeds
- Final: verify end-to-end functionality
