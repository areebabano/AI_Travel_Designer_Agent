# 🌍 **AI Travel Designer Agent**  
**Built with Python · Chainlit · OpenAI Gemini API · MIT License**

✨ **Your intelligent, interactive travel companion — designed to make every journey unforgettable.**

---

## 🧠 **Overview**

**AI Travel Designer Agent** is your personal AI-powered travel planner that helps you explore dream destinations, book mock flights and hotels, and uncover local attractions — all through a seamless, interactive chat interface.

> _“Travel isn’t always pretty... The journey changes you; it should change you.”_  
> — **Anthony Bourdain**

---

## 🚀 **Features at a Glance**

| ✨ **Feature**              | **Description**                                                               |
|----------------------------|-------------------------------------------------------------------------------|
| ✈️ **Destination Suggestions** | Travel spots based on your mood, region, and season.                          |
| 🏨 **Mock Booking Assistant**  | Flight and hotel options matched to your budget and schedule.                  |
| 🍽️ **Attractions & Food**      | Discover must-see places and iconic foods in your destination.               |
| 🤖 **Multi-Agent Coordination** | Destination, Explore, and Booking agents work in harmony.                    |
| 💬 **Chainlit UI**             | Chat live with your AI travel agent via CLI or web interface.                |
| 🔑 **Gemini API Powered**      | Smart replies from Google Gemini 2.0 Flash model.                            |

---

## 📋 **Getting Started**

### ✅ **Prerequisites**
- Python **3.10+**
- **Chainlit** for UI
- **OpenAI SDK** (with Gemini support)
- `python-dotenv` for managing `.env`
- Gemini API Key from [Google AI Studio](https://aistudio.google.com/)

---

## ⚙️ **Quick Setup**

```bash
pip install uv
uv venv
uv shell
uv pip install openai chainlit python-dotenv

Then add your API key in a .env file:
GEMINI_API_KEY="your_gemini_api_key_here"

🔧 How It Works
🧩 Agents
DestinationAgent – Suggests destinations by mood, season, and location.

ExploreAgent – Recommends attractions and foods.

BookingAgent – Offers mock booking options.

🧠 Orchestrator
Coordinates between agents for smooth user experience.

💬 Chainlit UI
Chat-based interface for engaging and intuitive planning.

🌐 Live Demo
🚧 Coming Soon
Deploy on Vercel, Render, or Hugging Face Spaces.

Let your users travel smarter — one conversation at a time. ✨

php-template
Copy
Edit

---

### 🌐 2. For Web/Chainlit Interface – With Animated HTML Headings

```html
<h1 style="font-weight: bold; font-size: 2.5rem; animation: fadeIn 2s ease-in-out;">🌍 AI Travel Designer Agent</h1>
<p><strong>Built with Python · Chainlit · OpenAI Gemini API · MIT License</strong></p>
<p style="font-style: italic;">✨ Your intelligent, interactive travel companion — designed to make every journey unforgettable.</p>

<hr>

<h2 style="animation: fadeInUp 1.5s ease-in-out;">🧠 <strong>Overview</strong></h2>
<p><strong>AI Travel Designer Agent</strong> is your personal AI-powered travel planner...</p>

<!-- Add similar animation to other headings -->
<style>
@keyframes fadeIn {
  from { opacity: 0; transform: scale(0.95); }
  to { opacity: 1; transform: scale(1); }
}
@keyframes fadeInUp {
  from { opacity: 0; transform: translateY(20px); }
  to { opacity: 1; transform: translateY(0); }
}
</style>


