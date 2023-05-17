from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from electronic_sales_network.users.models import User


@admin.register(User)
class BaseUserAdmin(UserAdmin):
    """
    Админ-панель для модели User
    """
    list_display = ('username', 'first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_superuser')
    readonly_fields = ('last_login', 'date_joined',)
    fieldsets = (
        (
            None,
            {'fields': ('username', 'password')}
        ),
        (
            'Персональные Данные',
            {'fields': ('first_name', 'last_name', 'email')}
        ),
        (
            'Разрешения',
            {'fields': ('is_active', 'is_superuser', 'is_staff')}
        ),
        (
            'Подробная Информация',
            {'fields': ('last_login', 'date_joined')}
        ),
    )

    admin.site.unregister(Group)
