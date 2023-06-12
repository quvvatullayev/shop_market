from rest_framework import serializers
from django.contrib.auth.models import User as AdminUser
from .models import (
    User,
    Category,
    Sub_category,
    Product,
    Cart,
    Order,
    Contact_store
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
    product = ProductSerializer(many=False, read_only=True)
    user = UserSerializer(many=False, read_only=True)
    def validate(self, attrs):
        print(attrs)
        return super().validate(attrs)
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'count', 'address', 'phone', 'status']

class CreateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'user', 'product', 'count', 'address', 'phone', 'status']

class Contact_storeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact_store
        fields = '__all__'

class AdminUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminUser
        fields = '__all__'