from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from rest_framework import generics
from ..models import (
    Contact_store,
)
from ..serializers import (
    Contact_storeSerializer,
)

class Contact_storeList(APIView):
    def get(self, request: Request):
        contact_stores = Contact_store.objects.all()
        serializer = Contact_storeSerializer(contact_stores, many=True)
        return Response({
            'status': True,
            'message': 'Contact_store list',
            'data': serializer.data
        }, status=status.HTTP_200_OK)