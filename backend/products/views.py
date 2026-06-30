from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .permissions import IsAdmin
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.select_related(
        "category"
    ).all()

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_fields = [
        "category",
        "is_active",
    ]

    search_fields = [
        "name",
        "description",
        "category__name",
    ]

    ordering_fields = [
        "price",
        "stock_quantity",
        "created_at",
        "name",
    ]

    ordering = [
        "-created_at",
    ]