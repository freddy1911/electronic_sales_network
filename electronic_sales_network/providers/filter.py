import django_filters

from electronic_sales_network.providers.models import Company


class CompanyFilter(django_filters.FilterSet):
    """
    Фильтр по полю Город
    """
    title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Company
        fields = ['city', ]
