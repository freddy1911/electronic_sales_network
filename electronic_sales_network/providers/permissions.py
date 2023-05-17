from rest_framework import permissions

# реализация доступа только активных пользователей


class ActiveUsers(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_active:
            return True
        return False
