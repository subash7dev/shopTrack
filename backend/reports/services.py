from django.db.models import Count, Sum

from products.models import Product
from categories.models import Category
from orders.models import Order

from common.responses import ApiResponse


class DashboardService:

    @staticmethod
    def dashboard():

        data = {

            "total_products": Product.objects.count(),

            "total_categories": Category.objects.count(),

            "total_orders": Order.objects.count(),

            "pending_orders": Order.objects.filter(
                status="PENDING"
            ).count(),

            "processing_orders": Order.objects.filter(
                status="PROCESSING"
            ).count(),

            "shipped_orders": Order.objects.filter(
                status="SHIPPED"
            ).count(),

            "delivered_orders": Order.objects.filter(
                status="DELIVERED"
            ).count(),

            "cancelled_orders": Order.objects.filter(
                status="CANCELLED"
            ).count(),

            "low_stock_products": Product.objects.filter(
                stock_quantity__lte=10
            ).count(),

            "revenue": Order.objects.filter(
                status="DELIVERED"
            ).aggregate(
                total=Sum("total_amount")
            )["total"] or 0,
        }

        return ApiResponse.success(
            data=data,
            message="Dashboard loaded successfully.",
        )