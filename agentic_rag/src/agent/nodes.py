from typing import Literal
from langchain_core.messages import HumanMessage
from langchain_core.output_parsers import StrOutputParser
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain import hub

def avaliar_documentos(state) -> Literal["gerar", "reescrever"]:
    """Determina se os documentos recuperados são relevantes para a pergunta."""
    print("---VERIFICANDO RELEVÂNCIA---")

    class nota(BaseModel):
        """Pontuação binária para verificação de relevância."""
        pontuacao_binaria: str = Field(description="Pontuação de relevância 'sim' ou 'não'")

    modelo = ChatOpenAI(temperature=0, model="gpt-4o-mini", streaming=True)
    llm_com_ferramenta = modelo.with_structured_output(nota)

    prompt = PromptTemplate(
        template="""Você é um avaliador analisando a relevância de um documento recuperado para uma pergunta do usuário. \n 
        Aqui está o documento recuperado: \n\n {context} \n\n
        Aqui está a pergunta do usuário: {question} \n
        Se o documento contiver palavra(s)-chave ou significado semântico relacionado à pergunta do usuário, classifique-o como relevante. \n
        Dê uma pontuação binária 'sim' ou 'não' para indicar se o documento é relevante para a pergunta.""",
        input_variables=["context", "question"],
    )

    cadeia = prompt | llm_com_ferramenta

    mensagens = state["messages"]
    pergunta = mensagens[0].content
    docs = mensagens[-1].content

    resultado_avaliado = cadeia.invoke({"question": pergunta, "context": docs})
    pontuacao = resultado_avaliado.pontuacao_binaria

    if pontuacao == "sim":
        print("---DECISÃO: DOCUMENTOS RELEVANTES---")
        return "gerar"
    else:
        print("---DECISÃO: DOCUMENTOS NÃO RELEVANTES---")
        return "reescrever"

def agente(state, tools):
    """Invoca o modelo do agente para gerar uma resposta baseada no estado atual."""
    print("---CHAMANDO AGENTE---")
    mensagens = state["messages"]
    modelo = ChatOpenAI(temperature=0, streaming=True, model="gpt-4o-mini")
    modelo = modelo.bind_tools(tools)
    resposta = modelo.invoke(mensagens)
    return {"messages": [resposta]}

def reescrever(state):
    """Transforma a consulta para produzir uma pergunta melhor."""
    print("---TRANSFORMANDO CONSULTA---")
    mensagens = state["messages"]
    pergunta = mensagens[0].content

    msg = [
        HumanMessage(
            content=f""" \n 
    Analise a entrada e tente compreender a intenção semântica/significado subjacente. \n 
    Aqui está a pergunta inicial:
    \n ------- \n
    {pergunta} 
    \n ------- \n
    Formule uma pergunta aprimorada: """,
        )
    ]

    modelo = ChatOpenAI(temperature=0, model="gpt-4o-mini", streaming=True)
    resposta = modelo.invoke(msg)
    return {"messages": [resposta]}

def gerar(state):
    """Gera resposta final."""
    print("---GERANDO---")
    mensagens = state["messages"]
    pergunta = mensagens[0].content
    docs = mensagens[-1].content

    prompt = hub.pull("rlm/rag-prompt")
    llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0, streaming=True)
    
    def formatar_docs(docs):
        return "\n\n".join(doc.page_content for doc in docs)

    cadeia_rag = prompt | llm | StrOutputParser()
    resposta = cadeia_rag.invoke({"context": docs, "question": pergunta})
    return {"messages": [resposta]}
