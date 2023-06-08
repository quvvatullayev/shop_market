from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    User,
)
from ..serializers import (
    UserSerializer,
)

class AddUser(APIView):
    def post(self, request: Request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'status': True,
                'message': 'User created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response({
            'status': False,
            'message': 'User not created',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class UserList(APIView):
    def get(self, request: Request, *args, **kwargs):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            'status': True,
            'message': 'User list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class GetUser(APIView):
    def get(self, request: Request, chat_id):
        user = User.objects.get(chat_id=chat_id)
        serializer = UserSerializer(user)
        return Response({
            'status': True,
            'message': 'User',
            'data': serializer.data
        }, status=status.HTTP_200_OK)
    
class UpdateUser(APIView):
    def post(self, request: Request):
        data = request.data
        user = User.objects.get(chat_id=data['chat_id'])
        serializer = UserSerializer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({
                'status': True,
                'message': 'User updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            'status': False,
            'message': 'User not updated',
            'data': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteUser(APIView):
    def post(self, request: Request):
        data = request.data
        user = User.objects.get(chat_id=data['chat_id'])
        user.delete()
        return Response({
            'status': True,
            'message': 'User deleted successfully',
            'data': []
        }, status=status.HTTP_200_OK)