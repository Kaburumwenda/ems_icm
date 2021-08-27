
from django.conf import settings
from django.contrib.auth.models import User
from django.http import Http404
from django.shortcuts import render

from rest_framework import status, authentication, permissions
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Order, OrderItem
from .serializers import OrderSerializer,  MyOrderSerializer, MyOrderItemSerializer


@api_view(['POST'])
@authentication_classes([authentication.TokenAuthentication])
@permission_classes([permissions.IsAuthenticated])
def checkout(request):
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        paid_amount = sum(item.get('quantity') * item.get('product').Sprice for item in serializer.validated_data['items'])

        try:
            serializer.save(user=request.user, paid_amount=paid_amount)

            return Response(serializer.data)
        except Exception:
            return Response(serializer.errors)
    
    return Response(serializer.errors)


class OrdersList(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)


class LatestOrder(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        orders = Order.objects.filter(user=request.user)[:1]
        serializer = MyOrderSerializer(orders, many=True)
        return Response(serializer.data)


class OrdersItem(APIView):

    def get(self, request,id, format=None):
        orders = OrderItem.objects.filter(order_id=id)
        serializer = MyOrderItemSerializer(orders, many=True)
        return Response(serializer.data)
