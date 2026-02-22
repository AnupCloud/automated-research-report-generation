"""
Tests for the logger module.
"""

import os

from research_and_analyst.logger import GLOBAL_LOGGER
from research_and_analyst.logger.custom_logger import CustomLogger


class TestCustomLogger:
    def test_global_logger_exists(self):
        """GLOBAL_LOGGER should be a valid logger instance."""
        assert GLOBAL_LOGGER is not None

    def test_logger_creates_log_directory(self, tmp_path):
        """Logger should create the log directory if it doesn't exist."""
        log_dir = str(tmp_path / "test_logs")
        logger_instance = CustomLogger(log_dir=log_dir)  # noqa: F841
        assert os.path.exists(log_dir)

    def test_logger_creates_log_file(self, tmp_path):
        """Logger should create a timestamped log file when get_logger() is called."""
        log_dir = str(tmp_path / "test_logs")
        logger_instance = CustomLogger(log_dir=log_dir)
        # Log file is only created when get_logger() configures the FileHandler
        logger = logger_instance.get_logger("test")
        logger.info("test log entry")
        assert os.path.exists(logger_instance.log_file_path)

    def test_logger_returns_structlog_logger(self):
        """get_logger() should return a valid structlog logger."""
        logger_instance = CustomLogger()
        logger = logger_instance.get_logger("test_module")
        assert logger is not None
