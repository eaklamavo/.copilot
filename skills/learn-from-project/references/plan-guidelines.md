# Plan Guidelines — Tech-to-Phase Mapping & Design Rules

Reference document loaded by the `learn-from-project` skill during phase mapping (Step 3).

---

## Tech-Stack-to-Phase Mapping

Use these heuristics to assign discovered technologies to phases. Adapt to what the project actually uses — skip irrelevant rows, combine thin phases, split thick ones.

### Phase 1 — Language Foundations

| Stack | Topics to Cover |
|-------|----------------|
| **Python** | Virtual environments, pip, project structure, `__init__.py`, `os` module, `dotenv`, class-based config, `logging` module, custom exceptions, `setuptools`/`pyproject.toml` packaging |
| **Node.js** | `nvm`/`node`, `npm`/`yarn`/`pnpm`, `package.json`, project structure, ES modules vs CommonJS, `dotenv`, `winston`/`pino` logging, custom error classes, `tsconfig.json` (if TS) |
| **Go** | `go mod init`, project layout (`cmd/`, `internal/`, `pkg/`), environment variables, `log` package, custom error types, `Makefile` |
| **Java** | JDK setup, Maven/Gradle, project layout (`src/main/java`), `application.properties`/`application.yml`, SLF4J/Logback logging, custom exceptions |
| **Rust** | `rustup`, `cargo init`, `Cargo.toml`, module system (`mod`, `use`), `dotenv`, `log`/`env_logger` crates, custom error types with `thiserror` |
| **Ruby** | `rbenv`/`rvm`, `Gemfile`/`Bundler`, project layout, `dotenv`, `Logger`, custom exceptions |
| **.NET/C#** | `dotnet` CLI, `.csproj`, project structure, `appsettings.json`, `ILogger`, custom exceptions |

### Phase 2 — Data Models & Core Logic

| Stack | Topics to Cover |
|-------|----------------|
| **Pydantic** (Python) | `BaseModel`, `Field`, `@validator`, `@field_validator`, type annotations, nested models, custom validators |
| **SQLAlchemy / Django ORM** | Model definitions, relationships, migrations, queries |
| **TypeScript interfaces / Zod** | Type definitions, runtime validation, schema composition |
| **Go structs** | Struct definitions, JSON tags, validation libraries |
| **JPA / Hibernate** | Entity classes, annotations, relationships |
| **Serde** (Rust) | Derive macros, serialization/deserialization, custom implementations |
| **ActiveRecord** (Ruby) | Model definitions, validations, associations, migrations |

### Phase 3 — Integration Layer

| Technology | Topics to Cover |
|-----------|----------------|
| **LLM APIs** (OpenAI, Groq, Anthropic) | API keys, client setup, prompts, structured output parsing, retry logic |
| **LangChain** | Prompt templates, output parsers, chains, chat models |
| **REST API clients** | HTTP requests, authentication, error handling, response parsing |
| **Databases** (PostgreSQL, MongoDB, Redis) | Connection setup, CRUD operations, connection pooling |
| **Message Queues** (RabbitMQ, Kafka, SQS) | Producer/consumer patterns, message serialization |
| **Cloud SDKs** (AWS, GCP, Azure) | Authentication, service clients, common operations |

### Phase 4 — Framework / UI

| Framework | Topics to Cover |
|-----------|----------------|
| **Streamlit** | `st.title`, sidebar, widgets (selectbox, text_input, number_input, button, radio), session state, rerun pattern, file download, data display |
| **Flask** | Routes, templates (Jinja2), request handling, blueprints, error handlers |
| **FastAPI** | Path operations, request/response models, dependency injection, middleware |
| **Express.js** | Routes, middleware, request/response, error handling, template engines |
| **Django** | Views, URL routing, templates, forms, admin |
| **React / Next.js** | Components, state, props, hooks, routing, data fetching |
| **CLI** (Click, Cobra, clap) | Commands, arguments, options, help text, output formatting |

### Phase 5 — Deployment & Infrastructure

| Technology | Topics to Cover |
|-----------|----------------|
| **Docker** | Images vs containers, Dockerfile (`FROM`, `ENV`, `WORKDIR`, `RUN`, `COPY`, `EXPOSE`, `CMD`), `.dockerignore`, build, run, port mapping, env vars, best practices (slim images, layer caching, `--no-cache-dir`) |
| **Docker Compose** | `docker-compose.yml`, multi-service setup, volumes, networks, environment files |
| **Kubernetes** | Pods, Deployments, Services, Secrets, ConfigMaps, manifests, `kubectl` commands, Minikube for local |
| **CI/CD** (GitHub Actions, Jenkins, GitLab CI) | Pipeline definition, stages, triggers, build/test/deploy steps |
| **Terraform / IaC** | Providers, resources, variables, state, plan/apply |
| **Serverless** (Lambda, Cloud Functions) | Handler functions, deployment, triggers, environment config |

---

## Phase Design Rules

### Ordering
1. Phases MUST be ordered by dependency: no phase references concepts from a later phase.
2. Within a phase, lessons are ordered so each builds on the previous.
3. The dependency graph of the project's source files determines lesson order — files with zero internal imports come first.

### Sizing
- **3–6 lessons per phase** is the target range.
- If a phase would have 7+ lessons, split it into sub-phases (e.g., "Phase 2a — Data Models", "Phase 2b — Validation & Serialization").
- If a phase would have only 1–2 lessons, merge it into an adjacent phase.
- Each lesson should take roughly 20–40 minutes to complete.

