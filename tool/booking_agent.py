import os
from openai import AsyncOpenAI
from dotenv import load_dotenv
from agents import Agent, OpenAIChatCompletionsModel, Runner, set_tracing_disabled

# Load environment variables
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("❌ GEMINI_API_KEY missing in .env")

# Setup client
client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)
set_tracing_disabled(disabled=True)

class BookingAgent:
    def __init__(self, client):
        self.client = client

    async def get_flights(self, origin: str, destination: str, date: str) -> str:
        prompt = (
            f"Mock a few flight options from {origin} to {destination} on {date}. "
            "Show airlines, departure & arrival times, and mock prices in USD."
        )

        try:
            response = await self.client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.6,
                max_tokens=350,
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"❌ Error fetching flight options: {str(e)}"

    async def suggest_hotels(self, city: str, budget: str) -> str:
        prompt = (
            f"Suggest 3 hotel options in {city} that match a {budget} budget. "
            "Include name, rating, and a short description. Keep it mock and concise."
        )

        try:
            response = await self.client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=350,
            )
            return response.choices[0].message.content

        except Exception as e:
            return f"❌ Error fetching hotel suggestions: {str(e)}"
