from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from .serialize import ProductsSerializers
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response
from .models import Product 
from rest_framework.permissions import IsAuthenticated
from .permission import IsAdmin,isStaff
from rest_framework.permissions import IsAuthenticated

# Create your views here.
def index(request):
    return HttpResponse("Hello, World.")

class productView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.request.method in['PUT','PATCH','DELETE']:
            return [IsAdmin()]
        elif self.request.method == 'POST':
            return [isStaff()]
        return super().get_permissions()
    
    
    def post(self,request):
        serializer=ProductsSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def get(self,request,id=None):
        if id:
            try:
                product=Product.objects.get(id=id)
            except Product.DoesNotExist:
                raise Http404
            serializer=ProductsSerializers(product)
            return Response(serializer.data)
            
        else:
            product=Product.objects.all()
            serializer=ProductsSerializers(product,many=True)
            return Response(serializer.data)
    def put(self,request,id):
            try:
                product= Product.objects.get(id=id)
            except Product.DoesNotExist:
                raise Http404
            serializer=ProductsSerializers(product,data=request.data)
            if serializer.is_valid():
             serializer.save
             return Response(serializer.data,status=status.HTTP_200_OK)
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    def delete(self,request,id):
        try:
            product= Product.objects.get(id=id)
        except Product.DoesNotExist:
            raise Http404
        product.delete()
        serializer=ProductsSerializers(product)
        return Response(serializer.data)
    def patch(self,request,id):
        try:
            product= Product.objects.get(id=id)
        except Product.DoesNotExist:
                raise Http404
        serializer=ProductsSerializers(product,data=request.data,partial=True)
        if serializer.is_valid():
             serializer.save
             return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
        
    