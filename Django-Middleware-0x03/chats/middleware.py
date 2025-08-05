"""
Custom Middleware for Chats App
"""
from datetime import datetime, time
from ipaddress import ip_address

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
        if current_time >= 21 or current_time < 6:
            return JsonResponse(
                data={"error": "You do not have access at this time."},
                status=status.HTTP_403_FORBIDDEN)
        else:
            response = self.get_response(request)
            return response


class OffensiveLanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.record = {

        }
        self.message_count = 0
        self.start_time = datetime.now()

    def __call__(self, request):
        if request.method == 'POST' and request.path == '/api/messages/':
            ip_addr = get_client_ip(request)
            if not self.record.get(ip_addr):
                self.record[ip_addr] = {
                    'time': datetime.now(),
                    'count': 0,
                }
            user = self.record.get(ip_addr)

            clock = datetime.now()
            diff = clock - user['time']
            # total_minutes = diff.total_seconds() // 60
            # hours = total_minutes // 60
            # minutes = total_minutes % 60
            # seconds = int(diff.total_seconds() % 60)

            if (diff.total_seconds()) // 60 <= 10:
                user['count'] += 1
                if user['count'] > 5:
                    return JsonResponse(
                        data={"error": "Message Limit Reached."},
                        status=status.HTTP_403_FORBIDDEN)
            else:
                user['count'] = 1
                user['time'] = datetime.now()

        response = self.get_response(request)
        return response


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


class RolepermissionMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'POST' and not request.path.startswith('/admin/'):
            allowed_roles = ['admin', 'moderator']

            if request.user.role.lower not in allowed_roles:
                return JsonResponse(
                    data={"error": "You do not the required permission set."},
                    status=status.HTTP_403_FORBIDDEN)

        response = self.get_response(request)
        return response
