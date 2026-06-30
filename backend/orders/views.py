from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from .models import Order
from .serializers import OrderSerializer
from .services import OrderService


class OrderViewSet(ModelViewSet):

    queryset = Order.objects.prefetch_related(
        "items"
    )

    serializer_class = OrderSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def list(self, request, *args, **kwargs):

        return OrderService.list(
            request.user
        )

    def retrieve(self, request, *args, **kwargs):

        return OrderService.retrieve(
            self.get_object()
        )

    def create(self, request, *args, **kwargs):

        return OrderService.create(
            request.user,
            request.data.get("items", []),
        )