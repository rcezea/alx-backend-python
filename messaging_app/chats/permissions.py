"""
Custom Django Permission Classes
for User Authentication AND Authorization
"""

from rest_framework.permissions import BasePermission


class IsParticipantOfConversation(BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsSenderOfMessage(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user

    # def has_permission(self, request, view):
    #     return not bool(request.user and request.user.is_authenticated)
