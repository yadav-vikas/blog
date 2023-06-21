from rest_framework import permissions

class IsAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin
    
class IsSupervisor(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_supervisor
    
class IsUser(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_user