from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "category_name",
            "name",
            "slug",
            "description",
            "price",
            "stock_quantity",
            "image",
            "is_active",
            "created_at",
            "updated_at",
        ]
        read_only_fields = (
            "created_at",
            "updated_at",
        )

    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "Price must be greater than zero."
            )
        return value

    def validate_stock_quantity(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Stock cannot be negative."
            )
        return value