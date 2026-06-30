from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.pagination import StandardPagination
from common.permissions import IsAdmin

from .models import Product
from .serializers import ProductSerializer
from .services import ProductService


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.select_related(
        "category"
    ).all()

    serializer_class = ProductSerializer

    pagination_class = StandardPagination

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    def list(self, request, *args, **kwargs):
        return ProductService.get_all()

    def create(self, request, *args, **kwargs):
        return ProductService.create(
            request.data
        )

    def update(self, request, *args, **kwargs):
        return ProductService.update(
            self.get_object(),
            request.data,
        )

    def destroy(self, request, *args, **kwargs):
        return ProductService.delete(
            self.get_object(),
        )