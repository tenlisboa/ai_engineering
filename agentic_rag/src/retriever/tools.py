from langchain_community.document_loaders import WebBaseLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.tools.retriever import create_retriever_tool

def setup_retriever():
    """Configure e retorna a ferramenta de recuperação"""
    # URLs dos sites que serão processados
    urls = [
        "https://scoras.com.br/academy/",
        "https://scoras.com.br/"
    ]

    # Carrega os documentos de cada URL
    docs = [WebBaseLoader(url).load() for url in urls]
    docs_list = [item for sublist in docs for item in sublist]

    # Configura o divisor de texto
    text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(
        chunk_size=100,
        chunk_overlap=50
    )
    doc_splits = text_splitter.split_documents(docs_list)

    # Adiciona ao banco de dados vetorial
    vectorstore = Chroma.from_documents(
        documents=doc_splits,
        collection_name="rag-chroma",
        embedding=OpenAIEmbeddings(),
    )
    retriever = vectorstore.as_retriever()

    # Cria e retorna a ferramenta de recuperação
    return create_retriever_tool(
        retriever,
        "retrieve_blog_posts",
        "Pesquise e retorne informações sobre cursos da Scoras Academy e serviços da Scoras, que são duas empresas diferentes"
    )
