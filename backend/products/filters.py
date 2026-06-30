import django_filters

from .models import Product


class ProductFilter(django_filters.FilterSet):

    category = django_filters.NumberFilter(
        field_name="category_id"
    )

    min_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="gte",
    )

    max_price = django_filters.NumberFilter(
        field_name="price",
        lookup_expr="lte",
    )

    min_stock = django_filters.NumberFilter(
        field_name="stock",
        lookup_expr="gte",
    )

    max_stock = django_filters.NumberFilter(
        field_name="stock",
        lookup_expr="lte",
    )

    class Meta:
        model = Product
        fields = [
            "category",
            "min_price",
            "max_price",
            "min_stock",
            "max_stock",
        ]