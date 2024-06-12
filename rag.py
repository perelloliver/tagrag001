### The following code...

## Loads our data into a quick vectorDB
## Runs basic RAG with static prompt
## Outputs filename


from langchain import hub
from langchain_chroma import Chroma
from langchain_community.document_loaders import CSVLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import CharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate, ChatMessagePromptTemplate

from setup import *

loader = CSVLoader(file_path='data.csv')
docs = loader.load()

text_splitter = CharacterTextSplitter(separator="\n",chunk_size=100, chunk_overlap=50)
splits = text_splitter.split_documents(docs)

vectorstore = Chroma.from_documents(documents=splits, embedding=OpenAIEmbeddings())

# Retrieve and generate using the relevant snippets of the blog.
retriever = vectorstore.as_retriever()
rag_prompt = hub.pull("rlm/rag-prompt") # link to prompt https://smith.langchain.com/hub/rlm/rag-prompt

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | llm
    | StrOutputParser()
)


#Test query

# x = rag_chain.invoke("Output most relevant filename to query: /Scrambled input API KEY ERROR")

# print(x)