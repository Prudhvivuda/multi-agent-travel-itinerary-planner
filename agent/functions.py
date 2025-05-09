# TravelPlanner/agent/agent_functions.py
from typing import Dict, List
from langchain_core.messages import HumanMessage, AIMessage
from utils.llm import initialize_llm
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate


itinerary_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful travel assistant. Create a day trip itinerary for {city} based on the user's interests: {interests}. Provide a brief, bulleted itinerary."),
    ("human", "Create an itinerary for my day trip."),
])


def input_city(city: str, state: Dict) -> Dict:
    print("Please enter the city you want to visit for your day trip: ")
    print(city, state)
    return {
        **state,
        "city": city,
        "messages": state["messages"] + [HumanMessage(content=city)],
    }


def input_interests(interests: str, state: Dict) -> Dict:
    print(interests, state)
    return {
        **state,
        "interests": [interest.strip() for interest in interests.split(",") if interest.strip()],
        "messages": state["messages"] + [HumanMessage(content=interests)],
    }


def create_itinerary(state: Dict, llm: ChatGroq) -> str:
    print(f"Creating an itinerary for {state['city']} based on interests : {', '.join(state['interests'])}")
    response = llm.invoke(itinerary_prompt.format_messages(city=state["city"], interests=", ".join(state["interests"])))
    print("\nFinal Itinerary: ")
    print(response.content)
    return {
        **state,
        "messages": state["messages"] + [AIMessage(content=response.content)],
        "itinerary": response.content,
    }