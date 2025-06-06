FROM python:3.12-slim

WORKDIR /app

# Instalar uv com pip install --no-cache-dir para reduzir tamanho
RUN pip install --no-cache-dir uv

# Copy requirements first for better caching
COPY requirements.txt .

# Usar uv pip compile para gerar requirements.txt otimizado
# e uv pip sync para instalar apenas o necessário
RUN uv pip compile requirements.txt -o requirements.lock && \
    uv pip sync --system requirements.lock && \
    rm requirements.lock

# Copy the rest of the application
COPY src/ ./src/

# Set environment variables
ENV PYTHONPATH=/app/src \
    PYTHONUNBUFFERED=1 \
    # Adicionar variáveis para otimização
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=1

# Limpar caches desnecessários
RUN rm -rf /root/.cache && \
    find /usr/local -type d -name __pycache__ -exec rm -r {} +

# Verificar a instalação do langchain-core e então executar o aplicativo
CMD ["sh", "-c", "python -c 'import langchain_core; print(\"langchain-core installed successfully\")' && python src/main.py"]
