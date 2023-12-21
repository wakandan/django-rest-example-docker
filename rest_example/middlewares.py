from django.core.cache import cache
from django.http import HttpResponseForbidden
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings


class RateLimitMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        key = f'rate_limit:{request.META["REMOTE_ADDR"]}'
        request_count = cache.get(key, 0)

        # Set the rate limit (e.g., 10 requests per minute)
        limit = settings.RATE_LIMITER_MAX_REQUESTS_PER_MIN
        expiration_time = 60  # in seconds

        if request_count >= limit:
            return HttpResponseForbidden("Rate limit exceeded")

        # Increment the request count
        cache.set(key, request_count + 1, expiration_time)

        response = self.get_response(request)
        return response
