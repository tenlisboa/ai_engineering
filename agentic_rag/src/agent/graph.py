from langgraph.graph import END, StateGraph, START
from langgraph.prebuilt import ToolNode, tools_condition

def create_workflow(agent_state, tools):
    """Cria e retorna o workflow do grafo."""
    
    from .nodes import agente, avaliar_documentos, reescrever, gerar
    
    # Define um novo grafo
    workflow = StateGraph(agent_state)

    # Define os nós
    workflow.add_node("agente", lambda state: agente(state, tools))
    recuperador = ToolNode(tools)
    workflow.add_node("recuperar", recuperador)
    workflow.add_node("reescrever", reescrever)
    workflow.add_node("gerar", gerar)

    # Define as arestas
    workflow.add_edge(START, "agente")
    
    # Decide se deve recuperar
    workflow.add_conditional_edges(
        "agente",
        tools_condition,
        {
            "tools": "recuperar",
            END: END,
        },
    )

    # Arestas após a recuperação
    workflow.add_conditional_edges(
        "recuperar",
        avaliar_documentos,
        {
            "gerar": "gerar",
            "reescrever": "reescrever"
        }
    )
    
    workflow.add_edge("gerar", END)
    workflow.add_edge("reescrever", "agente")

    return workflow.compile()
