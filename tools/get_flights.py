import os
from dotenv import load_dotenv
from agents import function_tool, AsyncOpenAI

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

external_client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
)

@function_tool
async def get_flights(origin: str, destination: str, date: str):
    print(f"🔧 Tool get_flights called with: {destination}")
    """
    Finds flight options from origin to destination on a given date.

    Args:
        origin (str): Departure city or airport.
        destination (str): Arrival city or airport.
        date (str): Travel date in YYYY-MM-DD format.

    Returns:
        dict: Flight options including airline, departure, arrival, duration, and price.
    """
    print(f"🔧 Tool get_flights called with: origin={origin}, destination={destination}, date={date}")

    try:
        # Input validation
        if not origin or not destination or not date:
            return {
                "error": "⚠ Please provide valid 'origin', 'destination', and 'date' parameters."
            }

        # Prompt engineering
        prompt = f"""
You are an expert travel assistant specialized in flight information.

Please provide up to 3 best flight options from {origin} to {destination} on {date}.

For each flight option, include:
- Airline name
- Departure time
- Arrival time
- Flight duration
- Approximate price in USD

Format your answer as a clear, concise bullet list suitable for a user looking to book flights.
"""

        # API call to the OpenAI-compatible Gemini endpoint
        response = await external_client.chat.completions.create(
            model="gemini-2.0-flash",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800
        )

        output = response.choices[0].message.content.strip()

        return {
            "origin": origin,
            "destination": destination,
            "date": date,
            "flight_options": output
        }

    except Exception as e:
        error_msg = f"❌ Exception in get_flights tool: {str(e)}"
        print(error_msg)
        return {
            "error": error_msg
        }
