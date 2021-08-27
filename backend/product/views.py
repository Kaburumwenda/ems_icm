from django.db.models import Q
from django.http import Http404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Fakedata, Product, Category, menuEntries
from .serializers import ProductSerializer, CategorySerializer, CategoryTwoSerializer,menuSerializer, FakedataSerializer

from rest_framework import viewsets

class ProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class FakedataList(viewsets.ModelViewSet):
    queryset = Fakedata.objects.all().order_by('?')
    serializer_class = FakedataSerializer



# class FakedataList(APIView):
#     def get(self, request, format=None):
#         products = Fakedata.objects.all()
#         serializer = FakedataSerializer(products, many=True)
#         return Response(serializer.data)
#         # payload = { }
#         # payload["data"] = serializer.data
#         # return Response (payload)


class CategoryTree(APIView):
    def get(self, request):
        query = Category.objects.all()
        serializers =CategoryTwoSerializer(query, many=True)
        return Response(serializers.data)
        

class CategoryTree2(APIView):
    def get(self, request):
        query = menuEntries.objects.all()
        serializers = menuSerializer(query, many=True)
        return Response(serializers.data)



class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)
        except Category.DoesNotExist:
            raise Http404
    
    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(title__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})