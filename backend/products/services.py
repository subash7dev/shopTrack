from django.shortcuts import get_object_or_404


from common.responses import ApiResponse
from common.utils import generate_slug

from .models import Product
from .serializers import ProductSerializer


class ProductService:

    

    @staticmethod
    def get_all():
        products = Product.objects.select_related(
            "category"
        )

        serializer = ProductSerializer(
            products,
            many=True,
        )

        return ApiResponse.success(
              data=serializer.data,
              message="Products fetched successfully.",
          )

    @staticmethod
    def retrieve(instance):

        serializer = ProductSerializer(instance)

        return ApiResponse.success(
            data=serializer.data,
            message="Product fetched successfully.",
        )

    @staticmethod
    def create(user, data):

        data = data.copy()

        if not data.get("slug") and data.get("name"):
            data["slug"] = generate_slug(data["name"])

        serializer = ProductSerializer(
            data=data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save(created_by=user,updated_by=user,)

        return ApiResponse.success(
            data=serializer.data,
            message="Product created successfully.",
            status=201,
        )

    @staticmethod
    def update(user, instance, data):

        data = data.copy()

        if not data.get("slug") and data.get("name"):
            data["slug"] = generate_slug(data["name"])

        serializer = ProductSerializer(
            instance,
            data=data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save(updated_by=user,)

        return ApiResponse.success(
            data=serializer.data,
            message="Product updated successfully.",
        )

    @staticmethod
    def partial_update(user,instance, data):

        data = data.copy()

        if data.get("name") and not data.get("slug"):
            data["slug"] = generate_slug(data["name"])

        serializer = ProductSerializer(
            instance,
            data=data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save(updated_by=user, )

        return ApiResponse.success(
            data=serializer.data,
            message="Product updated successfully.",
        )

    @staticmethod
    def delete(instance):

        instance.delete()

        return ApiResponse.success(
            message="Product deleted successfully.",
        )