import os
import ormar
import databases
import sqlalchemy
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
TEST_DATABASE_URL = os.getenv("TEST_DATABASE_URL", 'false')
database = databases.Database(DATABASE_URL, force_rollback=TEST_DATABASE_URL == 'true')
metadata = sqlalchemy.MetaData()


class BaseMeta(ormar.ModelMeta):
    metadata = metadata
    database = database


def config_database(database_url: str = DATABASE_URL, drop_all: bool = False):
    engine = sqlalchemy.create_engine(database_url)
    if drop_all:
        BaseMeta.metadata.drop_all(engine)
    BaseMeta.metadata.create_all(engine)
