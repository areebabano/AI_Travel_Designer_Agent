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
async def suggest_hotels(destination: str, check_in_date: str = None, check_out_date: str = None):
    print(f"🔧 Tool suggest_hotels called with: {check_in_date}:{check_out_date}")
    """
    Suggests hotel options for a given travel destination and optional stay dates.

    Args:
        destination (str): City or location where user wants to stay.
        check_in_date (str, optional): Check-in date in YYYY-MM-DD format.
        check_out_date (str, optional): Check-out date in YYYY-MM-DD format.

    Returns:
        dict: Hotel suggestions including name, rating, location, and approximate price range.
    """
    print(f"🔧 Tool suggest_hotels called with: destination={destination}, check_in_date={check_in_date}, check_out_date={check_out_date}")

    try:
        # Input validation
        if not destination or not destination.strip():
            return {
                "error": "⚠ Please provide a valid destination."
            }

        # Build optional dates string for prompt
        dates_info = ""
        if check_in_date and check_out_date:
            dates_info = f" for a stay from {check_in_date} to {check_out_date}"
        elif check_in_date:
            dates_info = f" starting from {check_in_date}"

        # Prompt engineering
        prompt = f"""
You are an expert travel assistant specialized in hotel recommendations.

Please suggest 3 to 4 highly-rated hotels in {destination}{dates_info}.

For each hotel, provide:
- Hotel name
- Star rating or guest rating
- Location or neighborhood
- Approximate price range per night in USD

Format your answer as a clear, concise bullet list suitable for a user looking to book accommodation.
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
            "destination": destination,
            "hotel_suggestions": output
        }

    except Exception as e:
        error_msg = f"❌ Exception in suggest_hotels tool: {str(e)}"
        print(error_msg)
        return {
            "error": error_msg
        }
