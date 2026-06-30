from decimal import Decimal

from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from products.models import Product

from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderViewSet(ModelViewSet):

    serializer_class = OrderSerializer

    permission_classes = [
        IsAuthenticated,
    ]

    def get_queryset(self):

        user = self.request.user

        if user.role == "ADMIN":
            return Order.objects.prefetch_related(
                "items"
            ).all()

        return Order.objects.prefetch_related(
            "items"
        ).filter(
            user=user
        )

    def perform_create(self, serializer):

        serializer.save(
            user=self.request.user
        )

    def create(self, request, *args, **kwargs):

        items = request.data.get("items", [])

        if not items:
            return Response(
                {
                    "detail": "Order items required."
                },
                status=status.HTTP_400_BAD_REQUEST,
            )

        order = Order.objects.create(
            user=request.user
        )

        total = Decimal("0.00")

        for item in items:

            product = Product.objects.get(
                id=item["product"]
            )

            qty = int(item["quantity"])

            if product.stock_quantity < qty:

                order.delete()

                return Response(
                    {
                        "detail": f"{product.name} is out of stock."
                    },
                    status=status.HTTP_400_BAD_REQUEST,
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=qty,
                unit_price=product.price,
                subtotal=product.price * qty,
            )

            product.stock_quantity -= qty

            product.save()

            total += product.price * qty

        order.total_amount = total

        order.save()

        serializer = self.get_serializer(order)

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
        )