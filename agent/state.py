# TravelPlanner/agent/state.py
from typing import TypedDict, Annotated, List, Dict
from langchain_core.messages import HumanMessage, AIMessage


class PlannerState(TypedDict):
    messages: Annotated[List[HumanMessage | AIMessage], "The messages in the conversation"]
    city: str
    interests: List[str]
    itinerary: str