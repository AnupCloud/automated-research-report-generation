"""
Tests for Pydantic data models and graph state definitions.
"""

from research_and_analyst.schemas.models import (
    Analyst,
    GenerateAnalystsState,
    Perspectives,
    ResearchGraphState,
    SearchQuery,
    Section,
)


class TestSection:
    def test_create_section(self):
        section = Section(title="Introduction", content="This is the intro.")
        assert section.title == "Introduction"
        assert section.content == "This is the intro."

    def test_section_empty_content(self):
        section = Section(title="Empty", content="")
        assert section.content == ""


class TestAnalyst:
    def test_create_analyst(self, sample_analyst_data):
        analyst = Analyst(**sample_analyst_data)
        assert analyst.name == "Dr. Jane Smith"
        assert analyst.role == "AI Ethics Researcher"
        assert analyst.affiliation == "MIT"

    def test_analyst_persona_property(self, sample_analyst_data):
        analyst = Analyst(**sample_analyst_data)
        persona = analyst.persona
        assert "Dr. Jane Smith" in persona
        assert "AI Ethics Researcher" in persona
        assert "MIT" in persona

    def test_analyst_persona_contains_all_fields(self, sample_analyst_data):
        analyst = Analyst(**sample_analyst_data)
        persona = analyst.persona
        assert "Name:" in persona
        assert "Role:" in persona
        assert "Affiliation:" in persona
        assert "Description:" in persona


class TestPerspectives:
    def test_create_perspectives(self, sample_analyst_data):
        analyst = Analyst(**sample_analyst_data)
        perspectives = Perspectives(analysts=[analyst])
        assert len(perspectives.analysts) == 1
        assert perspectives.analysts[0].name == "Dr. Jane Smith"

    def test_empty_perspectives(self):
        perspectives = Perspectives(analysts=[])
        assert len(perspectives.analysts) == 0

    def test_multiple_analysts(self, sample_analyst_data):
        a1 = Analyst(**sample_analyst_data)
        a2 = Analyst(
            affiliation="Stanford",
            name="Dr. John Doe",
            role="Healthcare Policy Analyst",
            description="Focuses on healthcare policy impact.",
        )
        perspectives = Perspectives(analysts=[a1, a2])
        assert len(perspectives.analysts) == 2


class TestSearchQuery:
    def test_create_search_query(self):
        sq = SearchQuery(search_query="AI healthcare trends 2025")
        assert sq.search_query == "AI healthcare trends 2025"

    def test_default_search_query(self):
        sq = SearchQuery()
        assert sq.search_query is None


class TestStateClasses:
    def test_generate_analysts_state_type(self):
        """Verify GenerateAnalystsState is a valid TypedDict."""
        state: GenerateAnalystsState = {
            "topic": "AI in Healthcare",
            "max_analysts": 3,
            "human_analyst_feedback": "",
            "analysts": [],
        }
        assert state["topic"] == "AI in Healthcare"
        assert state["max_analysts"] == 3

    def test_research_graph_state_type(self):
        """Verify ResearchGraphState is a valid TypedDict."""
        state: ResearchGraphState = {
            "topic": "Test Topic",
            "max_analysts": 2,
            "human_analyst_feedback": "",
            "analysts": [],
            "sections": [],
            "introduction": "",
            "content": "",
            "conclusion": "",
            "final_report": "",
        }
        assert state["topic"] == "Test Topic"
        assert state["final_report"] == ""
