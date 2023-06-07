from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Category,
)
from ..serializers import (
    CategorySerializer,
)

class AddCategory(APIView):
    def post(self, request: Request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

class CategoryList(APIView):
    def get(self, request: Request):
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetCategory(APIView):
    def get(self, request: Request, category_id):
        category = Category.objects.get(id=category_id)
        serializer = CategorySerializer(category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateCategory(APIView):
    def post(self, request: Request):
        data = request.data
        category = Category.objects.get(id=data['id'])
        serializer = CategorySerializer(category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteCategory(APIView):
    def post(self, request: Request):
        data = request.data
        category = Category.objects.get(id=data['id'])
        category.delete()
        return Response({
            'status': True,
            'message': 'Category deleted successfully',
            'data': []
        }, status=status.HTTP_200_OK)