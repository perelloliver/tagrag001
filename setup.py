import os
from langchain_openai import ChatOpenAI

api_key = os.getenv("OPENAI_API_KEY")

#just for debugging

if api_key is not None:
    print("API key working")
    llm = ChatOpenAI(model="gpt-4o")

    messages = [
    (
        "system",
        "You are a helpful assistant that finishes sentences",
    ),
    ("human", "Program now ru"),
    ]
    warmup = llm.invoke(messages)
    print(warmup.content)
