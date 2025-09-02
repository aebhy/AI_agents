#importing libraries
from agents import Agent , Runner , OpenAIChatCompletionsModel


# since our api key is in dotenv we are using :
from dotenv import load_dotenv
import os

# load environment variables from .env file 

load_dotenv()

GOOGLE_KEY=os.getenv("GOOGLE_API_KEY")

'''since we don't have openai api key we are using gemini api key
 .env folder . so , we are importing this ;ibrary termed as 
 below . we will create a client in this setup         '''
from openai import AsyncOpenAI


client=AsyncOpenAI (
 
       api_key="GOOGLE_KEY",
       base_url = "https://generativelanguage.googleapis.com/v1beta/openai/",
        
)




# creating and defining agent
agent = Agent(name="basic_agent",
               instructions="what is the use of numpy?",
                model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),)

# posting query for the agents purpose and the operation it should do what is being asked
query="what is the capital of france?"

# ruuning the query 
result=Runner.run_sync(agent , query)
print(result.final_output)

