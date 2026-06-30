from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
)

from rest_framework.views import APIView

from .services import UserService


class RegisterView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        return UserService.register(
            request.data
        )


class LoginView(APIView):

    permission_classes = [AllowAny]

    def post(self, request):

        return UserService.login(
            request.data
        )


class MeView(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):

        return UserService.me(
            request.user
        )