import os
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.chains import RetrievalQA
from langchain_groq import ChatGroq  # Fixed import
from langchain_core.prompts import PromptTemplate
from tavily import TavilyClient
from dotenv import load_dotenv

load_dotenv()

TAVILY_API_KEY = os.getenv("-----")
GROQ_API_KEY = os.getenv("--------")
GROQ_MODEL = "llama3-70b-8192"  
  
tavily_client = TavilyClient(api_key=TAVILY_API_KEY)
llm = ChatGroq(api_key=GROQ_API_KEY, model=GROQ_MODEL)


prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template="""
    You are an AI career advisor. Use the below context to answer the user's query about career risk due to AI.

    Context: {context}
    Question: {question}

    Answer in clear steps. If the career is risky, suggest safer alternatives and relevant new skills.
    """
)

def get_rag_answer(user_query: str) -> str:
    
    search_results = tavily_client.search(query=user_query, search_depth="advanced", max_results=5)
    documents = [Document(page_content=doc['content']) for doc in search_results['results']]

    
    embeddings = HuggingFaceEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    retriever = vectorstore.as_retriever()


    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        chain_type="stuff",
        chain_type_kwargs={"prompt": prompt_template}
    )

    
    result = rag_chain.invoke({"query": user_query})

    return result

if __name__ == "__main__":
    query = "Is content writing a safe job in the AI era?"
    print(get_rag_answer(query))















