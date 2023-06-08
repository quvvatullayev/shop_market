from rest_framework import serializers
from .models import (
    User,
    Category,
    Sub_category,
    Product,
    Cart,
    Order,
)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    # sub_category = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id', 'name', 'discription', 'image']

class Sub_categorySerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False, read_only=True)
    class Meta:
        model = Sub_category
        fields = ['id', 'name', 'discription', 'image', 'category']

class ProductSerializer(serializers.ModelSerializer):
    # category = CategorySerializer()
    sub_category = Sub_categorySerializer(many=False, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'name', 'discription', 'image', 'price', 'sub_category']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'