from rest_framework import serializers


def validate_positive_price(value):

    if value <= 0:
        raise serializers.ValidationError(
            "Price must be greater than zero."
        )

    return value


def validate_stock(value):

    if value < 0:
        raise serializers.ValidationError(
            "Stock cannot be negative."
        )

    return value