### Difficulty Progression
- **Beginner lessons** (Phase 1, early Phase 2): assume no prior knowledge of the specific technology. Define every term. Show every import. Explain every line.
- **Intermediate lessons** (late Phase 2, Phase 3–4): assume earlier lessons completed. Can reference prior concepts without re-explaining. Introduce design patterns.
- **Advanced-optional** (Phase 5, stretch goals): deployment and infrastructure are optional for learners focused only on code. Mark these clearly.

### Naming Conventions
- Phase directories: `phase-N-<slug>` where slug is lowercase, hyphen-separated (e.g., `phase-1-python-foundations`)
- Lesson files: `lesson-N.M-<slug>.ipynb` (e.g., `lesson-1.1-environment-setup.ipynb`)
- Capstone directory: `capstone/`
- Capstone file: `capstone-project.ipynb`

---

## Notebook Structure Rules

### Cell Alternation Pattern
Every notebook should follow this rhythm:
```
[Markdown] Title + Learning Objectives
[Markdown] Concept explanation
[Code]     Imports / setup
[Markdown] Step-by-step narrative
[Code]     Code-along implementation (1 cell per logical step)
[Markdown] Exercise description
[Code]     Exercise stub with # TODO: comments
[Markdown] Key Takeaways + Next link
```

### Code Cell Rules
- Every code cell must be independently runnable IF all cells above it have been executed.
- Use inline comments to explain non-obvious lines.
- For file-writing lessons (where the learner creates a project file), use `%%writefile <path>` magic to write the code to disk, OR show the code and instruct the learner to create the file manually.
- Exercise cells include `# TODO:` followed by a clear description of what the learner should implement.

### Markdown Cell Rules
- Use `#` for the lesson title (only once, first cell).
- Use `##` for major sections (Concepts, Code-Along, Exercise, Key Takeaways).
- Use `###` for sub-sections within a major section.
- Bold key terms on first introduction.
- Use fenced code blocks (```) for terminal commands within markdown cells.
- Include the difficulty level badge at the top: `**Level: Beginner**` or `**Level: Intermediate**`.

### Non-Code Topics (Docker, K8s, CI)
For topics where the primary activity is running terminal commands rather than writing code:
- Use markdown cells with fenced ``` blocks for commands labeled "Run in your terminal"
- Where possible, use `!` shell commands or `%%bash` magic in code cells so the notebook remains interactive
- For YAML/Dockerfile content, show the content in a code cell with `%%writefile` magic
- Always explain what each command does before showing it

---

## Capstone Design Principles

1. **File creation order follows the dependency graph.** Start with files that have zero internal imports (config, logging, exceptions), then models, then integration code, then business logic, then UI/entry point, then deployment.
2. **Each step references the lesson where it was taught** (e.g., "See Lesson 1.2 for details").
3. **Verification checkpoints** after each major group of files — the learner should be able to test partial progress.
4. **The final checkpoint** must demonstrate the full running application (not just "it compiles").
5. **Stretch goals** should extend beyond what the workspace project does (e.g., add tests, add a new feature, deploy to cloud).

---

## Exemplar: Study Buddy AI (Python/Streamlit/LangChain/Docker/K8s)

This is a reference mapping for a real project. Use it as a model for similar Python ML/LLM applications.

### Discovered Stack
- Python 3.10, python-dotenv, logging, custom exceptions, setuptools
- Pydantic (BaseModel, Field, @validator)
- LangChain (PromptTemplate, PydanticOutputParser, ChatGroq)
- Streamlit (sidebar, widgets, session state, download button)
- Pandas (DataFrame, to_csv)
- Docker (python:3.10-slim, EXPOSE 8501, streamlit CMD)
- Kubernetes (Deployment, Service, Secret, NodePort)

### Phase Mapping Result
| Phase | Name | Lessons | Key Files Produced |
|-------|------|---------|-------------------|
| 1 | Python Foundations | 5 | project structure, `settings.py`, `logger.py`, `custom_exception.py`, `setup.py` + `requirements.txt` |
| 2 | Data Models & LLM Integration | 6 | `question_schemas.py`, `templates.py`, `groq_client.py`, `question_generator.py` |
| 3 | Streamlit UI & Business Logic | 5 | sidebar widgets, session state, `helpers.py` (QuizManager), `application.py` |
| 4 | Docker & Containerisation | 4 | `Dockerfile`, `.dockerignore`, build + run commands |
| 5 | Kubernetes & Deployment | 3 | `deployment.yaml`, `service.yaml`, secret + minikube commands |
| 6 | Capstone | 1 | full rebuild from scratch |

### Dependency Graph (file creation order for capstone)
```
src/__init__.py                    (no deps)
src/common/__init__.py             (no deps)
src/config/__init__.py             (no deps)
src/config/settings.py             (dotenv)
src/common/logger.py               (stdlib only)
src/common/custom_exception.py     (stdlib only)
setup.py + requirements.txt        (reads requirements.txt)
src/models/__init__.py             (no deps)
src/models/question_schemas.py     (pydantic)
src/prompts/__init__.py            (no deps)
src/prompts/templates.py           (langchain)
src/llm/__init__.py                (no deps)
src/llm/groq_client.py             (langchain-groq, settings)
src/generator/__init__.py          (no deps)
src/generator/question_generator.py (models, prompts, llm, settings, logger, exception)
src/utils/__init__.py              (no deps)
src/utils/helpers.py               (generator, streamlit, pandas)
application.py                     (helpers, generator, streamlit, dotenv)
Dockerfile                         (setup.py, all source)
manifests/deployment.yaml          (Docker image)
manifests/service.yaml             (deployment)
```
