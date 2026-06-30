from rest_framework.views import exception_handler
from rest_framework import status
from rest_framework.response import Response


class ShopTrackException(Exception):
    """Base exception for ShopTrack."""
    pass


class NotFoundException(ShopTrackException):
    pass


class OutOfStockException(ShopTrackException):
    pass


class ValidationException(ShopTrackException):
    pass


class PermissionDeniedException(ShopTrackException):
    pass


def custom_exception_handler(exc, context):

    response = exception_handler(exc, context)

    if response is not None:
        return Response(
            {
                "success": False,
                "message": "Request failed.",
                "errors": response.data,
            },
            status=response.status_code,
        )

    if isinstance(exc, OutOfStockException):
        return Response(
            {
                "success": False,
                "message": str(exc),
            },
            status=status.HTTP_400_BAD_REQUEST,
        )

    if isinstance(exc, NotFoundException):
        return Response(
            {
                "success": False,
                "message": str(exc),
            },
            status=status.HTTP_404_NOT_FOUND,
        )

    if isinstance(exc, PermissionDeniedException):
        return Response(
            {
                "success": False,
                "message": str(exc),
            },
            status=status.HTTP_403_FORBIDDEN,
        )

    return Response(
        {
            "success": False,
            "message": "Internal Server Error",
        },
        status=status.HTTP_500_INTERNAL_SERVER_ERROR,
    )