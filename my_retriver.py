from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.llms import Ollama
# from langchain_community.retrievers import MultiQueryRetriever
import streamlit as st
from langchain_community.document_loaders import PyPDFLoader

def getDB():
    embeddings = (
        OllamaEmbeddings(model="llama3:latest")
    )
    db = FAISS.load_local("D:\\AI\\RagUsingOllama\\vectorDBDistributedSystems\\index",
                          embeddings,
                          allow_dangerous_deserialization=True)
    
    return db


#---- creating prompt-----

prompt = ChatPromptTemplate.from_template(
    """
    Answer the following question based on the below context:
    <context>
    {context}
    </context>
    Question: {input}
    """
)

llm = Ollama(model="llama3:latest")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

db = getDB()

retriever = db.as_retriever()
# retriever = MultiQueryRetriever.from_llm(
#     retriever=base_retriever,
#     llm=llm
# )

def is_count_query(query: str):
    keywords = ["how many", "count", "number of", "occurrences"]
    query = query.lower()
    return any(k in query for k in keywords)

retrieval_chain = (
    {"context": retriever | format_docs, "input": RunnablePassthrough()}
    | prompt
    | llm
)

# streamlit code

st.title("basic model testing")
input_text = st.text_input("Ask a question")

# if input_text:
#     res = retrieval_chain.invoke(input_text)
#     st.write(res)


def load_full_pdf_text(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    full_text = "\n".join(doc.page_content for doc in docs)
    return full_text.lower()


full_text = load_full_pdf_text("data/understanding-distributed-systems.pdf")

if input_text:
    if is_count_query(input_text):
        word = input_text.lower().split()[-1]  # naive extraction
        count = full_text.count(word)

        st.write(f"'{word}' appears {count} times.")
    
    else:
        response_container = st.empty()
        full_response = ""

        for chunk in retrieval_chain.stream(input_text):
            if hasattr(chunk, "content"):
                full_response += chunk.content
            else:
                full_response += str(chunk)

            response_container.markdown(full_response)