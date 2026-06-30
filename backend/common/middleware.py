import time

from common.logging import (
    app_logger,
    error_logger,
)


class RequestLoggingMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        start = time.time()

        response = self.get_response(request)

        duration = round(
            time.time() - start,
            3,
        )

        app_logger.info(
            "%s %s | %s | %.3fs",
            request.method,
            request.path,
            response.status_code,
            duration,
        )

        return response

    def process_exception(self, request, exception):

        error_logger.exception(
            "%s %s",
            request.method,
            request.path,
        )