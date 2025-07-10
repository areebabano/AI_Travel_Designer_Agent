import chainlit as cl
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from core.travel_companion_agent import TravelCompanionAgent

# Initialize once
planner = TravelCompanionAgent()

# Store conversation state
user_data = {}

@cl.on_chat_start
async def start():
    await cl.Message(content="👋 Hello! I’m your Travel Companion Agent.\nLet’s plan your perfect trip!").send()
    await cl.Message(content="🌈 What's your mood for this trip? (e.g., relaxing, adventurous, romantic)").send()

@cl.on_message
async def handle_message(message: cl.Message):
    content = message.content.strip()

    if "mood" not in user_data:
        user_data["mood"] = content
        await cl.Message(content="🌍 Which region are you interested in? (e.g., Europe, Asia)").send()

    elif "region" not in user_data:
        user_data["region"] = content
        await cl.Message(content="🍂 What season are you planning to travel in? (e.g., summer, winter)").send()

    elif "season" not in user_data:
        user_data["season"] = content
        await cl.Message(content="✈️ What is your departure city?").send()

    elif "origin" not in user_data:
        user_data["origin"] = content
        await cl.Message(content="📅 What is your travel date? (e.g., 2025-08-20)").send()

    elif "travel_date" not in user_data:
        user_data["travel_date"] = content
        await cl.Message(content="💰 What is your budget? (e.g., low, medium, high)").send()

    elif "budget" not in user_data:
        user_data["budget"] = content
        await cl.Message(content="🧳 Planning your trip... Please wait!").send()

        # ✅ Await the async function properly
        result = await planner.handle_travel_plan(
            mood=user_data["mood"],
            region=user_data["region"],
            season=user_data["season"],
            origin=user_data["origin"],
            travel_date=user_data["travel_date"],
            budget=user_data["budget"]
        )

        await cl.Message(content=result).send()

        # Clear for next user/session
        user_data.clear()
