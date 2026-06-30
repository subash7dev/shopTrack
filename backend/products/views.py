from drf_spectacular.utils import (
    extend_schema,
    extend_schema_view,
)

from common.viewsets import BaseViewSet

from .models import Product
from .serializers import ProductSerializer
from .services import ProductService


@extend_schema_view(
    list=extend_schema(tags=["Products"], summary="List Products"),
    retrieve=extend_schema(tags=["Products"], summary="Retrieve Product"),
    create=extend_schema(tags=["Products"], summary="Create Product"),
    update=extend_schema(tags=["Products"], summary="Update Product"),
    partial_update=extend_schema(tags=["Products"], summary="Partial Update Product"),
    destroy=extend_schema(tags=["Products"], summary="Delete Product"),
)
class ProductViewSet(BaseViewSet):

    queryset = Product.objects.select_related(
        "category"
    )

    serializer_class = ProductSerializer

    service = ProductService