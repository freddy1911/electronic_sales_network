from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from electronic_sales_network.providers.filter import CompanyFilter
from electronic_sales_network.providers.models import Company, Products
from electronic_sales_network.providers.permissions import ActiveUsers
from electronic_sales_network.providers.serializers import CompanySerializer, ProductsSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    filter_backends = (DjangoFilterBackend,)
    filterset_class = CompanyFilter
    permission_classes = ActiveUsers, IsAuthenticated,

    serializer_class = CompanySerializer


class ProductsViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductsSerializer
    permission_classes = ActiveUsers, IsAuthenticated,
