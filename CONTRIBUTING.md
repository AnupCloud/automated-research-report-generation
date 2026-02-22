# Contributing to Autonomous Research Report Generator

Thank you for your interest in contributing! This guide will help you get started.

---

## 🚀 Getting Started

### Prerequisites
- **Python 3.11+**
- **[uv](https://docs.astral.sh/uv/)** — fast Python package manager
- **API Keys** — Google Gemini and Tavily (see `.env.example`)

### Development Setup

```bash
# Clone the repository
git clone <repo-url>
cd automated-research-report-generation

# Install dependencies
uv sync

# Copy and configure environment
cp .env.example .env
# Edit .env with your API keys

# Run the development server
uv run uvicorn research_and_analyst.api.main:app --reload --port 8000
```

---

## 📋 Development Workflow

1. **Create a branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the [Code Standards](#code-standards)

3. **Test your changes**:
   ```bash
   # Verify imports
   uv run python -c "from research_and_analyst.api.main import app; print('OK')"
   
   # Run the server and test manually
   uv run uvicorn research_and_analyst.api.main:app --reload
   ```

4. **Commit and push**:
   ```bash
   git add .
   git commit -m "feat: description of your change"
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request** against `main`

---

## 📐 Code Standards

### Python Style
- Follow **PEP 8** conventions
- Use **type hints** for all function signatures
- Write **docstrings** for all public classes and methods
- Use the project's `ResearchAnalystException` for error handling
- Use `GLOBAL_LOGGER` (structlog) for all logging — no `print()` in production code

### Imports
Always use fully-qualified package paths:
```python
# ✅ Correct
from research_and_analyst.utils.config_loader import load_config
from research_and_analyst.logger import GLOBAL_LOGGER

# ❌ Incorrect
from utils.config_loader import load_config
from logger import GLOBAL_LOGGER
```

### Commit Messages
Follow [Conventional Commits](https://www.conventionalcommits.org/):
- `feat:` — new feature
- `fix:` — bug fix
- `docs:` — documentation changes
- `refactor:` — code restructuring
- `chore:` — maintenance tasks

---

## 🏗 Project Structure

See [docs/PROJECT_FILES.md](docs/PROJECT_FILES.md) for detailed file descriptions and [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) for system architecture.

---

## 🐛 Reporting Issues

When filing an issue, please include:
1. Steps to reproduce the problem
2. Expected vs actual behavior
3. Python version and OS
4. Relevant log output from `logs/` directory

---

## 📝 License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).
