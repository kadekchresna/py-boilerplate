
import time
from starlette.middleware.base import BaseHTTPMiddleware
from collections import defaultdict
from fastapi import Request
from fastapi.responses import JSONResponse


class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, max_requests: int, time_window: int):
        super().__init__(app)
        self.max_requests = max_requests
        self.time_window = time_window
        self.ip_access_times = defaultdict(list)

    async def dispatch(self, request: Request, call_next):
        client_ip = request.client.host
        current_time = time.time()

        # Record request time
        access_times = self.ip_access_times[client_ip]
        access_times.append(current_time)

        # Filter requests within the time window
        self.ip_access_times[client_ip] = [
            t for t in access_times if t > current_time - self.time_window
        ]

        if len(self.ip_access_times[client_ip]) > self.max_requests:
            return  JSONResponse(status_code=429, content="Too many requests")

        return await call_next(request)
