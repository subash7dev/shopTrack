from common.services import BaseService
from common.utils import generate_slug

from .models import Product
from .serializers import ProductSerializer


class ProductService(BaseService):

    model = Product
    serializer_class = ProductSerializer

    @classmethod
    def get_all(cls, queryset):
        """
        Returns the filtered queryset received from the ViewSet.
        Filtering, searching, ordering and pagination are handled
        by DRF before reaching this service.
        """
        return super().get_all(queryset)

    @classmethod
    def retrieve(cls, instance):
        return super().retrieve(instance)

    @classmethod
    def create(cls, user, data):

        data = data.copy()

        if data.get("name") and not data.get("slug"):
            data["slug"] = generate_slug(data["name"])

        return super().create(user, data)

    @classmethod
    def update(cls, user, instance, data):

        data = data.copy()

        if data.get("name") and not data.get("slug"):
            data["slug"] = generate_slug(data["name"])

        return super().update(
            user,
            instance,
            data,
        )

    @classmethod
    def partial_update(cls, user, instance, data):

        data = data.copy()

        if data.get("name") and not data.get("slug"):
            data["slug"] = generate_slug(data["name"])

        return super().partial_update(
            user,
            instance,
            data,
        )

    @classmethod
    def delete(cls, instance):
        return super().delete(instance)