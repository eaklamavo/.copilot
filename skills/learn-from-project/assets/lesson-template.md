# Lesson Notebook Template

Structural guide for generating each `.ipynb` lesson notebook. This describes the cell sequence and content patterns the agent should follow when creating lesson files.

---

## Notebook Metadata

```json
{
  "kernelspec": {
    "display_name": "{{language_display_name}}",
    "language": "{{language}}",
    "name": "{{kernel_name}}"
  },
  "language_info": {
    "name": "{{language}}"
  }
}
```

For Python projects, use:
```json
{
  "kernelspec": {
    "display_name": "Python 3",
    "language": "python",
    "name": "python3"
  },
  "language_info": {
    "name": "python",
    "version": "3.10.0"
  }
}
```

---

## Cell Sequence

### Cell 1 — Title & Objectives (Markdown)

```markdown
# Lesson {{N.M}} — {{Title}}

**Level: {{Beginner|Intermediate}}**

## Learning Objectives

By the end of this lesson, you will be able to:

- {{objective_1}}
- {{objective_2}}
- {{objective_3}}

**Project file(s) produced:** `{{file_path}}`
```

### Cell 2 — Concept Explanation (Markdown)

```markdown
## Concepts

{{Explain the core concepts in beginner-friendly language. Define every technical term on first use. Use analogies where helpful.}}

### {{Sub-concept 1}}

{{Explanation with a small illustrative example if needed.}}

### {{Sub-concept 2}}

{{Explanation.}}
```

### Cell 3 — Setup / Imports (Code)

```python
# Lesson {{N.M}} — {{Title}}
# Setup: install and import required packages

{{import_statements}}
```

> **Rule:** Only import what this lesson needs. If a package hasn't been covered in a prior lesson, add a `!pip install {{package}}` line (commented out with a note to run if needed).

### Cells 4–N — Code-Along Steps (alternating Markdown + Code)

For each logical step in the code-along:

**Markdown cell:**
```markdown
## Code-Along: Step {{X}} — {{Step Title}}

{{Explain what this step does, why it's needed, and how it connects to the overall project. Point out any patterns or best practices.}}
```

**Code cell:**
```python
# Step {{X}}: {{brief description}}
{{code_that_produces_part_of_the_project_file}}
```

> **Rules:**
> - One code cell per logical step (not one cell per line).
> - Each code cell should be runnable after executing all cells above it.
> - Use inline comments for non-obvious lines.
> - When the lesson produces a project file, the final code-along cell should either:
>   - Use `%%writefile {{path}}` magic to write the file, OR
>   - Show the complete file content and instruct the learner to save it manually.

### Cell N+1 — Exercise Description (Markdown)

```markdown
## Exercise

{{Clear description of what the learner should do. Be specific about the expected input and output.}}

**Your task:**
1. {{step_1}}
2. {{step_2}}
3. {{step_3}}

**Expected result:** {{what_success_looks_like}}
```

### Cell N+2 — Exercise Stub (Code)

```python
# Exercise: {{exercise_title}}
# TODO: {{description_of_what_to_implement}}

{{scaffolding_code_with_TODO_placeholders}}

# Test your implementation:
{{test_or_assertion_code}}
```

> **Rules:**
> - Provide enough scaffolding that the learner knows where to write code.
> - Include a test/assertion at the bottom so learners can verify correctness.
> - The `# TODO:` comment must describe WHAT to do, not HOW (unless the learner hasn't learned the relevant concept yet).

### Cell N+3 — Key Takeaways (Markdown)

```markdown
## Key Takeaways

- {{takeaway_1}}
- {{takeaway_2}}
- {{takeaway_3}}
```

### Cell N+4 — Next Lesson Link (Markdown)

```markdown
---

**Next:** [Lesson {{N.M+1}} — {{Next Title}}](./lesson-{{N.M+1}}-{{next_slug}}.ipynb)
```

---

## Variations

### For non-code topics (Docker, Kubernetes, CI/CD)

Replace code cells with:
- `%%bash` magic cells for terminal commands that can run in the notebook
- `%%writefile` cells for creating Dockerfiles, YAML manifests, etc.
- Markdown cells with fenced ``` blocks labeled "**Run in your terminal:**" for commands that must run outside the notebook (e.g., `docker build`, `kubectl apply`)

Example writefile cell:
```python
%%writefile Dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install -e .
CMD ["python", "app.py"]
```

Example terminal command in markdown:
```markdown
**Run in your terminal:**
```bash
docker build -t my-app:v1 .
docker run -p 8080:8080 my-app:v1
```
```

### For lessons covering multiple small files

If a lesson produces several small files (e.g., `__init__.py` files, config files):
- Use one `%%writefile` cell per file
- Group related files with a markdown cell introducing each group

### First lesson of each phase

Include an additional markdown cell after the title:
```markdown
## Phase {{N}} Overview

This phase covers {{brief_description}}. By the end of this phase, you will have built:
{{file_list}}

### Prerequisites
- {{prerequisite_lessons_completed}}
- {{tools_to_have_installed}}
```
