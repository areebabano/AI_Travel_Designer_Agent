# from agents import function_tool

# @function_tool
# def get_flights(destination: str) -> str:
#     return f"Found flights to {destination}: Flight A (10:00 AM), Flight B (4:00 PM)."


# agents module se function_tool decorator import kar rahe hain
from agents import function_tool

# get_flights function ko tool banane ke liye @function_tool decorator use kiya gaya hai
@function_tool
def get_flights(destination: str) -> str:
    # Given destination ke liye dummy flight timings return karta hai
    return f"Found flights to {destination}: Flight A (10:00 AM), Flight B (4:00 PM)."
