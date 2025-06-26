from langchain_community.llms import Ollama
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains.question_answering import load_qa_chain
import os


def get_answer(query: str) -> str:
    persist_directory = "db"

    if not os.path.exists(persist_directory):
        return "❌ Vector store not found. Please run ingest.py first."

    retriever = Chroma(
        persist_directory=persist_directory,
        embedding_function=OllamaEmbeddings(model="llama3")
    ).as_retriever()

    docs = retriever.get_relevant_documents(query)

    if not docs:
        return "🤷 No relevant documents found. Try asking differently."

    llm = Ollama(model="llama3")
    chain = load_qa_chain(llm, chain_type="stuff")

    return chain.run(input_documents=docs, question=query)
