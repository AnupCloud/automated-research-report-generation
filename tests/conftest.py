"""
Shared fixtures for the test suite.
"""

import os
import sys
from pathlib import Path

import pytest

# Ensure project root is on sys.path
PROJECT_ROOT = Path(__file__).resolve().parent.parent
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Set test environment variables BEFORE any imports that load .env
os.environ.setdefault("GOOGLE_API_KEY", "test-google-key")
os.environ.setdefault("TAVILY_API_KEY", "test-tavily-key")
os.environ.setdefault("LLM_PROVIDER", "google")


@pytest.fixture
def sample_topic():
    """A reusable research topic for tests."""
    return "Impact of AI on Healthcare"


@pytest.fixture
def sample_analyst_data():
    """Sample analyst data for model tests."""
    return {
        "affiliation": "MIT",
        "name": "Dr. Jane Smith",
        "role": "AI Ethics Researcher",
        "description": "Focuses on the ethical implications of AI in healthcare settings.",
    }
