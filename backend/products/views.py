from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

from common.viewsets import BaseViewSet

from .models import Product
from .serializers import ProductSerializer
from .services import ProductService

from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .filters import ProductFilter


@extend_schema_view(
    list=extend_schema(tags=["Products"], summary="List Products"),
    retrieve=extend_schema(tags=["Products"], summary="Retrieve Product"),
    create=extend_schema(tags=["Products"], summary="Create Product"),
    update=extend_schema(tags=["Products"], summary="Update Product"),
    partial_update=extend_schema(tags=["Products"], summary="Partial Update Product"),
    destroy=extend_schema(tags=["Products"], summary="Delete Product"),
)
class ProductViewSet(BaseViewSet):
    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
        ]

    filterset_class = ProductFilter

    search_fields = [
    "name",
    "description",
    "category__name",
]

    ordering_fields = [
    "price",
    "stock",
    "created_at",
    "updated_at",
]

    ordering = [
    "-created_at",
]

    ordering_fields = [
    "price",
    "stock",
    "created_at",
]

    ordering = [
    "-created_at",
]

    queryset = Product.objects.select_related(
        "category"
    )

    serializer_class = ProductSerializer

    service = ProductService