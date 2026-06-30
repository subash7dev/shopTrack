from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.pagination import StandardPagination
from common.permissions import IsAdmin

from .models import Product
from .serializers import ProductSerializer
from .services import ProductService


@extend_schema_view(
    list=extend_schema(
        tags=["Products"],
        summary="List Products",
        description="Retrieve all available products.",
    ),
    retrieve=extend_schema(
        tags=["Products"],
        summary="Retrieve Product",
        description="Retrieve a product by its ID.",
    ),
    create=extend_schema(
        tags=["Products"],
        summary="Create Product",
        description="Create a new product.",
    ),
    update=extend_schema(
        tags=["Products"],
        summary="Update Product",
        description="Update an existing product.",
    ),
    partial_update=extend_schema(
        tags=["Products"],
        summary="Partially Update Product",
        description="Update one or more product fields.",
    ),
    destroy=extend_schema(
        tags=["Products"],
        summary="Delete Product",
        description="Delete a product.",
    ),
)
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

    def retrieve(self, request, *args, **kwargs):
        return ProductService.retrieve(
            self.get_object()
        )

    def create(self, request, *args, **kwargs):
        return ProductService.create(
            request.data
        )

    def update(self, request, *args, **kwargs):
        return ProductService.update(
            self.get_object(),
            request.data,
        )

    def partial_update(self, request, *args, **kwargs):
        return ProductService.partial_update(
            self.get_object(),
            request.data,
        )

    def destroy(self, request, *args, **kwargs):
        return ProductService.delete(
            self.get_object(),
        )