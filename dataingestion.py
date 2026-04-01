from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter


# function to load pdf and split into chunks
def loadPDF(path):
    loader =  PyPDFLoader(path)
    docs  = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=800,
                                                   chunk_overlap=150)
    text = text_splitter.split_documents(docs)
    return text