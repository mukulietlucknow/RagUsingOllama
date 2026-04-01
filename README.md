# RAG Using Ollama

A Retrieval-Augmented Generation (RAG) system built with LangChain, Ollama, FAISS, and Streamlit. This project allows you to ingest PDF documents, create vector embeddings, and query them through a web interface for contextual answers.

## Features

- **Document Ingestion**: Load and split PDF files into manageable chunks.
- **Embedding Generation**: Use Ollama models (e.g., Llama 3, Gemma) to create vector embeddings.
- **Vector Storage**: Store embeddings in a FAISS vector database for efficient retrieval.
- **Query Interface**: Interactive Streamlit web app for asking questions and getting answers based on the ingested documents.
- **Local Inference**: Run entirely locally using Ollama for privacy and cost-efficiency.

## Prerequisites

- Python 3.8 or higher
- Ollama installed and running (download from [ollama.ai](https://ollama.ai))
- At least one Ollama model pulled (e.g., `ollama pull llama3:latest` or `ollama pull gemma2:2b`)

## Installation

1. **Clone or Download the Project**:
   ```
   git clone <repository-url>
   cd RagUsingOllama
   ```

2. **Create a Virtual Environment**:
   ```
   python -m venv .venv
   .venv\Scripts\activate  # On Windows
   # source .venv/bin/activate  # On macOS/Linux
   ```

3. **Install Dependencies**:
   ```
   pip install -r requirement.txt
   ```

4. **Install Ollama**:
   - Download and install Ollama from the official website.
   - Pull required models:
     ```
     ollama pull llama3:latest  # For embeddings and LLM
     ollama pull gemma2:2b      # Alternative LLM
     ```

## Usage

### 1. Prepare Data
- Place your PDF files in the `data/` directory (e.g., `data/Mukul_Varshney_Resume.pdf`).

### 2. Create Embeddings
Run the embedding script to process documents and build the vector store:
```
python embeddings.py
```
This will:
- Load and split the PDF into chunks (500 characters with 50 overlap).
- Generate embeddings using Ollama.
- Save the FAISS index to `vectorDB/index/`.

**Note**: This step may take time depending on document size and hardware. For faster processing, consider using a smaller model or GPU acceleration in Ollama.

### 3. Run the Query Interface
Start the Streamlit app:
```
streamlit run my_retriver.py
```
- Open the provided URL in your browser.
- Enter questions related to the ingested documents.
- Get contextual answers limited to 100 words.

### 4. Data Ingestion (Optional)
If you need to modify document processing, edit `dataingestion.py`:
- Adjust chunk size or overlap in `RecursiveCharacterTextSplitter`.
- Supports PyPDFLoader for PDF files.

## Project Structure

```
RagUsingOllama/
├── data/                          # Directory for input PDF files
├── vectorDB/
│   └── index/                     # FAISS vector store index
├── dataingestion.py               # PDF loading and text splitting
├── embeddings.py                  # Embedding creation and vector store setup
├── my_retriver.py                 # Streamlit app for querying
├── requirement.txt                # Python dependencies
└── README.md                      # This file
```

## How It Works

1. **Ingestion**: PDFs are loaded using PyPDFLoader and split into chunks for better retrieval.
2. **Embedding**: Each chunk is converted to a vector using Ollama's embedding model.
3. **Storage**: Vectors are stored in FAISS for fast similarity search.
4. **Retrieval**: User queries are embedded and matched against stored vectors.
5. **Generation**: Relevant context is passed to the LLM (via Ollama) to generate answers.

## Configuration

- **Models**: Change models in `embeddings.py` and `my_retriver.py` (e.g., `OllamaEmbeddings(model="llama3:latest")`).
- **Chunking**: Modify `chunk_size` and `chunk_overlap` in `dataingestion.py`.
- **Prompt**: Customize the query prompt in `my_retriver.py`.

## Troubleshooting

- **ModuleNotFoundError**: Ensure virtual environment is activated and dependencies are installed.
- **Ollama Connection Issues**: Verify Ollama is running (`ollama serve`) and models are pulled.
- **Slow Embedding**: Use a smaller model or enable GPU in Ollama.
- **FAISS Errors**: Delete `vectorDB/index/` and re-run `embeddings.py` if corrupted.

## Dependencies

- langchain: For chaining LLM and retrieval components
- langchain-community: Community integrations (Ollama, FAISS)
- langchain-core: Core LangChain functionality
- streamlit: Web app framework
- pypdf: PDF processing
- faiss-cpu: Vector database
- sentence-transformers: Alternative embeddings (optional)

## Contributing

1. Fork the repository.
2. Create a feature branch.
3. Make changes and test.
4. Submit a pull request.

## License

This project is open-source. Use at your own risk.

## Acknowledgments

- Built with [LangChain](https://langchain.com)
- Powered by [Ollama](https://ollama.ai)
- Vector storage via [FAISS](https://github.com/facebookresearch/faiss)