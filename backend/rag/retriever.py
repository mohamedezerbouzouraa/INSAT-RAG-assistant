from langchain_community.retrievers import BM25Retriever
from rag.documents import documents
from config import TOP_K

retriever = BM25Retriever.from_documents(
    documents=documents,
    k=TOP_K
    
)
