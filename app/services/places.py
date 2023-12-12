from app.services.base import BaseService
from app.models.places import Place


class PlaceService(BaseService):
    def __init__(self):
        super().__init__(model=Place,
                         path='places',
                         related=None)


places_service = PlaceService()