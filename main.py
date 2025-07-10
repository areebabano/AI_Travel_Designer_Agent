def main():
    print("Hello from ai-travel-designer-agent!")


if __name__ == "__main__":
    main()

import os
from dotenv import load_dotenv

load_dotenv()

print("API Key:", os.getenv("GEMINI_API_KEY"))
