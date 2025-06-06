def formatar_docs(docs):
    """Formata uma lista de documentos em uma única string"""
    return "\n\n".join(doc.page_content for doc in docs)

def print_separator(message: str = "", length: int = 50):
    """Imprime uma linha separadora com uma mensagem opcional"""
    print(f"\n{'-' * length}")
    if message:
        print(message)
        print(f"{'-' * length}")
