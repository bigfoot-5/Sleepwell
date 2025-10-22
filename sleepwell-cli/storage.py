# sleepwell-cli/storage.py
from langchain.document_loaders import TextLoader
from langchain.text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma

def load_and_split_documents(file_paths):
    """Load and split documents into chunks."""
    loaders = [TextLoader(file_path) for file_path in file_paths]
    documents = [doc for loader in loaders for doc in loader.load()]
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=100)
    return splitter.split_documents(documents)

def create_vector_store(documents):
    """Create a vector store from documents."""
    embeddings = OpenAIEmbeddings()
    return Chroma.from_documents(documents, embeddings)