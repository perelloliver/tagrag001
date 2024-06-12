import os
from langchain_openai import ChatOpenAI
import logging

logging.basicConfig(level=logging.INFO)

# api_key = os.getenv("OPENAI_API_KEY")

api_key = os.environ.get("OPENAI_API_KEY")
#just for debugging

try:
    if api_key is not None:
        # print("API key working")
        llm = ChatOpenAI(model="gpt-4o")

except Exception as e:
        logging.error(f"Error during setup: {e}")
        raise

    # messages = [
    # (
    #     "system",
    #     "You are a helpful assistant that finishes sentences",
    # ),
    # ("human", "Program now ru"),
    # ]

    # warmup = llm.invoke(messages)
    # print(warmup.content)
