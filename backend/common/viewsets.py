from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from common.pagination import StandardPagination
from common.permissions import IsAdmin


class BaseViewSet(ModelViewSet):

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    pagination_class = StandardPagination

    service = None

    def list(self, request, *args, **kwargs):

       queryset = self.filter_queryset(
        self.get_queryset()
    )

       page = self.paginate_queryset(queryset)

       if page is not None:
           return self.get_paginated_response(
            self.get_serializer(page, many=True).data
        )

       return self.service.get_all(queryset)
    
    def retrieve(self, request, *args, **kwargs):
        return self.service.retrieve(
            self.get_object()
        )

    def create(self, request, *args, **kwargs):
        return self.service.create(
            request.user,
            request.data,
        )

    def update(self, request, *args, **kwargs):
        return self.service.update(
            request.user,
            self.get_object(),
            request.data,
        )

    def partial_update(self, request, *args, **kwargs):
        return self.service.partial_update(
            request.user,
            self.get_object(),
            request.data,
        )

    def destroy(self, request, *args, **kwargs):
        return self.service.delete(
            self.get_object()
        )