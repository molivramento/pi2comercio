from app.models.users import User
from app.services.base import BaseService


class UserService(BaseService):
    def __init__(self):
        super().__init__(model=User,
                         path='users',
                         related=None)


user_service = UserService()
