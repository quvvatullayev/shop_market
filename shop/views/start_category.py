from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import status
from ..models import (
    Category,
    Sub_category,
    Product,
)
from ..serializers import (
    CategorySerializer,
    Sub_categorySerializer,
    ProductSerializer
)

class StartCategory(APIView):
    def get(self, request: Request):
        data = {'result':[]}
        category_all = Category.objects.all()
        categorys = CategorySerializer(category_all, many = True).data
        for category in categorys:
            data['result'].append(category)
            sub_category_all = Sub_category.objects.filter(category = category['id'])
            sub_categorys = Sub_categorySerializer(sub_category_all, many = True).data
            sub_cate = []
            for sub_category in sub_categorys:
                product_all = Product.objects.filter(sub_category = sub_category['id'])
                products = ProductSerializer(product_all, many = True)
                sub_category['products'] = products.data
                sub_cate.append(sub_category)
            category['sub_category'] = sub_cate
            data['result'].append(category)
        return Response(data=data, status=status.HTTP_200_OK)


