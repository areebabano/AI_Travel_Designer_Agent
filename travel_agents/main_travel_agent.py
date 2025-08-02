# from agents import Agent, handoff, RunConfig 

# # Import your custom agents
# from travel_agents.destination_agent import DestinationAgent
# from travel_agents.explore_agent import ExploreAgent
# from travel_agents.booking_agent import BookingAgent

# # Main Travel Planner Agent
# TravelPlannerAgent = Agent(
#     name="TravelPlannerAgent",
#     instructions=("""
# You are the main travel guide. Start by asking the user about their current mood or what kind of travel experience they are looking for (e.g., relaxation, adventure, culture, nature, food, history, etc.).

# Based on their response, route the conversation to the most appropriate specialized agent:
# - Handoff to DestinationAgent if the user is unsure about where to go and needs a travel destination suggestion.
# - Handoff to BookingAgent if the user already has a destination and wants to book flights or hotels.
# - Handoff to ExploreAgent if the user has a destination and wants to explore attractions, food, or activities there.

# Do not answer the queries yourself. Always ask first, then route to the correct agent depending on the user's input.
# """
  
#     ),
#     handoffs=[
#         # Use 'when' conditions here for proper routing if needed (not shown here)
#         handoff(DestinationAgent, on_handoff=lambda ctx: print("🔄 Handing off to DestinationAgent")),
#         handoff(BookingAgent, on_handoff=lambda ctx: print("🔄 Handing off to BookingAgent")),
#         handoff(ExploreAgent, on_handoff=lambda ctx: print("🔄 Handing off to ExploreAgent")),
#     ]
# )

# agents library se necessary components import kar rahe hain:
# Agent: custom agent banane ke liye
# handoff: doosre agents ko route karne ke liye
# RunConfig: optional runtime configuration (abhi use nahi ho raha)
from agents import Agent, handoff, RunConfig 

# Apne custom agents import kar rahe hain
from travel_agents.destination_agent import DestinationAgent  # Destination suggest karta hai
from travel_agents.explore_agent import ExploreAgent          # Attractions, food, activities suggest karta hai
from travel_agents.booking_agent import BookingAgent          # Flights aur hotels book karta hai

# TravelPlannerAgent banaya gaya hai — ye main entry point agent hai
TravelPlannerAgent = Agent(
    name="TravelPlannerAgent",  # Agent ka naam

    # Ye instructions batati hain ke agent ka kaam kya hai
    instructions=("""
You are the main travel guide. Start by asking the user about their current mood or what kind of travel experience they are looking for (e.g., relaxation, adventure, culture, nature, food, history, etc.).

Based on their response, route the conversation to the most appropriate specialized agent:

- Handoff to DestinationAgent if the user is unsure about where to go and needs a travel destination suggestion.
- Handoff to BookingAgent if the user already has a destination and wants to book flights or hotels.
- Handoff to ExploreAgent if the user has a destination and wants to explore attractions, food, or activities there.

Do not answer the queries yourself. Always ask first, then route to the correct agent depending on the user's input.
"""
    ),

    # Handoff conditions define kar rahe hain — kis situation me kis agent ko control dena hai
    handoffs=[
        # Agar user ko destination chahiye (wo sure nahi hai kahan jana hai) → DestinationAgent
        handoff(DestinationAgent, on_handoff=lambda ctx: print("🔄 Handing off to DestinationAgent")),

        # Agar user ko destination pata hai aur flight/hotel book karni hai → BookingAgent
        handoff(BookingAgent, on_handoff=lambda ctx: print("🔄 Handing off to BookingAgent")),

        # Agar user ko destination pata hai aur explore karna hai (kya dekhna, khana, karna hai) → ExploreAgent
        handoff(ExploreAgent, on_handoff=lambda ctx: print("🔄 Handing off to ExploreAgent")),
    ]
)

# Example use case:
# User: "I'm looking for some adventure but I don't know where to go."
# → TravelPlannerAgent will handoff to DestinationAgent

# User: "I want to book a hotel in Istanbul."
# → TravelPlannerAgent will handoff to BookingAgent

# User: "I'm going to Tokyo, what should I do there?"
# → TravelPlannerAgent will handoff to ExploreAgent
