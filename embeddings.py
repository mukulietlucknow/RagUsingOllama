from dataingestion import loadPDF

from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS


def create_embeddings():
    print("creating embeddings...")
    doc = loadPDF("data/understanding-distributed-systems.pdf")
    embeddings = (
        OllamaEmbeddings(model="llama3:latest")
    )
    print("creating vector store...")
    vectorStore = FAISS.from_documents(doc, embeddings)
    print("saving vector store...")
    vectorStore.save_local("vectorDBDistributedSystems/index")
    print("done")
    
    
    
create_embeddings()