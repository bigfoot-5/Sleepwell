# sleepwell-cli/suggestion.py
from sleepwell_cli.storage import load_and_split_documents, create_vector_store
from sleepwell_cli.rules_engine import load_rules, apply_rules
from langchain.chains import RetrievalQA
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain_ollama.llms import OllamaLLM

def query_ollama(prompt, model="qwen3:1.7b"):
    """Query the Ollama model."""
    llm = OllamaLLM(model_name=model)
    return llm.invoke(prompt)

def create_rag_chain(vector_store):
    """Create a RAG chain."""
    prompt_template = """
    You are a helpful assistant. Given the following context, answer the user's question:

    {context}

    User's question: {question}
    """
    prompt = PromptTemplate(input_variables=["context", "question"], template=prompt_template)
    llm_chain = LLMChain(prompt=prompt, llm=query_ollama)
    return RetrievalQA(combine_docs_chain=llm_chain, retriever=vector_store.as_retriever())

def generate_suggestion(query):
    """Generate a suggestion based on the user query."""
    # Load and split documents
    document_paths = ["data/document1.txt", "data/document2.txt"]
    documents = load_and_split_documents(document_paths)
    
    # Create vector store
    vector_store = create_vector_store(documents)
    
    # Create RAG chain
    rag_chain = create_rag_chain(vector_store)
    
    # Load rules
    rules = load_rules()
    
    # Retrieve relevant documents
    retrieved_docs = rag_chain.retrieve(query)
    
    # Apply rules to retrieved documents
    for doc in retrieved_docs:
        doc['content'] = apply_rules(doc['content'], rules)
    
    # Generate suggestion
    suggestion = rag_chain.run(query)
    return suggestion