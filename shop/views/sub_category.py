from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Sub_category,
)
from ..serializers import (
    Sub_categorySerializer,
)

class AddSub_category(APIView):
    def post(self, request: Request):
        serializer = Sub_categorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class Sub_categoryList(APIView):
    def get(self, request: Request):
        sub_categorys = Sub_category.objects.all()
        serializer = Sub_categorySerializer(sub_categorys, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class GetSub_category(APIView):
    def get(self, request: Request, category_id):
        sub_category = Sub_category.objects.get(category_id=category_id)
        serializer = Sub_categorySerializer(sub_category)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UpdateSub_category(APIView):
    def post(self, request: Request):
        data = request.data
        sub_category = Sub_category.objects.get(id=data['id'])
        serializer = Sub_categorySerializer(sub_category, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
class DeleteSub_category(APIView):
    def post(self, request: Request):
        data = request.data
        sub_category = Sub_category.objects.get(id=data['id'])
        sub_category.delete()
        return Response({
            'status': True,
            'message': 'Sub_category deleted successfully',
            'data': []
        }, status=status.HTTP_200_OK)