# # main.py

# import os

# from travel_agents.main_travel_agent import TravelPlannerAgent

# from dotenv import load_dotenv  # Load environment variables from .env file
# import chainlit as cl           # Chainlit framework for chat UI
# from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig

# # Load environment variables (like API keys)
# load_dotenv()

# # Initialize the OpenAI-compatible async client with Gemini API key and base URL
# external_client = AsyncOpenAI(
#     api_key=os.getenv("GEMINI_API_KEY"),  # Fetch API key from environment variables
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # Initialize the OpenAI chat model with the async client
# model = OpenAIChatCompletionsModel(
#     model="gemini-2.5-flash",  # Specify model version
#     openai_client=external_client,
# )

# # Configuration for running the agent, including model and client details
# config = RunConfig(
#     model=model,
#     model_provider=external_client,
#     tracing_disabled=True
# )

# # Triggered when the chat session starts
# @cl.on_chat_start
# async def start():
#     await cl.Message(content="🌍 Welcome to the Travel Planner! Tell me how you're feeling or what kind of trip you'd like.").send()

# # Triggered when the user sends a message
# @cl.on_message
# async def handle_user_message(message: cl.Message):
#     user_input = message.content

#     # Run the TravelPlannerAgent with the user's input
#     result = Runner.run_sync(TravelPlannerAgent, user_input, run_config=config)

#     # Send the final output from the agent
#     await cl.Message(content=result.final_output).send()

# main.py

# ------------------------
# Import required modules
# ------------------------

import os  # For accessing environment variables

from travel_agents.main_travel_agent import TravelPlannerAgent  # Import the main orchestrating agent

from dotenv import load_dotenv  # To load environment variables from a .env file
import chainlit as cl           # Chainlit framework to build conversational UI
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, Runner, RunConfig  # Tools for agent execution

# -----------------------------
# Load environment variables
# -----------------------------

# Load API keys and other environment-specific settings from the .env file
load_dotenv()

# -----------------------------------------------------
# Initialize OpenAI-compatible client with Gemini API
# -----------------------------------------------------

external_client = AsyncOpenAI(
    api_key=os.getenv("GEMINI_API_KEY"),  # Safely load your Gemini API key from environment variables
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"  # Gemini-compatible endpoint
)

# ----------------------------------------
# Configure the model using Gemini client
# ----------------------------------------

model = OpenAIChatCompletionsModel(
    model="gemini-2.5-flash",  # Define the Gemini model version
    openai_client=external_client,  # Set the Gemini client as the backend
)

# ---------------------------------------
# Define agent runtime configuration
# ---------------------------------------

config = RunConfig(
    model=model,  # Model to use for responses
    model_provider=external_client,  # Underlying provider (Gemini)
    tracing_disabled=True  # Disable debugging trace
)

# --------------------------------------------------
# Triggered when the chat session is started
# --------------------------------------------------

@cl.on_chat_start
async def start():
    # Send welcome message to the user when chat starts
    await cl.Message(
        content="🌍 Welcome to the Travel Planner! Tell me how you're feeling or what kind of trip you'd like."
    ).send()

# ---------------------------------------------------
# Triggered when a user sends a message to the bot
# ---------------------------------------------------

@cl.on_message
async def handle_user_message(message: cl.Message):
    user_input = message.content  # Capture the user's message

    # Pass the user input to the TravelPlannerAgent for processing
    result = Runner.run_sync(TravelPlannerAgent, user_input, run_config=config)

    # Return the final result from the agent back to the user
    await cl.Message(content=result.final_output).send()
