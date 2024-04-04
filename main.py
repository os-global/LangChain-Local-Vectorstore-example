from dotenv import load_dotenv

load_dotenv()

from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain_mistralai import MistralAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain.chains import RetrievalQA
from langchain_mistralai import ChatMistralAI

if __name__ == "__main__":
    pdf_path = "/Users/user_home/Downloads/What_Is_AI.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    documents = loader.load()
    text_splitter = CharacterTextSplitter(
        chunk_size=1000, chunk_overlap=30, separator="\n"
    )
    docs = text_splitter.split_documents(documents=documents)

    embeddings = MistralAIEmbeddings()
    vectorstore = FAISS.from_documents(docs, embeddings)
    vectorstore.save_local("faiss_index_react")

    new_vectorstore = FAISS.load_local("faiss_index_react", embeddings, allow_dangerous_deserialization=True)
    qa = RetrievalQA.from_chain_type(
        llm=ChatMistralAI(), chain_type="stuff", retriever=new_vectorstore.as_retriever()
    )
    res = qa.run("Give me the gist of AI in 3 sentences")
    print(res)
