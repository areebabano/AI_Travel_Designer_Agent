# from agents import function_tool

# @function_tool
# def suggest_hotels(destination: str) -> str:
#     return f"Hotels in {destination}: Hotel Blue, City Inn, Comfort Stay."

# agents module se function_tool decorator import kar rahe hain
from agents import function_tool

# suggest_hotels function ko tool banane ke liye @function_tool decorator use kiya gaya hai
@function_tool
def suggest_hotels(destination: str) -> str:
    # Given destination ke liye mock hotel suggestions return karta hai
    return f"Hotels in {destination}: Hotel Blue, City Inn, Comfort Stay."
