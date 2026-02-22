"""
Tests for the exception handling module.
"""

from research_and_analyst.exception.custom_exception import ResearchAnalystException


class TestResearchAnalystException:
    def test_basic_exception_message(self):
        exc = ResearchAnalystException("Something went wrong")
        assert "Something went wrong" in str(exc)

    def test_exception_with_error_details(self):
        try:
            _ = 1 / 0
        except Exception as e:
            exc = ResearchAnalystException("Division error", e)
            assert "Division error" in str(exc)
            assert "ZeroDivisionError" in str(exc)

    def test_exception_captures_file_info(self):
        try:
            _ = int("not_a_number")
        except Exception as e:
            exc = ResearchAnalystException("Parse error", e)
            assert exc.file_name != "<unknown>"
            assert exc.lineno > 0

    def test_exception_repr(self):
        exc = ResearchAnalystException("Test error")
        repr_str = repr(exc)
        assert "ResearchAnalystException" in repr_str
        assert "Test error" in repr_str
