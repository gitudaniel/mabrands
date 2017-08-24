from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Everyone has read permissions
        if request.method in permissions.SAFE_METHODS:
            return True

        # Only the owner has write permissions
        return obj.owner == request.user
