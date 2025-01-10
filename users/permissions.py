from rest_framework.permissions import BasePermission


class IsModer(BasePermission):

    def has_permission(self, request, view):
        return request.user.is_superuser

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user


class IsSelfUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj == request.user


class IsActiveUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_active
