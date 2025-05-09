import os
from typing import Dict

from agent.workflow import app  # Import the compiled LangGraph app
from utils.llm import initialize_llm  # Import LLM initialization
from langchain_core.messages import HumanMessage


def travel_planner(user_request: str) -> None:
    """
    Executes the travel planner workflow based on the user request.

    Args:
        user_request (str): The initial request from the user.
    """

    print(f"Initial Request: {user_request}\n")
    state: Dict = {
        "messages": [HumanMessage(content=user_request)],
        "city": "",
        "interests": [],
        "itinerary": "",
    }

    for output in app.stream(state):
        print(output)  # Or process the output as needed


if __name__ == "__main__":
    # user_request = "I want to plan a day trip"  # Example usage
    # travel_planner(user_request)

    # Gradio Interface (Optional - Moved here for main execution)
    import gradio as gr

    def gradio_travel_planner(city: str, interests: str) -> str:
        llm = initialize_llm()  # Initialize LLM inside the function
        state: Dict = {
            "messages": [],
            "city": "",
            "interests": [],
            "itinerary": "",
        }
        from agent.functions import input_city, input_interests, create_itinerary
        state = input_city(city, state)
        state = input_interests(interests, state)
        itinerary = create_itinerary(state, llm)  # Pass llm
        return itinerary["itinerary"]

    interface = gr.Interface(
        fn=gradio_travel_planner,
        inputs=[
            gr.Textbox(label="Enter the city for your day trip"),
            gr.Textbox(label="Enter your interests (comma-separated)"),
        ],
        outputs=gr.Textbox(label="Generated Itinerary"),
        title="Travel Itinerary Planner",
        description="Enter a city and your interests to generate a personalized day trip itinerary.",
    )
    interface.launch(share=True)