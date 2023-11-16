from uuid import UUID

import ormar
from database import BaseMeta


class User(ormar.Model):
    class Meta(BaseMeta):
        tablename = "users"

    uuid: UUID = ormar.UUID(primary_key=True, editable=False)
    email: str = ormar.String(max_length=128, unique=True)
    password: str = ormar.String(max_length=128)
    first_name: str = ormar.String(max_length=64, nullable=True, server_default=None)
    last_name: str = ormar.String(max_length=64, nullable=True, server_default=None)
    is_active: bool = ormar.Boolean(default=True)
    is_staff: bool = ormar.Boolean(default=False)
    is_superuser: bool = ormar.Boolean(default=False)
