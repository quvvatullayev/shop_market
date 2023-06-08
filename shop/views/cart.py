from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Cart,
    User,
)
from ..serializers import (
    CartSerializer,
)

class AddCart(APIView):
    def post(self, request: Request):
        data = request.data
        chat_id = data['chat_id']
        user = User.objects.get(chat_id=chat_id)
        user_id = user.id
        data['user'] = user_id
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'Product added successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': 'Product not added',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

class CartList(APIView):
    def get(self, request: Request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response({
            'status': True,
            'message': 'Product list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class GetCart(APIView):
    def get(self, request: Request, sub_category_id):
        carts = Cart.objects.filter(sub_category=sub_category_id)
        serializer = CartSerializer(carts, many=True)
        return Response({
            'status': True,
            'message': 'Product list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class UpdateCart(APIView):
    def post(self, request: Request):
        data = request.data
        cart = Cart.objects.get(id=data['id'])
        cart.quantity = data.get('quantity', cart.quantity)
        cart.save()
        serializer = CartSerializer(cart)
        return Response({
            'status': True,
            'message': 'Product updated successfully',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class DeleteCart(APIView):
    def post(self, request: Request):
        data = request.data
        cart = Cart.objects.get(id=data['id'])
        cart.delete()
        return Response({
            'status': True,
            'message': 'Product deleted successfully',
        }, status=status.HTTP_200_OK)
    