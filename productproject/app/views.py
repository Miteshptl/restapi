from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializers
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.

@api_view(["GET"])
def Apioverview(req):
    api_urls={
        "all_products":"/AllProducts",
        "add_product":"/AddProduct",
        "update_product":"/UpdateProduct/pk",
        "delete_product":"/product/pk/delete"
    }
    return Response(api_urls)


class AllProductview(generics.ListAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers

class AddProductview(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers


class UpdateProduct(generics.ListCreateAPIView):
    queryset=Product.objects.all()
    serializer_class=ProductSerializers
    partial=True