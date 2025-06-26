import os
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings  # updated import

def ingest():
    # Load and split documents
    loader = TextLoader("data/scholarships.txt", encoding="utf-8")
    documents = loader.load()
    
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    # Create embedding and store
    embedding = OllamaEmbeddings(model="llama3")

    db = Chroma.from_documents(
        documents=chunks,
        embedding=embedding,
        persist_directory="db"  # required for persistence
    )
    db.persist()
    print("✅ Vector store created in ./db")

if __name__ == "__main__":
    ingest()
