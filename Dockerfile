# Use a imagem base do Python 3.11
FROM python:3.11-slim

# Configurações do ambiente
ENV PYTHONUNBUFFERED 1

# Instale as dependências do sistema
RUN apt-get update

# Copie o código do aplicativo para o contêiner
WORKDIR /app
COPY . /app

# Instale o Poetry
RUN pip install poetry

# Configure o Poetry para não usar a confirmação interativa
RUN poetry config virtualenvs.create false

# Instale as dependências do projeto com Poetry
RUN poetry install --no-dev

# Exponha a porta do aplicativo
EXPOSE 8000

# Inicie o servidor FastAPI
CMD ["poetry", "run", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
