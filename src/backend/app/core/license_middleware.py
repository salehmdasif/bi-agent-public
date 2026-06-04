"""
License enforcement middleware.
Blocks all non-exempt API routes when the deployment license is invalid.
"""
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response


EXEMPT_PATHS = {
    "/api/v1/health",
    "/api/v1/auth/login",
    "/api/v1/auth/refresh",
    "/api/v1/public/license/activate",
    "/api/docs",
    "/api/redoc",
    "/",
}


class LicenseMiddleware(BaseHTTPMiddleware):
    """
    ASGI middleware that validates the deployment license on every request.

    Exempt paths (health check, login, license activation) bypass validation.
    All other routes return 403 if the license is not valid.

    The license status is cached in Redis for one hour to avoid a database
    round-trip on every request.

    Note:
        Middleware implementation is proprietary and not included in this public version.
    """

    async def dispatch(self, request: Request, call_next) -> Response:
        """
        Validate license and pass request through or reject it.

        Note:
            Implementation is proprietary and not included in this public version.
        """
        raise NotImplementedError("Proprietary implementation")
