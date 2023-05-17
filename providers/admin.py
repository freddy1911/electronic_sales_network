from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from providers.models import Company, Products, CompanyProducts


class ProductsInline(admin.StackedInline):
    """
    Вывод нескольких строк для поля product
    """
    model = CompanyProducts
    extra = 0


class BaseCompanyAdmin(admin.ModelAdmin):
    """
    Настройка админ-панели для работы с моделями приложения providers
    """
    list_display = ('title', 'level', 'debt', 'provider_link')
    list_filter = ('city',)
    fieldsets = [
        (None, {'fields': ['level', 'title', 'debt', 'provider']}),
        ('Контакты', {'fields': ['country', 'email', 'city', 'street', 'house_number']}),
        ('Сотрудник', {'fields': ['user']}),
    ]

    def provider_link(self, obj):
        """
        Реализация ссылки на поставщика
        """
        if obj.provider:
            url = reverse(
                'admin:providers_company_change',
                args=(obj.provider.id, )
            )

            return mark_safe(u'<a href="{0}">{1}</a>'.format(url, obj.provider))

    actions = ['DebtZero']

    @admin.action(description='Списать задолженность')
    def DebtZero(self, request, queryset):
        """
        Action - списание задолженности
        """
        queryset.update(debt=0)

    inlines = [ProductsInline]


admin.site.register(Company, BaseCompanyAdmin)
admin.site.register(Products)
