import os
DATABASE_URL = os.getenv("DATABASE_URL", 'sqlite:///./test.sqlite')
os.environ["DATABASE_URL"] = DATABASE_URL
os.environ["TEST_DATABASE_URL"] = 'true'

import pytest
from main import app
from typing import Generator
from database import config_database
from fastapi.testclient import TestClient


@pytest.fixture(scope="function")
def client() -> Generator:
    config_database(drop_all=True)
    with TestClient(app) as c:
        yield c


@pytest.fixture(scope="function")
def cleanup_test_db():
    yield
    os.remove("./test.sqlite")