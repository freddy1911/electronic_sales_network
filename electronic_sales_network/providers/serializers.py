from rest_framework import serializers

from electronic_sales_network.providers.models import Company, Products


class CompanySerializer(serializers.ModelSerializer):
    products = serializers.StringRelatedField(many=True, read_only=True)
    debt = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)

    class Meta:
        model = Company
        fields = '__all__'


class ProductsSerializer(serializers.ModelSerializer):
    companies = serializers.StringRelatedField(many=True, required=False, read_only=True)

    class Meta:
        model = Products
        fields = '__all__'
