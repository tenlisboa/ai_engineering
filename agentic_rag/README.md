# RAG Agêntico - Scoras Academy

![Logo da Scoras Academy](https://scoras.com.br/wp-content/uploads/2024/09/Scoras_academy.png)

Bem-vindo ao projeto **RAG Agêntico** da **Scoras Academy**! Este projeto implementa um sistema de Recuperação Aumentada por Geração (RAG) usando LangGraph, permitindo fazer perguntas sobre a Scoras e Scoras Academy com respostas baseadas em conteúdo recuperado de suas páginas web.

## 👨‍🏫 Autor
**Anderson L. Amaral**  
Instrutor - Scoras Academy

## 🚀 Sobre o Projeto
Este é o primeiro aplicativo da Trilha "Deployment Agnóstico de Apps de IA". O projeto demonstra como estruturar e implementar um sistema RAG profissional, seguindo as melhores práticas de engenharia de software.

## 🏗️ Estrutura do Projeto

```
rag_agentico_app/
├── src/
│   ├── agent/          # Componentes do agente RAG
│   │   ├── nodes.py    # Implementação dos nós do grafo
│   │   ├── state.py    # Gerenciamento de estado
│   │   └── graph.py    # Definição do grafo de execução
│   ├── retriever/      # Sistema de recuperação
│   ├── utils/          # Utilitários
│   ├── config.py       # Configurações centralizadas
│   └── main.py         # Ponto de entrada da aplicação
├── Dockerfile          # Configuração Docker
├── requirements.txt    # Dependências Python
├── .env.example        # Template de variáveis de ambiente
└── README.md          # Documentação do projeto
```

### Componentes Principais

1. **`main.py`**
   - Ponto de entrada principal do aplicativo
   - Inicialização do sistema RAG
   - Gerenciamento do loop de interação

2. **`config.py`**
   - Centraliza configurações e variáveis de ambiente
   - Gerencia credenciais de APIs (OpenAI, etc.)

3. **Pasta `agent/`**
   - Implementação do RAG Agêntico
   - Nós do grafo de execução
   - Gerenciamento de estado e fluxo

4. **Pasta `retriever/`**
   - Lógica de recuperação de documentos
   - Integração com fontes de dados

5. **Arquivos de Configuração**
   - `.env.example`: Template para variáveis de ambiente
   - `requirements.txt`: Dependências do projeto
   - `Dockerfile`: Configuração de containerização

## 🚀 Como Executar com Docker

1. **Clone o repositório**:
```bash
git clone https://github.com/Scoras-Academy/rag_agentico_app.git
cd rag_agentico_app
```

2. **Configure as variáveis de ambiente**:
```bash
cp .env.example .env
```

3. **Edite o arquivo `.env` com suas chaves de API**:
```
OPENAI_API_KEY=sua_chave_openai_aqui
ANTHROPIC_API_KEY=sua_chave_anthropic_aqui
```

4. **Construa a imagem Docker**:
```bash
docker build -t rag_agentico_app .
```

5. **Execute o container**:
```bash
docker run -it --env-file .env rag_agentico_app
```

## 💻 Como Usar

1. Após iniciar o container, você verá uma mensagem de boas-vindas.

2. Digite sua pergunta quando solicitado. Exemplos:
   - "Qual o valor dos cursos da Scoras Academy?"
   - "Quais os serviços da Scoras?"

3. O sistema processará sua pergunta através de várias etapas:
   - Recuperação de informações relevantes
   - Avaliação da relevância dos documentos
   - Geração da resposta final

4. Para sair, digite 'sair'.

## ⚠️ Troubleshooting

Se encontrar problemas:
1. Verifique se as variáveis de ambiente estão configuradas corretamente
2. Confirme se sua chave da OpenAI está ativa e com créditos
3. Certifique-se de que o Docker está instalado e funcionando

## 📄 Sobre a Scoras Academy

A **Scoras Academy** é dedicada a fornecer formação prática e de qualidade em **Inteligência Artificial**, **Modelos de Aprendizado** e **Automação com Agentes de IA**. Nossos cursos combinam teoria com prática, baseando-se em casos reais da Scoras e da Dira Marketing.

Para saber mais sobre nossos cursos, visite [www.scoras.com.br/academy](https://www.scoras.com.br/academy).

## 📄 Licença

Este projeto está sob a **[Creative Commons Attribution 4.0 International License (CC BY 4.0)](LICENSE)**. Você pode usar, modificar e distribuir o conteúdo, **desde que atribua os devidos créditos à Scoras Academy**.

## 📞 Suporte

Para suporte técnico:
- **Site**: [www.scoras.com.br/academy](https://www.scoras.com.br/academy)

---

**Scoras Academy** - Capacitando mentes para o futuro da Inteligência Artificial

Desenvolvido por **Anderson L. Amaral**  
Instrutor - Scoras Academy

