from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view

from . import products
from .models import Product
from .serializers import ProductSerializer
# Create your views here.


def home(request):
    return JsonResponse('Hello', safe=False)


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
