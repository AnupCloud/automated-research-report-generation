"""
Tests for the configuration loader utility.
"""

from pathlib import Path

import pytest

from research_and_analyst.utils.config_loader import _project_root, load_config


class TestProjectRoot:
    def test_project_root_returns_path(self):
        root = _project_root()
        assert isinstance(root, Path)

    def test_project_root_contains_config_dir(self):
        root = _project_root()
        config_dir = root / "config"
        assert config_dir.exists(), f"Expected config dir at {config_dir}"


class TestLoadConfig:
    def test_load_default_config(self):
        """Load the default configuration.yaml and verify top-level keys."""
        config = load_config()
        assert isinstance(config, dict)
        assert "llm" in config
        assert "embedding_model" in config

    def test_config_llm_providers(self):
        """Verify all three LLM providers are configured."""
        config = load_config()
        llm = config["llm"]
        assert "google" in llm
        assert "groq" in llm
        assert "openai" in llm

    def test_config_google_model(self):
        """Verify the Google LLM config has expected fields."""
        config = load_config()
        google = config["llm"]["google"]
        assert google["provider"] == "google"
        assert "model_name" in google
        assert "temperature" in google

    def test_config_embedding_model(self):
        """Verify embedding model configuration."""
        config = load_config()
        emb = config["embedding_model"]
        assert emb["provider"] == "google"
        assert "model_name" in emb

    def test_load_explicit_path(self):
        """Load config from an explicit path."""
        root = _project_root()
        explicit_path = str(root / "config" / "configuration.yaml")
        config = load_config(config_path=explicit_path)
        assert isinstance(config, dict)
        assert "llm" in config

    def test_load_nonexistent_path_raises(self):
        """Loading from a non-existent path should raise an exception."""
        with pytest.raises(Exception):
            load_config(config_path="/nonexistent/config.yaml")

    def test_load_config_from_env_var(self, monkeypatch):
        """Verify CONFIG_PATH environment variable is respected."""
        root = _project_root()
        config_path = str(root / "config" / "configuration.yaml")
        monkeypatch.setenv("CONFIG_PATH", config_path)
        config = load_config()
        assert "llm" in config

    def test_load_invalid_yaml(self, tmp_path):
        """Loading a file with invalid YAML should raise."""
        bad_file = tmp_path / "bad.yaml"
        bad_file.write_text(": invalid: yaml: [[[")
        with pytest.raises(Exception):
            load_config(config_path=str(bad_file))
