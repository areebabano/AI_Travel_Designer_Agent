from agents import function_tool

@function_tool
def get_flights(destination: str) -> str:
    return f"Found flights to {destination}: Flight A (10:00 AM), Flight B (4:00 PM)."

