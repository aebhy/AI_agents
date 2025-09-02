from agents import Agent, Runner, OpenAIChatCompletionsModel
from dotenv import load_dotenv
import os
from openai import AsyncOpenAI

# Load environment variables
load_dotenv()

GOOGLE_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_KEY:
    raise ValueError("GOOGLE_API_KEY not found in .env file")

# Create Google client
client = AsyncOpenAI(
    api_key=GOOGLE_KEY,  # ✅ fixed here
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Create agent
agent = Agent(
    name="basic_agent",
    instructions="what is the use of numpy?",
     model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client,
    ),
)

# Run query
query = "what is the capital of china?"
result = Runner.run_sync(agent, query)
print(result.final_output)
