import os
from langchain_openai import ChatOpenAI
import logging
import time

logging.basicConfig(level=logging.INFO)

# api_key = os.getenv("OPENAI_API_KEY")

# api_key = os.environ.get("OPENAI_API_KEY")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def setup_llm():
    api_key = "sk-proj-ewmW4Vdedh9tgqFFuXrLT3BlbkFJaDfQr21qUPYysywggbwB"
    if api_key is None:
        logger.error("API key is missing")
        return "API key is missing"

    logger.info(f"Retrieved API key: {api_key[:4]}...")  # Log the first 4 characters for verification

    messages = [
        {"role": "system", "content": "You are a helpful assistant that finishes sentences"},
        {"role": "user", "content": "Program now ru"},
    ]

    attempt = 0
    max_retries = 3
    wait_time = 5  # seconds

    while attempt < max_retries:
        try:
            logger.info(f"Attempt {attempt + 1} to connect to OpenAI API")

            llm = ChatOpenAI(model="gpt-4o")

            warmup = llm.invoke(messages)

            response_message = warmup.content

            logger.info("LLM message retrieved successfully")
            return response_message
        except Exception as e:
            logger.error(f"Error during setup: {e}")
        attempt += 1
        logger.info(f"Retrying in {wait_time} seconds...")
        time.sleep(wait_time)

    return f"An error occurred during LLM setup after multiple attempts: {e}"

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

