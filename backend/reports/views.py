from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView

from common.permissions import IsAdmin

from .services import ReportService


class DashboardView(APIView):

    permission_classes = [
        IsAuthenticated,
        IsAdmin,
    ]

    def get(self, request):

        return ReportService.dashboard()