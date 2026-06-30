from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .models import Category
from .serializers import CategorySerializer
from .permissions import IsAdmin


class CategoryViewSet(ModelViewSet):

    queryset = Category.objects.all()

    serializer_class = CategorySerializer

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]