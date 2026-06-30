from django.db.models import Sum

from products.models import Product
from categories.models import Category
from orders.models import Order


def get_dashboard_data():

    return {

        "total_products": Product.objects.count(),

        "total_categories": Category.objects.count(),

        "total_orders": Order.objects.count(),

        "pending_orders": Order.objects.filter(
            status="PENDING"
        ).count(),

        "processing_orders": Order.objects.filter(
            status="PROCESSING"
        ).count(),

        "delivered_orders": Order.objects.filter(
            status="DELIVERED"
        ).count(),

        "low_stock": Product.objects.filter(
            stock_quantity__lte=10
        ).count(),

        "revenue": Order.objects.filter(
            status="DELIVERED"
        ).aggregate(
            total=Sum("total_amount")
        )["total"] or 0,
    }