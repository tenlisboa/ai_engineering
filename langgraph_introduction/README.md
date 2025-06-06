

# Scoras Academy

![Logo da Scoras Academy](https://scoras.com.br/wp-content/uploads/2024/09/Scoras_academy.png)

## Bem-vindo ao Curso Introdutório de LangGraph!

Obrigado por participar do nosso curso introdutório de LangGraph. Neste guia, orientaremos você na configuração do ambiente necessário para começar.

---

## Índice

1. [Iniciando](#iniciando)
2. [Configuração do Ambiente](#configuração-do-ambiente)
   - [Usando Conda](#usando-conda)
     - [Linux](#linux)
     - [Windows e Mac](#windows-e-mac)
   - [Usando Virtual Environment (venv)](#usando-virtual-environment-venv)
     - [Mac e Linux](#mac-e-linux)
     - [Windows](#windows)
3. [Configuração das Chaves de API](#configuração-das-chaves-de-api)
   - [OpenAI API Key](#openai-api-key)
   - [LangSmith](#langsmith)
   - [Tavily para Pesquisa na Web](#tavily-para-pesquisa-na-web)
4. [Configurando Variáveis de Ambiente](#configurando-variáveis-de-ambiente)
   - [Windows](#windows-1)
   - [Mac e Linux](#mac-e-linux-1)

---

## Iniciando

Clone o repositório e navegue até o diretório:

```bash
git clone https://github.com/Scoras-Academy/Curso_Introdutorio_de_Langgraph.git
cd Curso_Introdutorio_de_Langgraph
```

## Configuração do Ambiente

### Usando Conda

#### Linux

Recomendamos Python 3.11 ou superior:

```bash
conda create -n scoras_academy python=3.11
conda activate scoras_academy
pip install -r requirements.txt
```

> **Nota:** O Jupyter Notebook já possui scripts para instalar as dependências.

#### Windows e Mac

```bash
conda create -n scoras_academy python=3.9
conda activate scoras_academy
pip install -r requirements.txt
```

### Usando Virtual Environment (venv)

#### Mac e Linux

```bash
python3 -m venv scoras_academy
source scoras_academy/bin/activate
pip install -r requirements.txt
```

#### Windows

```bash
python -m venv scoras_academy
scoras_academy\Scripts\activate
pip install -r requirements.txt
```

## Configuração das Chaves de API

### OpenAI API Key

- Se você ainda não possui uma chave da OpenAI API, inscreva-se [aqui](https://openai.com/index/openai-api/).
- Configure a variável de ambiente `OPENAI_API_KEY`.

### LangSmith

- Inscreva-se no LangSmith [aqui](https://docs.smith.langchain.com/).
- Configure as variáveis de ambiente:
  - `LANGCHAIN_API_KEY`
  - `LANGCHAIN_TRACING_V2=true`

### Tavily para Pesquisa na Web

A Tavily Search API é otimizada para LLMs e RAG, proporcionando resultados eficientes e rápidos. Inscreva-se para obter uma chave de API [aqui](https://tavily.com/).

- Configure a variável de ambiente `TAVILY_API_KEY`.

## Configurando Variáveis de Ambiente

### Windows

No Prompt de Comando, execute:

```cmd
setx OPENAI_API_KEY "sua_chave_aqui"
setx LANGCHAIN_API_KEY "sua_chave_aqui"
setx LANGCHAIN_TRACING_V2 "true"
setx TAVILY_API_KEY "sua_chave_aqui"
```

### Mac e Linux

Adicione ao `~/.bash_profile`:

```bash
echo 'export OPENAI_API_KEY="sua_chave_aqui"' >> ~/.bash_profile
echo 'export LANGCHAIN_API_KEY="sua_chave_aqui"' >> ~/.bash_profile
echo 'export LANGCHAIN_TRACING_V2="true"' >> ~/.bash_profile
echo 'export TAVILY_API_KEY="sua_chave_aqui"' >> ~/.bash_profile
source ~/.bash_profile
```

---

**Boa sorte e bom aprendizado com a Scoras Academy!**

