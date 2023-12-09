from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser


from rest_framework import status
import time 

from ..models import Product
from ..serializers import ProductSerializer


@api_view(['GET'])
def getProducts(request):
    products = Product.objects.all()
    serilizer = ProductSerializer(products, many=True)
    return Response(serilizer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = Product.objects.get(_id=int(pk))
    serilizer = ProductSerializer(product, many=False)
    return Response(serilizer.data)