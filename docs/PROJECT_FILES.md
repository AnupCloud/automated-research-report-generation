# 📁 Project Files Reference

> Complete file-by-file description of the Autonomous Research Report Generator.

---

## Repository Root

| File | Description |
|:-----|:------------|
| `pyproject.toml` | Python project metadata, dependencies, and build configuration. Uses setuptools backend. Defines all runtime deps and a `serve` script entry point. |
| `requirements.txt` | Legacy pip-format dependency list (preserved for Docker compatibility). |
| `uv.lock` | UV-generated lockfile for reproducible installs. Regenerate with `uv lock`. |
| `.python-version` | Pins the project Python version to `3.11`. |
| `main.py` | Minimal CLI entry point for health checks. |
| `.env.example` | Template environment file with required API keys and configuration. |
| `.gitignore` | Git ignore rules for `__pycache__/`, `.venv/`, `.env`, `logs/`, `generated_report/`, etc. |
| `README.md` | Project overview, setup instructions, and architecture summary. |
| `CONTRIBUTING.md` | Contribution guidelines, code standards, and PR process. |
| `CHANGELOG.md` | Version history and release notes. |
| `LICENSE` | MIT license. |

---

## `research_and_analyst/` — Main Package

### Root

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer (empty). |

---

### `api/` — FastAPI Web Application

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer. |
| `main.py` | FastAPI application factory. Mounts static files, configures Jinja2 templates, CORS middleware, health check endpoint, and registers all routes. |

#### `api/routes/`

| File | Description |
|:-----|:------------|
| `report_routes.py` | All HTTP route handlers: auth routes (login, signup), report generation routes (dashboard, generate, feedback, download). Uses cookie-based session management. |

#### `api/services/`

| File | Description |
|:-----|:------------|
| `report_service.py` | Business logic layer. `ReportService` class manages the full report lifecycle: initiating the LangGraph pipeline, submitting human feedback, fetching report status, saving to PDF/DOCX, and serving file downloads. Uses a shared `MemorySaver` for state persistence. |

#### `api/models/`

| File | Description |
|:-----|:------------|
| `request_models.py` | Pydantic request/response models for API validation: `ReportRequest`, `FeedbackRequest`, `LoginRequest`, `SignupRequest`. |

#### `api/templates/`

| File | Description |
|:-----|:------------|
| `login.html` | Login page template with username/password form. |
| `signup.html` | User registration template. |
| `dashboard.html` | Main dashboard for authenticated users to start report generation. |
| `report_progress.html` | Report progress page showing analyst feedback form and download links. |

---

### `workflows/` — LangGraph Pipelines

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer. |
| `report_generator_workflow.py` | **Core engine.** `AutonomousReportGenerator` class builds and runs the main LangGraph DAG. Contains nodes for analyst creation, human feedback interrupt, report writing, intro/conclusion generation, finalization, and PDF/DOCX export. |
| `interview_workflow.py` | `InterviewGraphBuilder` class constructs the interview sub-graph. Manages multi-turn Q&A between analyst and expert, web search via Tavily, answer synthesis, interview transcript saving, and section writing. |

---

### `schemas/` — Data Models

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer. |
| `models.py` | Pydantic and TypedDict models: `Analyst`, `Section`, `Perspectives`, `SearchQuery`, `GenerateAnalystsState`, `InterviewState`, `ResearchGraphState`. Defines all state shapes used by LangGraph. |

---

### `prompt_lib/` — Prompt Engineering

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer. |
| `prompt_locator.py` | Jinja2-based prompt templates for all AI operations: `CREATE_ANALYSTS_PROMPT`, `ANALYST_ASK_QUESTIONS`, `GENERATE_SEARCH_QUERY`, `GENERATE_ANSWERS`, `WRITE_SECTION`, `REPORT_WRITER_INSTRUCTIONS`, `INTRO_CONCLUSION_INSTRUCTIONS`. Uses template variables for dynamic context injection. |

---

### `utils/` — Utility Modules

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer. |
| `config_loader.py` | `load_config()` function that loads YAML configuration with a priority chain: explicit path → `CONFIG_PATH` env var → default path. Includes `_project_root()` helper. |
| `model_loader.py` | `ApiKeyManager` (loads API keys from `.env`) and `ModelLoader` (dynamically loads LLMs and embeddings based on YAML config and `LLM_PROVIDER` env var). Supports Google Gemini, OpenAI, and Groq providers. |

---

### `database/` — Persistence

| File | Description |
|:-----|:------------|
| `db_config.py` | SQLAlchemy setup: engine, session factory, `User` model, `hash_password()` and `verify_password()` functions using bcrypt. Auto-creates SQLite tables on import. |

---

### `config/` — Configuration

| File | Description |
|:-----|:------------|
| `configuration.yaml` | YAML configuration file specifying: embedding model (Google text-embedding-004), retriever settings (top_k), and LLM configurations for all three providers (Gemini, Groq, OpenAI) with model names, temperatures, and token limits. |

---

### `logger/` — Structured Logging

| File | Description |
|:-----|:------------|
| `__init__.py` | Creates and exports `GLOBAL_LOGGER` singleton — a structlog logger used across the entire application. |
| `custom_logger.py` | `CustomLogger` class that configures structlog with JSON rendering, ISO timestamps, log-level tagging, and dual output (console + timestamped file in `logs/`). |

---

### `exception/` — Error Handling

| File | Description |
|:-----|:------------|
| `__init__.py` | Package initializer. |
| `custom_exception.py` | `ResearchAnalystException` — custom exception class that captures file name, line number, and full traceback. Supports both `sys` module and direct `Exception` objects for error details. |

---

### `notebook/` — Development Notebooks

| File | Description |
|:-----|:------------|
| `research_automation.py` | Standalone research automation script (development/testing). |
| `test.py` | Test script for workflow validation. |
| `test.ipynb` | Jupyter notebook for interactive testing and prototyping. |

---

## `static/` — Frontend Assets

| File | Description |
|:-----|:------------|
| `css/style.css` | Application stylesheet. |
| `js/app.js` | Frontend JavaScript logic. |

---

## `generated_report/` — Output Directory

Reports are organized in topic-stamped subdirectories:

```
generated_report/
├── Impact_of_GenAI_over_the_Future_of_Jobs__20251026_001447/
│   ├── *.docx
│   └── *.pdf
├── LLM_Role_in_pharma_20251026_135707/
│   ├── *.docx
│   └── *.pdf
└── ...
```

---

## CI/CD & Deployment

| File | Description |
|:-----|:------------|
| `Dockerfile` | Multi-stage Docker build: builder stage installs deps, final stage copies app code and runs uvicorn on port 8000. Includes health check. |
| `Dockerfile.jenkins` | Jenkins-specific Dockerfile with Azure CLI and Docker-in-Docker support. |
| `Jenkinsfile` | Full CI/CD pipeline: checkout → setup Python → install deps → test → Azure login → verify ACR image → deploy to Azure Container Apps → verify deployment. |
| `build-and-push-docker-image.sh` | Script to build Docker image for `linux/amd64` and push to Azure Container Registry. |
| `setup-app-infrastructure.sh` | Azure infrastructure provisioning: creates resource group, storage account, file share, ACR, and Container Apps environment. |
| `azure-deploy-jenkins.sh` | Azure deployment helper for Jenkins pipeline. |

---

## Utility Scripts

| File | Description |
|:-----|:------------|
| `get_lib_versions.py` | Reads `requirements.txt`, queries installed package versions, and rewrites the file with exact pinned versions. |
