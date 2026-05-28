import os
from dotenv import load_dotenv

load_dotenv()

import os
from langchain_community.document_loaders import CSVLoader
# from langchain_community.document_loaders import UnstructuredExcelLoader
import pandas as pd
from langchain_community.document_loaders import DataFrameLoader
# Current folder
folder_path = "."

all_docs = []

for file in os.listdir(folder_path):

    file_path = os.path.join(folder_path, file)

    # CSV Files
    if file.endswith(".csv"):

        print(f"Loading CSV: {file}")

        loader = CSVLoader(file_path=file_path)

        docs = loader.load()

        all_docs.extend(docs)

    # Excel Files
    
    elif file.endswith(".xlsx"):

        print(f"Loading Excel: {file}")

        df = pd.read_excel(file_path)

    # Convert all values to string
        df = df.astype(str)

    # Convert rows into text
        rows = df.apply(
            lambda row: " | ".join(row.values),
            axis=1
        )

    # Create LangChain documents
        docs = DataFrameLoader(
            pd.DataFrame(rows, columns=["text"]),
            page_content_column="text"
        ).load()

        all_docs.extend(docs)

from langchain_text_splitters import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(
    chunk_size = 700,#~150 words per chunk
    chunk_overlap = 200,#overlap keeps context at boundaries
    separators = ['\n\n','\n','.',' '],#tries paragraph - line-sentence-word
)
chunks = splitter.split_documents(all_docs)

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
vector_store = Chroma.from_documents(chunks,embeddings)

retriever = vector_store.as_retriever(search_kwargs={"k":5})
# test_query  = "Who is the Head of Department of Artificial Intelligence Department"
# retrieved = retriever.invoke(test_query)

#RAG PIPELINE
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_groq import ChatGroq

#---Helper: join retrieved chunks into a single context string ---
def format_docs(docs):
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

    
SYSTEM_PROMPT = """
You are a helpful AI assistant similar to ChatGPT.

Answer questions clearly and conversationally.

If context is available, use it.
If context is missing, answer using your general knowledge but clearly mention when information is not from the dataset.

Do not show reasoning or chain-of-thought.


Context:
{context}
"""

prompt = ChatPromptTemplate.from_messages([
    ("system", SYSTEM_PROMPT),
    ("human","{question}"),
    ])

# ---LLM via Groq API---
llm = ChatGroq(
    model = "qwen/qwen3-32b",
    temperature = 1.5,

)

chain = (
    {"context":retriever | format_docs, "question" : RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()

)


print("RAG Pipeline Ready")
