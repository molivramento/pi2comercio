# pi2comercio

## Getting Started

To start the server, open the project folder in the terminal and run the following commands:

```shell
pip install poetry
poetry install
poetry run uvicorn main:app --reload
```

# Containers

Windows: https://docs.docker.com/desktop/install/windows-install/
Mac: https://docs.docker.com/desktop/install/mac-install/
Linux (Ubundo based): https://docs.docker.com/engine/install/ubuntu/

To start the containers, open the project folder in the terminal and run the following commands:

```shell
docker-compose up -d --build
```

