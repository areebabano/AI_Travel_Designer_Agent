# Travel Designer Agent

Welcome to the **Travel Designer Agent**, your AI-powered travel planning assistant!

## Overview

This project uses multiple specialized AI agents to create a seamless travel planning experience via conversational interface.

### Key Features

- **TravelPlannerAgent:** Main agent that understands user mood and preferences, then delegates tasks.
- **DestinationAgent:** Suggests specific travel destinations based on user interests.
- **BookingAgent:** Provides flight and hotel options by using dedicated tools.
- **ExploreAgent:** Recommends local attractions, activities, and foods for the chosen destination.
- **Tools:**  
  - `get_flights(destination)`: Returns mock flight details.  
  - `suggest_hotels(destination)`: Returns mock hotel suggestions.

## How It Works

1. **User Input:** The user describes their travel mood or needs.
2. **TravelPlannerAgent:** Determines which specialized agent to delegate the query.
3. **Agents & Tools:**  
   - DestinationAgent suggests travel spots.  
   - BookingAgent uses tools to fetch flight and hotel options.  
   - ExploreAgent offers local highlights.
4. **Response:** User receives tailored travel advice and booking info.

## Setup

1. Clone the repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:
pip install -r requirements.txt

markdown
Copy
Edit
4. Configure your `.env` file with required API keys.
5. Run the application:
chainlit run main.py

shell
Copy
Edit

## Example Interaction

🌍 Welcome to the Travel Planner! Tell me how you're feeling or what kind of trip you'd like.

I want a relaxing nature vacation.
(DestinationAgent suggests Bali, Swiss Alps, or Kyoto.)
Can you find flights and hotels to Switzerland?
(BookingAgent calls tools and returns flight and hotel info.)
What are some top places to visit and eat in Tokyo?
(ExploreAgent lists attractions and local foods.)

yaml
Copy
Edit

## Contribution

Feel free to contribute by opening issues or pull requests!

---

## License

[MIT License](LICENSE)
