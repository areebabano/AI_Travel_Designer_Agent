import chainlit as cl
from agents import Runner
from config import config
from travel_agents.main_travel_agent import TravelPlannerAgent  # Main orchestrating agent

@cl.on_chat_start
async def start():
    # Initialize conversation history in user session
    cl.user_session.set("history", [])
    # Welcome message with warm tone and clear prompt
    await cl.Message(
        "🌍 Hello! I'm your Travel Designer assistant. "
        "Tell me how you're feeling or what kind of trip you'd like, "
        "and I'll help you plan the perfect travel experience."
    ).send()

@cl.on_message
async def handle(message: cl.Message):
    # Retrieve or initialize conversation history
    history = cl.user_session.get("history", [])

    # Append user message to conversation history
    history.append({"role": "user", "content": message.content})

    # Send a thinking indicator message to the UI
    thinking_msg = await cl.Message("💡 Thinking...").send()

    try:
        # Pass full conversation history to the agent for context-aware response
        result = await Runner.run(
            TravelPlannerAgent,
            history,
            run_config=config
        )

        # Extract assistant's reply
        assistant_reply = result.final_output

        # Update the thinking message with the assistant's actual response
        thinking_msg.content = assistant_reply
        await thinking_msg.update()

        # Update conversation history with assistant's reply for next turn context
        updated_history = result.to_input_list()
        cl.user_session.set("history", updated_history)

    except Exception as e:
        # If error occurs, show error message instead of thinking indicator
        thinking_msg.content = f"❌ Oops, something went wrong: {e}"
        await thinking_msg.update()
