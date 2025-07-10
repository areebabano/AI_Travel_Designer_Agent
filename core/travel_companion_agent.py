import os
from dotenv import load_dotenv
from openai import AsyncOpenAI
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

from tool.destination_agent import DestinationAgent
from tool.explore_agent import ExploreAgent
from tool.booking_agent import BookingAgent

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY missing in .env")

# Setup async OpenAI client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_tracing_disabled(disabled=True)

class TravelCompanionAgent:
    def __init__(self):
        self.destination_agent = DestinationAgent(client)
        self.explore_agent = ExploreAgent(client)
        self.booking_agent = BookingAgent(client)

    async def handle_travel_plan(
        self,
        mood: str,
        region: str,
        season: str,
        origin: str,
        travel_date: str,
        budget: str
    ) -> str:
        try:
            destinations = await self.destination_agent.suggest_destinations(mood, region, season)
        except Exception as e:
            destinations = [f"❌ Error fetching destinations: {str(e)}"]

        selected_city = destinations[0].split("-")[0].strip() if destinations else region

        try:
            explore_info = await self.explore_agent.suggest_attractions(selected_city)
        except Exception as e:
            explore_info = f"❌ Error fetching attractions: {str(e)}"

        try:
            flight_info = await self.booking_agent.get_flights(origin, selected_city, travel_date)
        except Exception as e:
            flight_info = f"❌ Error fetching flight options: {str(e)}"

        try:
            hotel_info = await self.booking_agent.suggest_hotels(selected_city, budget)
        except Exception as e:
            hotel_info = f"❌ Error fetching hotel suggestions: {str(e)}"

        final_plan = f"""
🌍 **Top Destination Suggestions**:
{chr(10).join(destinations)}

🏙️ **Explore in {selected_city}**:
{explore_info}

✈️ **Flight Options from {origin} to {selected_city} on {travel_date}**:
{flight_info}

🏨 **Hotel Suggestions in {selected_city} under {budget} budget**:
{hotel_info}
"""
        return final_plan
