from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Product,
)
from ..serializers import (
    ProductSerializer,
)

class AddProduct(APIView):
    def post(self, request: Request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Product created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': 'Product not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class ProductList(APIView):
    def get(self, request: Request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response({
            'status': True,
            'message': 'Product list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class GetProduct(APIView):
    def get(self, request: Request, sub_category_id):
        product = Product.objects.get(sub_category=sub_category_id)
        serializer = ProductSerializer(product)
        return Response({
            'status': True,
            'message': 'Product',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class UpdateProduct(APIView):
    def post(self, request: Request):
        data = request.data
        product = Product.objects.get(id=data['id'])
        serializer = ProductSerializer(product, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Product updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': 'Product not updated',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteProduct(APIView):
    def post(self, request: Request):
        data = request.data
        product = Product.objects.get(id=data['id'])
        product.delete()
        return Response({
            'status': True,
            'message': 'Product deleted successfully',
            'data': []
        }, status=status.HTTP_200_OK)
    