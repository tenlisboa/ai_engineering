import sys
from typing import Dict, Any
import pprint
from config import load_config
from agent.state import AgentState
from agent.graph import create_workflow
from retriever.tools import setup_retriever

def initialize_environment() -> Dict[str, Any]:
    """Inicializa o ambiente e retorna a configuração"""
    try:
        return load_config()
    except ValueError as e:
        print(f"Erro de configuração: {e}")
        sys.exit(1)

def create_input_message(question: str) -> Dict[str, list]:
    """Cria a mensagem de entrada no formato esperado pelo grafo"""
    return {
        "messages": [
            ("user", question),
        ]
    }

def process_output(output: Dict[str, Any]) -> None:
    """Processa e exibe a saída do grafo"""
    for key, value in output.items():
        print(f"\nSaída do nó '{key}':")
        print("-" * 50)
        pprint.pprint(value, indent=2, width=80, depth=None)
        print("-" * 50)

def main():
    """Função principal do aplicativo"""
    print("Inicializando RAG Agêntico...")
    
    # Inicializa o ambiente
    config = initialize_environment()
    
    # Configura o retriever e as ferramentas
    retriever_tool = setup_retriever()
    tools = [retriever_tool]
    
    # Cria o workflow
    graph = create_workflow(AgentState, tools)
    
    print("\nRAG Agêntico inicializado e pronto para responder perguntas!")
    print("Digite 'sair' para encerrar o programa.")
    
    while True:
        # Solicita input do usuário
        question = input("\nFaça sua pergunta: ").strip()
        
        # Verifica se o usuário quer sair
        if question.lower() in ['sair', 'exit', 'quit']:
            print("Encerrando o programa...")
            break
        
        if not question:
            print("Por favor, digite uma pergunta válida.")
            continue
        
        try:
            print("\nProcessando sua pergunta...")
            # Cria o input e processa através do grafo
            inputs = create_input_message(question)
            
            # Processa a pergunta através do grafo
            for output in graph.stream(inputs):
                process_output(output)
                
        except Exception as e:
            print(f"\nErro ao processar a pergunta: {e}")
            print("Por favor, tente novamente.")

if __name__ == "__main__":
    main()
