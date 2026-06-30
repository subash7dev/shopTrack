from django.db.models import Avg, Sum

from common.responses import ApiResponse

from users.models import User
from categories.models import Category
from products.models import Product


class ReportService:

    @staticmethod
    def dashboard():

        cards = {
            "total_users": User.objects.count(),
            "total_categories": Category.objects.count(),
            "total_products": Product.objects.count(),

            "active_products": Product.objects.filter(
                is_active=True
            ).count(),

            "inactive_products": Product.objects.filter(
                is_active=False
            ).count(),

            "low_stock_products": Product.objects.filter(
                stock_quantity__lte=10
            ).count(),

            "out_of_stock_products": Product.objects.filter(
                stock_quantity=0
            ).count(),

            "inventory_value": Product.objects.aggregate(
                total=Sum("price")
            )["total"] or 0,

            "average_price": Product.objects.aggregate(
                avg=Avg("price")
            )["avg"] or 0,
        }

        recent_products = list(
            Product.objects.values(
                "id",
                "name",
                "price",
                "stock_quantity",
            ).order_by("-created_at")[:5]
        )

        return ApiResponse.success(
            data={
                "cards": cards,
                "recent_products": recent_products,
            },
            message="Dashboard loaded successfully.",
        )