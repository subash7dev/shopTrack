from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Product
from .permissions import IsAdmin
from .serializers import ProductSerializer


class ProductViewSet(ModelViewSet):

    queryset = Product.objects.select_related(
        "category"
    )

    serializer_class = ProductSerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]