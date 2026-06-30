from decimal import Decimal

from django.db import transaction

from common.responses import ApiResponse

from products.models import Product

from .models import Order, OrderItem
from .serializers import OrderSerializer


class OrderService:

    @staticmethod
    @transaction.atomic
    def create(user, items):

        if not items:
            return ApiResponse.error(
                message="Order items are required.",
                status=400,
            )

        order = Order.objects.create(
            user=user
        )

        total = Decimal("0.00")

        for item in items:

            product = Product.objects.select_for_update().get(
                pk=item["product"]
            )

            quantity = int(item["quantity"])

            if product.stock_quantity < quantity:

                raise ValueError(
                    f"{product.name} is out of stock."
                )

            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                unit_price=product.price,
                subtotal=product.price * quantity,
            )

            product.stock_quantity -= quantity

            product.save()

            total += product.price * quantity

        order.total_amount = total

        order.save()

        serializer = OrderSerializer(order)

        return ApiResponse.success(
            data=serializer.data,
            message="Order placed successfully.",
            status=201,
        )

    @staticmethod
    def list(user):

        if user.role == "ADMIN":
            queryset = Order.objects.prefetch_related(
                "items"
            )

        else:
            queryset = Order.objects.prefetch_related(
                "items"
            ).filter(
                user=user
            )

        serializer = OrderSerializer(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data
        )

    @staticmethod
    def retrieve(order):

        serializer = OrderSerializer(order)

        return ApiResponse.success(
            data=serializer.data
        )