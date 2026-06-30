from rest_framework import serializers

from .models import Order, OrderItem
from products.models import Product


class OrderItemSerializer(serializers.ModelSerializer):

    product_name = serializers.ReadOnlyField(
        source="product.name"
    )

    class Meta:
        model = OrderItem
        fields = [
            "id",
            "product",
            "product_name",
            "quantity",
            "unit_price",
            "subtotal",
        ]
        read_only_fields = (
            "unit_price",
            "subtotal",
        )


class OrderSerializer(serializers.ModelSerializer):

    items = OrderItemSerializer(
        many=True,
        read_only=True,
    )

    class Meta:
        model = Order

        fields = [
            "id",
            "user",
            "status",
            "total_amount",
            "items",
            "created_at",
            "updated_at",
        ]

        read_only_fields = (
            "user",
            "total_amount",
            "created_at",
            "updated_at",
        )