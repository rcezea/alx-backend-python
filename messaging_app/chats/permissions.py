"""
Custom Django Permission Classes
for User Authentication AND Authorization
"""

from rest_framework import permissions


class IsParticipantOfConversation(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user in obj.participants.all()


class IsSenderOfMessage(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.sender == request.user
