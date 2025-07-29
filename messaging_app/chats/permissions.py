"""
Custom Django Permission Classes
for User Authentication AND Authorization
"""

from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
                request.user and
                request.user.is_authenticated and
                request.user in obj.participants.all()
        )


class IsSenderOfMessage(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
                request.user and
                request.user.is_authenticated and
                obj.sender == request.user
        )
