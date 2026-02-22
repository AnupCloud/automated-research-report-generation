# models.py
import operator
from typing import Annotated

from langgraph.graph import MessagesState
from pydantic import BaseModel, Field
from typing_extensions import TypedDict

# -------------------------------
# Section Model
# -------------------------------


class Section(BaseModel):
    title: str
    content: str


# -------------------------------
# Analyst Models
# -------------------------------


class Analyst(BaseModel):
    affiliation: str = Field(description="Primary affiliation of the analyst.")
    name: str = Field(description="Name of the analyst.")
    role: str = Field(description="Role of the analyst in the context of the topic.")
    description: str = Field(description="Description of the analyst's focus, concerns, and motives.")

    @property
    def persona(self) -> str:
        return (
            f"Name: {self.name}\nRole: {self.role}\nAffiliation: {self.affiliation}\nDescription: {self.description}\n"
        )


class Perspectives(BaseModel):
    analysts: list[Analyst] = Field(description="Comprehensive list of analysts with their roles and affiliations.")


# -------------------------------
# Search Query Output Parser
# -------------------------------


class SearchQuery(BaseModel):
    search_query: str = Field(None, description="Search query for retrieval.")


# -------------------------------
# State Classes for Graphs
# -------------------------------


class GenerateAnalystsState(TypedDict):
    topic: str  # Research topic
    max_analysts: int  # Number of analysts to generate
    human_analyst_feedback: str  # Feedback from human
    analysts: list[Analyst]  # List of analysts generated


class InterviewState(MessagesState):
    max_num_turns: int  # Max interview turns allowed
    context: Annotated[list, operator.add]  # Retrieved or searched context
    analyst: Analyst  # Analyst conducting interview
    interview: str  # Full interview transcript
    sections: list  # Generated section from interview


class ResearchGraphState(TypedDict):
    topic: str  # Research topic
    max_analysts: int  # Number of analysts
    human_analyst_feedback: str  # Optional human feedback
    analysts: list[Analyst]  # All analysts involved
    sections: Annotated[list, operator.add]  # All interview-generated sections
    introduction: str  # Introduction of final report
    content: str  # Main content of report
    conclusion: str  # Conclusion of final report
    final_report: str  # Compiled report string
