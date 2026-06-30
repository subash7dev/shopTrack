from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate

from common.logging import security_logger
from common.responses import ApiResponse

from .serializers import (
    RegisterSerializer,
    UserSerializer,
)


class UserService:

    @staticmethod
    def register(data):

        serializer = RegisterSerializer(data=data)
        serializer.is_valid(raise_exception=True)

        user = serializer.save()

        security_logger.info(
            "New user registered: %s",
            user.email,
        )

        return ApiResponse.success(
            data=UserSerializer(user).data,
            message="User registered successfully.",
            status=status.HTTP_201_CREATED,
        )

    @staticmethod
    def login(data):

        email = data.get("email")
        password = data.get("password")

        user = authenticate(
            email=email,
            password=password,
        )

        if not user:

            security_logger.warning(
                "Failed login attempt: %s",
                email,
            )

            return ApiResponse.error(
                message="Invalid email or password.",
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)

        security_logger.info(
            "User logged in: %s",
            user.email,
        )

        return ApiResponse.success(
            data={
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            },
            message="Login successful.",
        )

    @staticmethod
    def me(user):

        return ApiResponse.success(
            data=UserSerializer(user).data,
            message="User profile fetched successfully.",
        )
