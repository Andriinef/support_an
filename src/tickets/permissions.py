from rest_framework.permissions import BasePermission

from customusers.constants import Role
from tickets.models import Ticket


class RoleIsAdmin(BasePermission):
    def has_permission(self, request, view):
        return bool(Role.ADMIN)


class RoleIsManager(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.MANAGER


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj: Ticket):
        return obj.customer == request.user


class RoleIsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == Role.USER
