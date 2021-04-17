from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        # fields = '__all__'
        fields = ('pk', 'category', 'name', 'image', 'description', 'price', 'countInStock', 'createdAt')
        # fields = ('pk', 'category', 'name', 'description', 'price', 'countInStock', 'createdAt')
