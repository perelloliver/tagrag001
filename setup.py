import os
from langchain_openai import ChatOpenAI
import logging

logging.basicConfig(level=logging.INFO)

# api_key = os.getenv("OPENAI_API_KEY")

api_key = os.environ.get("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_llm():
    try:
        api_key = os.getenv('OPENAI_API_KEY')
        if api_key is not None:
            # Initialize the ChatOpenAI with the provided API key
            llm = ChatOpenAI(model="gpt-4o")
            logger.info("API key working")

            messages = [
                {"role": "system", "content": "You are a helpful assistant that finishes sentences"},
                {"role": "user", "content": "Program now ru"},
            ]

            warmup = llm.invoke(messages)
            response_message = warmup.content
            logger.info("LLM message retrieved successfully")
            return response_message
        else:
            logger.error("API key is missing")
            return "API key is missing"
    except Exception as e:
        logger.error(f"Error during setup: {e}")
        return "An error occurred during LLM setup"


#LOCAL

# try:
#     if api_key is not None:
#         # print("API key working")
#         llm = ChatOpenAI(model="gpt-4o")

#         messages = [
#     (
#         "system",
#         "You are a helpful assistant that finishes sentences",
#     ),
#     ("human", "Program now ru"),
#     ]

#     warmup = llm.invoke(messages)
#     print(warmup.content)

# except Exception as e:
#         logging.error(f"Error during setup: {e}")
#         raise

