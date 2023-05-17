from django.urls import path, include
from rest_framework.routers import SimpleRouter

from providers.views import CompanyViewSet, ProductsViewSet

company_router = SimpleRouter()
company_router.register('company', CompanyViewSet, basename='company')

product_router = SimpleRouter()
product_router.register("product", ProductsViewSet)


urlpatterns = [
    path('', include(company_router.urls)),
    path("", include(product_router.urls))
]

