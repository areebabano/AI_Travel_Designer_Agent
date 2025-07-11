# 🌍 **AI Travel Designer Agent**  
[![Python](https://img.shields.io/badge/python-3.10%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Chainlit](https://img.shields.io/badge/Chainlit-UI-purple?logo=chainlit&logoColor=white)](https://docs.chainlit.io/)
[![OpenAI](https://img.shields.io/badge/OpenAI-Agent-orange?logo=openai&logoColor=white)](https://platform.openai.com/)
[![MIT License](https://img.shields.io/badge/license-MIT-brightgreen)](LICENSE)

✨ **Your intelligent, interactive travel companion — designed to make every journey unforgettable.**

---

## 🧠 **Overview**

**AI Travel Designer Agent** is a smart, AI-powered travel assistant that helps you dream, plan, and explore the world — right from your terminal or web interface. Whether you’re picking a destination, booking mock flights and hotels, or discovering local attractions and food, this agent is your one-stop solution for all things travel.

> _“Travel isn’t always pretty. It isn’t always comfortable... But that’s okay. The journey changes you; it should change you.”_  
> — **Anthony Bourdain**

---

## 🚀 **Features at a Glance**

| ✨ **Feature**                  | **Description**                                                                 |
|-------------------------------|---------------------------------------------------------------------------------|
| ✈️ **Destination Suggestions** | Personalized places based on your mood, region, and season.                    |
| 🏨 **Mock Booking Assistant**  | Offers mock flights and hotels tailored to your schedule and budget.           |
| 🍽️ **Explore Attractions & Food** | Discover top attractions and must-try local dishes.                         |
| 🤖 **Multi-Agent Coordination** | Combines Destination, Explore, and Booking agents for seamless planning.       |
| 💬 **Interactive Chat UI**     | Plan your trip through an intuitive CLI or web-based Chainlit interface.       |
| 🔑 **Powered by Gemini API**   | Leverages Google Gemini 2.0 Flash model for intelligent, real-time responses.  |

---

## 📋 **Getting Started**

### ✅ **Prerequisites**

- Python **3.10+**
- **Chainlit** for chat interface
- **OpenAI SDK** with Gemini support
- `python-dotenv` for managing environment variables
- A **Gemini API Key** from [Google AI Studio](https://aistudio.google.com/)

---

## ⚙️ **Quick Setup**

# Install uv (Python package manager)
pip install uv

# Create and activate virtual environment
uv venv
uv shell

# Install required libraries
uv pip install openai chainlit python-dotenv
Create a .env file in the root of your project:

# .env
GEMINI_API_KEY="your_gemini_api_key_here"
🔧 How It Works
🧩 Agents Architecture
DestinationAgent – Recommends locations based on mood, season, and region.

ExploreAgent – Suggests attractions and cuisine for selected cities.

BookingAgent – Provides mock bookings for flights and hotels.

🧠 Core Orchestrator
Coordinates the conversation flow by calling the appropriate agents based on user queries for a smooth, intelligent response.

💬 Chainlit Interface
A user-friendly chat UI (command line or web) that guides users through trip planning step-by-step using Chainlit.

🗂️ Project Folder Structure

AI_Travel_Designer_Agent/
│
├── agents/
│   ├── destination_agent.py
│   ├── explore_agent.py
│   ├── booking_agent.py
│   └── __init__.py
│
├── core/
│   └── travel_companion_agent.py
│
├── .env
├── main.py
├── requirements.txt
├── README.md
📌 Feel free to customize or expand the agents as needed.

🌐 Live Demo
🚧 Coming Soon!
You’ll be able to deploy your app on:

🌐 Vercel

☁️ Render

🤗 Hugging Face Spaces

Once deployed, simply share the live link with anyone for instant access!

🖼️ Logo (Optional)
You can create a simple project logo using Canva or Looka, and add it at the top of your README using:

![AI Travel Designer Agent](./assets/logo.png)
💡 Final Words
Travel smarter with the power of AI — one conversation at a time.
From wanderlust to boarding pass, your journey starts here. ✨

