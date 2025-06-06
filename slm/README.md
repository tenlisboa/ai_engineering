# ![Logo da Sua Empresa](https://scoras.com.br/wp-content/uploads/2024/09/Scoras_academy.png)

# SLM: Série de Aulas Práticas

Bem-vindo(a) à série de aulas práticas que complementam as aulas teóricas de SLM. Este repositório foi criado para facilitar o aprendizado e a integração de modelos de linguagem de grande escala em seus projetos.

## Integrando Ollama com Langgraph/Langchain

![Ollama Logo](https://ollama.com/public/ollama.png)

### Introdução ao Ollama

O [Ollama](https://ollama.com/) é uma ferramenta poderosa que permite executar modelos de linguagem de grande escala localmente. Ele atua como um servidor que roda modelos como **Qwen**, **Mistral** e muitos outros. Para mais informações e documentação, visite o [repositório oficial do Ollama no GitHub](https://github.com/ollama/ollama).

### Alternativa: Uso do Google Colab

Como alternativa ao Ollama, você pode utilizar o Google Colab para executar os modelos de linguagem sem a necessidade de configuração local. Acesse o notebook do Colab através deste [link](https://colab.research.google.com/drive/1YqM_WXSdGVoIpoqk8FrjjH4eGjUlt_sQ#scrollTo=cNUSOhkUiHhS) ou diretamente no repositório.

## Bibliotecas Necessárias

Para executar este notebook Jupyter, você precisará instalar as seguintes bibliotecas:

```bash
pip install langgraph langchain langchain-community langgchainhub langchain-core
pip install -U langchain-ollama
```

> **Nota:** Não se esqueça do "!" no início dos comandos se estiver executando no Jupyter Notebook.

## Configurando o Ollama

Certifique-se de que o serviço Ollama esteja em execução em sua máquina local. Se ainda não o instalou, siga as instruções abaixo:

### Instalação

- **macOS:** [Download](https://ollama.com/download-macos)
- **Windows (Prévia):** [Download](https://ollama.com/download-windows)
- **Linux:**

  ```bash
  curl -fsSL https://ollama.com/install.sh | sh
  ```

  Para instruções detalhadas, visite a [página de instalação manual](https://ollama.com/install).

- **Docker:** A imagem oficial do Ollama `ollama/ollama` está disponível no [Docker Hub](https://hub.docker.com/r/ollama/ollama).

### Executando o Ollama

Para executar e interagir com o modelo Llama 3.2, por exemplo, use:

```bash
ollama run llama3.2
```

## Modelo Utilizado: Qwen2.5

Neste projeto, estamos utilizando o modelo **Qwen2.5**, que faz parte da mais recente série de modelos de linguagem de grande escala Qwen.

### Características do Qwen2.5

- Disponível em tamanhos variando de **0,5 a 72 bilhões de parâmetros**.
- Melhorias significativas em relação ao Qwen2:
  - Conhecimento ampliado e capacidades aprimoradas em codificação e matemática.
  - Avanços na compreensão de instruções, geração de texto longo (mais de 8K tokens), compreensão de dados estruturados e geração de saídas estruturadas.
  - Maior resiliência a diversos prompts de sistema, melhorando role-play e configuração de condições para chatbots.
- Suporte para contextos longos de até **128K tokens** e geração de até **8K tokens**.
- Suporte multilíngue para mais de **29 idiomas**, incluindo português, inglês, espanhol, francês, alemão, italiano, russo, japonês, coreano, entre outros.

### Instalando e Executando o Qwen2.5

Para instalar e executar o Qwen2.5 (ou qualquer outro modelo), utilize os seguintes comandos:

- Se não estiver usando Docker:

  ```bash
  ollama run qwen2.5
  ```

- Se estiver usando Docker:
1. Baixe a imagem do Ollama:
    ```bash
    docker pull ollama/ollama
    ```

2. Execute o container do Ollama:

      **Sem GPU**

      ```bash
      docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
      ```
      **Com GPU**

      ```bash	
      docker run -d --gpus=all -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
      ```

3. Execute o modelo Qwen2.5 no container Ollama:
    ```bash
    docker exec -it ollama ollama run qwen2.5
    ```

### Configurando o ambiente para usar o Docker com CUDA (Nvidia GPU):
1. Abra o terminal do **PowerShell** como administrador no Windows
2. Atualize e entre no ambiente WSL
    ```bash
    wsl --update
    wsl
    ```

3. Remova repositórios e chaves CUDA e NVIDIA existentes
    ```bash
    sudo rm -f /etc/apt/sources.list.d/cuda.list
    sudo rm -f /etc/apt/sources.list.d/nvidia-ml.list
    sudo apt-key del 7fa2af80
    ```

4. Baixe e configure o pin do repositório CUDA
    ```bash
    wget https://developer.download.nvidia.com/compute/cuda/repos/wsl-ubuntu/x86_64/cuda-wsl-ubuntu.pin
    sudo mv cuda-wsl-ubuntu.pin /etc/apt/preferences.d/cuda-repository-pin-600
    ```

5. Baixe e instale o pacote do repositório CUDA
    ```bash
    wget https://developer.download.nvidia.com/compute/cuda/11.8.0/local_installers/cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
    sudo dpkg -i cuda-repo-wsl-ubuntu-11-8-local_11.8.0-1_amd64.deb
    sudo cp /var/cuda-repo-wsl-ubuntu-11-8-local/cuda-*-keyring.gpg /usr/share/keyrings/
    ```

6. Atualize listas de pacotes e instale CUDA e o kit de ferramentas NVIDIA CUDA
    ```bash
    sudo apt-get update
    sudo apt-get -y install cuda-11-8
    sudo apt install nvidia-cuda-toolkit
    ```

7. Verifique a versão do compilador CUDA
    ```bash
    nvcc --version
    ```

8. Saia do ambiente WSL
    ```bash
    exit
    ```

9. Teste a instalação do CUDA com Docker
    ```bash
    docker run --rm --gpus all nvidia/cuda:11.8.0-base-ubuntu22.04 nvidia-smi
    docker run --gpus all nvcr.io/nvidia/k8s/cuda-sample:nbody nbody -gpu -benchmark
    ```

10. Reinicie o serviço Docker e pronto!
    ```bash
    Restart-Service com.docker.service
    ```
  <br />

> **Observação:** Todos os modelos, exceto os de 3B e 72B, são lançados sob a licença Apache 2.0. Os modelos 3B e 72B estão sob a licença Qwen.

## Biblioteca de Modelos

O Ollama suporta uma lista extensa de modelos disponíveis em [ollama.com/library](https://ollama.com/library). Alguns modelos de exemplo que podem ser baixados:

| Modelo                | Parâmetros | Tamanho | Comando de Download               |
|-----------------------|------------|---------|-----------------------------------|
| **Llama 3.2**         | 3B         | 2.0GB   | `ollama run llama3.2`             |
| Llama 3.2             | 1B         | 1.3GB   | `ollama run llama3.2:1b`          |
| Llama 3.1             | 8B         | 4.7GB   | `ollama run llama3.1`             |
| Llama 3.1             | 70B        | 40GB    | `ollama run llama3.1:70b`         |
| Llama 3.1             | 405B       | 231GB   | `ollama run llama3.1:405b`        |
| Phi 3 Mini            | 3.8B       | 2.3GB   | `ollama run phi3`                 |
| Phi 3 Medium          | 14B        | 7.9GB   | `ollama run phi3:medium`          |
| **Mistral**           | 7B         | 4.1GB   | `ollama run mistral`              |
| Code Llama            | 7B         | 3.8GB   | `ollama run codellama`            |
| Llama 2 Uncensored    | 7B         | 3.8GB   | `ollama run llama2-uncensored`    |
| LLaVA                 | 7B         | 4.5GB   | `ollama run llava`                |
| Solar                 | 10.7B      | 6.1GB   | `ollama run solar`                |

## Contribuição

Sinta-se à vontade para contribuir com este projeto. Abra issues e pull requests para melhorias e correções.

## Licença

Este projeto está licenciado sob a licença [Apache 2.0](LICENSE).

---

# ![Logo da Sua Empresa](https://scoras.com.br/wp-content/uploads/2024/09/Scoras_academy.png)
