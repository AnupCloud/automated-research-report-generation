# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

---

## [0.1.0] — 2025-10-26

### Added
- Multi-agent research report generation pipeline using LangGraph
- Google Gemini, OpenAI, and Groq LLM provider support
- Tavily web search integration for real-time research
- FastAPI web UI with login, signup, dashboard, and report progress
- Human-in-the-loop analyst feedback system
- PDF and DOCX report export
- SQLite user authentication with bcrypt password hashing
- Structured logging with structlog (JSON format)
- YAML-based configuration management
- Jinja2 prompt templates for all AI operations
- Docker multi-stage build for containerized deployment
- Jenkins CI/CD pipeline for Azure Container Apps
- Azure infrastructure provisioning scripts

### Infrastructure
- `Dockerfile` with multi-stage build and health check
- `Jenkinsfile` for full CI/CD pipeline
- `setup-app-infrastructure.sh` for Azure resource provisioning
- `build-and-push-docker-image.sh` for ACR image management
