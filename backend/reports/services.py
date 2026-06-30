from django.db.models import Count, Sum
from django.db.models.functions import TruncMonth

from common.responses import ApiResponse

from users.models import User
from categories.models import Category
from products.models import Product
from orders.models import Order


class ReportService:

    @staticmethod
    def dashboard():

        cards = {
            "total_users": User.objects.count(),
            "total_categories": Category.objects.count(),
            "total_products": Product.objects.count(),
            "total_orders": Order.objects.count(),
            "low_stock_products": Product.objects.filter(
                stock__lte=10
            ).count(),
        }

        recent_products = list(
            Product.objects.order_by("-created_at")
            .values(
                "id",
                "name",
                "price",
                "stock",
            )[:5]
        )

        latest_orders = list(
            Order.objects.order_by("-created_at")
            .values(
                "id",
                "created_at",
            )[:5]
        )

        return ApiResponse.success(
            data={
                "cards": cards,
                "recent_products": recent_products,
                "latest_orders": latest_orders,
            },
            message="Dashboard data fetched successfully.",
        )