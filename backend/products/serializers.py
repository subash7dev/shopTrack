from rest_framework import serializers

from common.validators import (
    validate_positive_price,
    validate_stock,
)

from .models import Product


class ProductSerializer(serializers.ModelSerializer):

    category_name = serializers.CharField(
        source="category.name",
        read_only=True,
    )

    price = serializers.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[validate_positive_price],
    )

    stock_quantity = serializers.IntegerField(
        validators=[validate_stock],
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
            "id",
            "category_name",
            "created_at",
            "updated_at",
        )

    def validate_name(self, value):
        value = value.strip()

        if len(value) < 3:
            raise serializers.ValidationError(
                "Product name must contain at least 3 characters."
            )

        return value

    def validate_slug(self, value):

        queryset = Product.objects.filter(slug=value)

        if self.instance:
            queryset = queryset.exclude(pk=self.instance.pk)

        if queryset.exists():
            raise serializers.ValidationError(
                "A product with this slug already exists."
            )

        return value

    def validate(self, attrs):

        if attrs.get("price") and attrs.get("stock_quantity"):

            if attrs["price"] <= 0:
                raise serializers.ValidationError(
                    {
                        "price": "Price must be greater than zero."
                    }
                )

            if attrs["stock_quantity"] < 0:
                raise serializers.ValidationError(
                    {
                        "stock_quantity": "Stock cannot be negative."
                    }
                )

        return attrs