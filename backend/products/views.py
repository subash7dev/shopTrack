from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .serializers import ProductSerializer
from .permissions import IsAdmin


class ProductViewSet(ModelViewSet):

    queryset = (
        Product.objects
        .select_related("category")
        .all()
    )

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    filter_backends = [
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = [
        "name",
        "description",
        "category__name",
    ]

    ordering_fields = [
        "name",
        "price",
        "stock_quantity",
        "created_at",
    ]

    ordering = [
        "-created_at",
    ]