from agents import function_tool

@function_tool
def suggest_hotels(destination: str) -> str:
    return f"Hotels in {destination}: Hotel Blue, City Inn, Comfort Stay."
