from storage.database import get_recent_articles
from langchain.chains import RetrievalQA
from langchain.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.llms import OpenAI
from langchain.schema import Document

def build_qa_agent():
    articles = get_recent_articles(50)
    documents = [Document(page_content=a[2], metadata={"title": a[1]}) for a in articles]

    vectorstore = FAISS.from_documents(documents, OpenAIEmbeddings())
    qa = RetrievalQA.from_chain_type(
        llm=OpenAI(),
        retriever=vectorstore.as_retriever()
    )
    return qa
