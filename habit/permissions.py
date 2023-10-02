from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return request.user == view.get_object().owner

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser
