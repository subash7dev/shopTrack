from common.responses import ApiResponse


class BaseService:

    model = None
    serializer_class = None

    @classmethod
    def get_all(cls):

        queryset = cls.model.objects.all()

        serializer = cls.serializer_class(
            queryset,
            many=True,
        )

        return ApiResponse.success(
            data=serializer.data,
            message=f"{cls.model.__name__} list fetched successfully.",
        )

    @classmethod
    def retrieve(cls, instance):

        serializer = cls.serializer_class(instance)

        return ApiResponse.success(
            data=serializer.data,
            message=f"{cls.model.__name__} fetched successfully.",
        )

    @classmethod
    def create(cls, user, data):

        serializer = cls.serializer_class(data=data)

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save(
            created_by=user,
            updated_by=user,
        )

        return ApiResponse.success(
            data=serializer.data,
            message=f"{cls.model.__name__} created successfully.",
            status=201,
        )

    @classmethod
    def update(cls, user, instance, data):

        serializer = cls.serializer_class(
            instance,
            data=data,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save(
            updated_by=user,
        )

        return ApiResponse.success(
            data=serializer.data,
            message=f"{cls.model.__name__} updated successfully.",
        )

    @classmethod
    def partial_update(cls, user, instance, data):

        serializer = cls.serializer_class(
            instance,
            data=data,
            partial=True,
        )

        serializer.is_valid(
            raise_exception=True,
        )

        serializer.save(
            updated_by=user,
        )

        return ApiResponse.success(
            data=serializer.data,
            message=f"{cls.model.__name__} updated successfully.",
        )

    @classmethod
    def delete(cls, instance):

        instance.soft_delete()

        return ApiResponse.success(
            message=f"{cls.model.__name__} deleted successfully.",
        )