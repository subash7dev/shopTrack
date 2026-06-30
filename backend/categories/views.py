from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.permissions import IsAdmin

from .models import Category
from .serializers import CategorySerializer
from .services import CategoryService


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    def list(self, request, *args, **kwargs):
        return CategoryService.get_all()

    def create(self, request, *args, **kwargs):
        return CategoryService.create(request.data)

    def update(self, request, *args, **kwargs):
        return CategoryService.update(
            self.get_object(),
            request.data,
        )

    def destroy(self, request, *args, **kwargs):
        return CategoryService.delete(
            self.get_object(),
        )