from django.db.models import Count, Sum

from common.responses import ApiResponse

from users.models import User
from categories.models import Category
from products.models import Product
from orders.models import Order


class ReportService:

    @staticmethod
    def dashboard():

        data = {
            "total_users": User.objects.count(),
            "total_categories": Category.objects.count(),
            "total_products": Product.objects.count(),
            "total_orders": Order.objects.count(),

            "low_stock_products": Product.objects.filter(
                stock__lte=10
            ).count(),

            "active_products": Product.objects.filter(
                is_deleted=False
            ).count(),
        }

        return ApiResponse.success(
            data=data,
            message="Dashboard data fetched successfully.",
        )