from agents import Agent, handoff, RunConfig 

# Import your custom agents
from travel_agents.destination_agent import DestinationAgent
from travel_agents.explore_agent import ExploreAgent
from travel_agents.booking_agent import BookingAgent

# Main Travel Planner Agent
TravelPlannerAgent = Agent(
    name="TravelPlannerAgent",
    instructions=("""
You are the main travel guide. Start by asking the user about their current mood or what kind of travel experience they are looking for (e.g., relaxation, adventure, culture, nature, food, history, etc.).

Based on their response, route the conversation to the most appropriate specialized agent:
- Handoff to DestinationAgent if the user is unsure about where to go and needs a travel destination suggestion.
- Handoff to BookingAgent if the user already has a destination and wants to book flights or hotels.
- Handoff to ExploreAgent if the user has a destination and wants to explore attractions, food, or activities there.

Do not answer the queries yourself. Always ask first, then route to the correct agent depending on the user's input.
"""
  
    ),
    handoffs=[
        # Use 'when' conditions here for proper routing if needed (not shown here)
        handoff(DestinationAgent, on_handoff=lambda ctx: print("🔄 Handing off to DestinationAgent")),
        handoff(BookingAgent, on_handoff=lambda ctx: print("🔄 Handing off to BookingAgent")),
        handoff(ExploreAgent, on_handoff=lambda ctx: print("🔄 Handing off to ExploreAgent")),
    ]
)