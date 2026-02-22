# Automated Research Report Generation

This project is an autonomous research report generation system that uses a multi-agent approach to create detailed and comprehensive reports on a given topic. It leverages LangGraph to orchestrate a workflow of AI agents, each with a specific role in the research and writing process.

## Architecture

The project is built around a stateful graph, where each node represents a step in the report generation process. The graph is defined using LangGraph, and the state is passed between the nodes.

The main components of the architecture are:

*   **LangGraph:** Orchestrates the workflow of the AI agents.
*   **LLM:** A Large Language Model is used for generating content, creating analyst personas, and writing the report.
*   **Tavily Search:** Used for real-time web searches to gather up-to-date information.
*   **Agents:** The system uses a multi-agent approach, with different agents responsible for different tasks:
    *   **Analyst Agents:** A set of analyst personas are created with different perspectives on the topic.
    *   **Interviewer Agent:** Conducts interviews with the analyst agents to gather information.
    *   **Writer Agents:** Responsible for writing the introduction, main content, and conclusion of the report.
*   **Prompt Library:** A collection of prompts is used to guide the LLM in its tasks.
*   **Configuration:** The project uses a configuration file to manage settings.
*   **Logging and Exception Handling:** The system has robust logging and custom exception handling.

## Workflow

The report generation workflow is a multi-step process orchestrated by LangGraph:

1.  **Create Analysts:** Based on the given topic, the system creates a set of "analyst" personas with different backgrounds and perspectives. This ensures a balanced and comprehensive view of the topic.
2.  **Human Feedback:** The system pauses for human feedback on the generated analysts. This allows the user to guide the research process and ensure the analysts are aligned with the desired outcome.
3.  **Conduct Interviews:** The Interviewer Agent conducts a simulated interview with each analyst agent. During the interview, the agents discuss the topic, and the information gathered is used to create the report.
4.  **Write Report Sections:** The Writer Agents use the information gathered during the interviews to write the introduction, main content, and conclusion of the report.
5.  **Finalize Report:** The different sections of the report are assembled into a final document.
6.  **Save Report:** The final report is saved as a DOCX or PDF file.

## Project Structure

```
/
├───.gitignore
├───.python-version
├───Dockerfile
├───main.py
├───pyproject.toml
├───README.md
├───requirements.txt
├───uv.lock
├───generated_report/
├───research_and_analyst/
│   ├───__init__.py
│   ├───api/
│   ├───config/
│   ├───database/
│   ├───exception/
│   ├───logger/
│   ├───notebook/
│   ├───prompt_lib/
│   ├───schemas/
│   ├───utils/
│   └───workflows/
└───static/
```

### Key Directories

*   `research_and_analyst/`: This is the core of the project.
    *   `api/`: Contains the API for the application.
    *   `config/`: Configuration files.
    *   `database/`: Database related files.
    *   `exception/`: Custom exceptions.
    *   `logger/`: Logging configuration.
    *   `notebook/`: Jupyter notebooks for experimentation.
    *   `prompt_lib/`: The library of prompts for the LLM.
    *   `schemas/`: Pydantic models for data validation.
    *   `utils/`: Utility functions.
    *   `workflows/`: The core workflows of the application, defined using LangGraph.
*   `generated_report/`: The output directory for the generated reports.
*   `static/`: Static files for the web interface (if any).

## Installation

This project uses `uv` for package management.

### Prerequisites

*   Python 3.11 or higher
*   `uv` package manager. You can install it by following the official instructions: [https://github.com/astral-sh/uv](https://github.com/astral-sh/uv)
*   Tavily API Key: You need a Tavily API key for the search functionality. You can get one from [https://tavily.com/](https://tavily.com/).

### Steps

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/AnupCloud/automated-research-report-generation.git
    cd automated-research-report-generation
    ```

2.  **Create a virtual environment:**

    ```bash
    python -m venv .venv
    source .venv/bin/activate
    ```

3.  **Set up your environment variables:**

    Create a `.env` file in the root of the project and add your API keys:

    ```
    TAVILY_API_KEY="your_tavily_api_key"
    # Add other API keys for your LLM if needed
    ```

4.  **Sync the dependencies using `uv`:**

    ```bash
    uv pip sync --lock-file uv.lock
    ```

    This will install all the dependencies specified in the `uv.lock` file.

## Usage

To run the report generation pipeline, you can execute the `report_generator_workflow.py` script:

```bash
python -m research_and_analyst.workflows.report_generator_workflow
```

This will start the report generation process with a default topic. You can modify the `if __name__ == "__main__":` block in the script to change the topic and other settings.
