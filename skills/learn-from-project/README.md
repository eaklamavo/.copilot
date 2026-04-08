# learn-from-project

A portable Copilot skill that analyzes any project workspace and generates a beginner-to-intermediate study plan as Jupyter notebooks.

## Skill Structure

```
C:\Users\eaklamav\.copilot\skills\learn-from-project\
├── SKILL.md                        # Main skill — 7-step procedure with overwrite guard
├── references/
│   └── plan-guidelines.md          # Tech-to-phase mapping for Python, Node, Go, Java, Rust, Ruby, .NET
└── assets/
    ├── lesson-template.md          # Notebook cell sequence guide (markdown ↔ code alternation)
    └── capstone-template.md        # Capstone notebook structure with scaffolding depth rules
```

## How It Works

1. Type `/learn-from-project` in any Copilot chat to invoke it
2. It also auto-discovers when you ask about study plans, curricula, or learning from a codebase
3. **Step 1** checks if `study-plan/` exists and asks before overwriting
4. **Steps 2–3** analyze the workspace and map tech to phases
5. **Steps 4–6** generate `README.md` + `.ipynb` lesson notebooks + capstone notebook
6. Lessons alternate markdown explanation cells with runnable code cells, exercises use `# TODO:` stubs
7. The Study Buddy project is baked into `plan-guidelines.md` as a reference exemplar

## Scope

Since it's at the user level (`~/.copilot/skills/`), it's available in every workspace without copying anything.
