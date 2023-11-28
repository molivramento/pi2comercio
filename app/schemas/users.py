from typing import Optional
from app.models.users import User
from app.schemas.base import BaseFilter

UserIn = User.get_pydantic(
    exclude={
        'uuid',
        'is_staff',
        'is_active',
        'is_superuser'
    }
)

UserOut = User.get_pydantic(
    exclude={
        'password'
    }
)

CreateUserIn = User.get_pydantic(
    exclude={
        'uuid'
    }
)


class UserFilter(BaseFilter):
    email: Optional[str] = None
    email__icontains: Optional[str] = None
    first_name__icontains: Optional[str] = None
    last_name__icontains: Optional[str] = None
    is_active: Optional[bool] = None
    is_staff: Optional[bool] = None
    is_superuser: Optional[bool] = None
