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

class DestinationAgent:
    def __init__(self, client):
        self.client = client

    async def suggest_destinations(self, mood: str, region: str, season: str) -> list:
        prompt = (
            f"Suggest 5 travel destinations in {region} for someone looking for a '{mood}' experience "
            f"during the {season} season. Provide destination names with short descriptions."
        )

        try:
            response = await self.client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.8,
                max_tokens=400,
            )

            content = response.choices[0].message.content
            return content.split("\n")

        except Exception as e:
            return [f"❌ Error while fetching destinations: {str(e)}"]
