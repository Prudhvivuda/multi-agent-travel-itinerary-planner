from langgraph.graph import StateGraph, END
from .state import PlannerState
from .functions import input_city, input_interests, create_itinerary
from utils.llm import initialize_llm 


llm = initialize_llm()  # Initialize the LLM


workflow = StateGraph(PlannerState)

workflow.add_node("input_city", input_city)
workflow.add_node("input_interest", input_interests)
workflow.add_node("create_itinerary", lambda state: create_itinerary(state, llm))  # Pass llm

workflow.set_entry_point("input_city")

workflow.add_edge("input_city", "input_interest")
workflow.add_edge("input_interest", "create_itinerary")
workflow.add_edge("create_itinerary", END)

app = workflow.compile()


if __name__ == "__main__":
    from langchain_core.runnables import chain

    print(chain)