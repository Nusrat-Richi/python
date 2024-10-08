from rest_framework import serializers
from .models import Product
class ProductsSerializers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['id','name','description','price','stock','suplier','created_at','updated_at']