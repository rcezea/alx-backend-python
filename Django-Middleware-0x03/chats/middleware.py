"""
Custom Middleware for Chats App
"""
from datetime import datetime, time
from django.core.exceptions import PermissionDenied
from django.http import JsonResponse
from rest_framework import status
from pprint import pprint


class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # logic before request

        with open('requests.log', 'a') as log:
            content = (f'{datetime.now()} -'
                       f' User: {request.user} - Path: {request.path}\n')
            log.write(content)

        response = self.get_response(request)

        # logic after request

        return response


class RestrictAccessByTimeMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_time = datetime.now().hour
        if current_time >= 12 or current_time < 6:
            return JsonResponse(
                data={"error": "You do not have access at this time."},
                status=status.HTTP_403_FORBIDDEN)
        else:
            response = self.get_response(request)
            return response
