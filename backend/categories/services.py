from common.responses import ApiResponse

from .models import Category
from .serializers import CategorySerializer


class CategoryService:

    @staticmethod
    def get_all():

        categories = Category.objects.all()

        serializer = CategorySerializer(
            categories,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
            message="Categories fetched successfully.",
        )

    @staticmethod
    def create(data):

        serializer = CategorySerializer(
            data=data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save()

        return ApiResponse.success(
            data=serializer.data,
            message="Category created successfully.",
            status=201,
        )

    @staticmethod
    def update(instance, data):

        serializer = CategorySerializer(
            instance,
            data=data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save()

        return ApiResponse.success(
            data=serializer.data,
            message="Category updated successfully.",
        )

    @staticmethod
    def delete(instance):

        instance.delete()

        return ApiResponse.success(
            message="Category deleted successfully.",
        )