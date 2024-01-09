from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer