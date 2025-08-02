# import asyncio
# import os
# from dotenv import load_dotenv
# from agents import Agent, Runner, OpenAIChatCompletionsModel, RunContextWrapper, function_tool
# from agents.run import RunConfig
# from dataclasses import dataclass
# from openai import AsyncOpenAI
# from agents import enable_verbose_stdout_logging
# from pydantic import BaseModel
# import asyncio
# from dataclasses import dataclass
# enable_verbose_stdout_logging()
# load_dotenv()

# gemini_api_key = os.getenv("GEMINI_API_KEY")
# if not gemini_api_key:
#     raise ValueError("GEMINI_API_KEY not found in environment variables")

# # Initialize Gemini client and model
# external_client = AsyncOpenAI(
#     api_key=gemini_api_key,
#     base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
# )

# model = OpenAIChatCompletionsModel(
#     openai_client=external_client,
#     model="gemini-2.5-flash",
# )

# # config = RunConfig(
# #     model=model,
# #     model_provider=external_client,
# #     tracing_disabled=False,
# #     messages=[
# #         {"role": "system", "content": "The user's name is Umair."}
# #     ]
# # )

# config = RunConfig(
#     model=model,
#     tracing_disabled=False,
#     messages=[
#         {"role": "system", "content": "The user's name is Umair."}
#     ]
# )


# class MyContext(BaseModel):
#     session_id: str

# # ------------------------------
# # Create Agent (No Instructions / No Tools)
# # ------------------------------
# agent = Agent(
#     name="InputInjectionAgent",
#     instructions="you are helpfull assistant",
    
    
    
# )
# context = MyContext(session_id="session_123")
# # ------------------------------
# # Main Function
# # ------------------------------
# async def main():
#     # Context (Optional)
    
#     result = await Runner.run(
#         agent=agent,
#         input="What is the user's name?",
#         context=context,
#         run_config=config,
#     )
#     print(result.final_output)

# if __name__ == "__main__":
#     asyncio.run(main())

import asyncio
import os
from dotenv import load_dotenv
from agents import Agent, Runner, OpenAIChatCompletionsModel, RunContextWrapper
from agents.run import RunConfig
from pydantic import BaseModel
from openai import AsyncOpenAI
from agents import enable_verbose_stdout_logging

enable_verbose_stdout_logging()
load_dotenv()

gemini_api_key = os.getenv("GEMINI_API_KEY")
if not gemini_api_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")

# Initialize Gemini client and model
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    openai_client=external_client,
    model="gemini-2.5-flash",
)

config = RunConfig(
    model=model,
    tracing_disabled=False
)

class MyContext(BaseModel):
    session_id: str

agent = Agent(
    name="InputInjectionAgent",
    instructions="you are a helpful assistant"
)

context = MyContext(session_id="session_123")

async def main():
    # Pre-chain message history
    input_history = [
        {"role": "system", "content": "The user's name is Umair."},
        {"role": "user", "content": "What is the user's name?"}
    ]

    result = await Runner.run(
        agent,
        input=input_history,
        input="How is the president of pakistan",  # <-- Pass full message history here!
        context=context,
        run_config=config
    )
    print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())


