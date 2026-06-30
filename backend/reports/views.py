from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .dashboard import get_dashboard_data


class DashboardAPIView(APIView):

    permission_classes = [
        IsAuthenticated
    ]

    def get(self, request):

        if request.user.role != "ADMIN":
            return Response(
                {
                    "detail": "Permission denied."
                },
                status=403,
            )

        return Response(
            get_dashboard_data()
        )