from rest_framework import status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth import authenticate

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

        return Response(
            UserSerializer(user).data,
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

            return Response(
                {
                    "detail": "Invalid email or password."
                },
                status=status.HTTP_401_UNAUTHORIZED,
            )

        refresh = RefreshToken.for_user(user)

        return Response(
            {
                "refresh": str(refresh),
                "access": str(refresh.access_token),
                "user": UserSerializer(user).data,
            }
        )

    @staticmethod
    def me(user):

        return Response(
            UserSerializer(user).data
        )