"""
Custom Middleware for Chats App
"""
from datetime import datetime


class RequestLoggingMiddleware():
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        # logic before request

        with open('requests.log', 'a') as log:
            content = f'{datetime.now()} - User: {request.user} - Path: {request.path}\n'
            log.write(content)

        response = self.get_response(request)

        # logic after request

        return response
