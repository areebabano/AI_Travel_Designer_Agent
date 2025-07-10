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

class ExploreAgent:
    def __init__(self, client):
        self.client = client

    async def suggest_attractions(self, city: str) -> str:
        prompt = (
            f"List 5 popular tourist attractions and 3 famous local foods in {city}. "
            "Write it in a friendly and short bullet-point format."
        )

        try:
            response = await self.client.chat.completions.create(
                model="gemini-2.0-flash",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7,
                max_tokens=400,
            )

            return response.choices[0].message.content

        except Exception as e:
            return f"❌ Error while fetching attractions for {city}: {str(e)}"
