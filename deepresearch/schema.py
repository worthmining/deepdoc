from typing import TypedDict, List, Annotated, Literal, Union
from pydantic import BaseModel, Field
from langchain_core.messages import BaseMessage, HumanMessage
import operator

class Section(BaseModel):
    section_name: str = Field(..., description="The name of this section of the report without its number")
    sub_sections: List[str] = Field(..., description="Comprehensive descriptions of sub-sections, each combining the sub-section title and its bullet points into a fluid, natural-language description")

class Sections(BaseModel):
    sections: List[Section] = Field(..., description="A list of sections")

class Query(BaseModel):
    query: str = Field(..., description="A search query")

class Queries(BaseModel):
    queries: List[Query] = Field(..., description="A list of search queries")

class SearchResult(BaseModel):
    query: Query = Field(..., description="The search query that was used to retrieve the raw content")
    raw_content: list[str] = Field(..., description="The raw content retrieved from the search")

class Feedback(BaseModel):
    feedback: Union[str, bool] = Field(..., description="Feedback on the report structure. If the content is good for the section, return True (boolean), otherwise return a string of feedback on what is missing or incorrect.")

class SectionOutput(BaseModel):
    final_section_content: List[str] = Field(..., description="The final section content")

class AgentState(TypedDict):
    topic: str
    outline: str
    resource_path: str
    messages: Annotated[List[BaseMessage], operator.add]
    report_structure: str
    sections: List[Section]
    final_section_content: Annotated[List[str], operator.add] = []
    final_report_content: str

class ResearchState(TypedDict):
    section: Section
    knowledge: str
    reflection_feedback: Feedback = Feedback(feedback="")
    generated_queries: List[Query] = []
    searched_queries: Annotated[List[Query], operator.add] = []
    search_results: Annotated[List[SearchResult], operator.add] = []
    accumulated_content: str = ""
    reflection_count: int = 1
    final_section_content: Annotated[List[str], operator.add] = []