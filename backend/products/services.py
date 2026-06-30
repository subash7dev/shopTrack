from common.services import BaseService
from common.utils import generate_slug

from .models import Product
from .serializers import ProductSerializer


class ProductService(BaseService):

    model = Product
    serializer_class = ProductSerializer

    @classmethod
    def create(cls, user, data):

        data = data.copy()

        if not data.get("slug") and data.get("name"):
            data["slug"] = generate_slug(data["name"])

        return super().create(user, data)

    @classmethod
    def update(cls, user, instance, data):

        data = data.copy()

        if data.get("name") and not data.get("slug"):
            data["slug"] = generate_slug(data["name"])

        return super().update(user, instance, data)

    @classmethod
    def partial_update(cls, user, instance, data):

        data = data.copy()

        if data.get("name") and not data.get("slug"):
            data["slug"] = generate_slug(data["name"])

        return super().partial_update(user, instance, data)