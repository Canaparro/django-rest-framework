from django.shortcuts import get_object_or_404
from requests import Request
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer: ProductSerializer):
        # serializer.save(user = self.request.user)
        content = serializer.validated_data.get('content') or None
        if not content:
            content = serializer.validated_data.get('title')
        serializer.save(content=content)


class ProductDetailAPIVIew(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductUpdateAPIVIew(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title


class ProductDeleteAPIVIew(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_destroy(self, instance):
        # do whatever is needed here
        super().perform_destroy(instance)


@api_view(['GET', 'POST'])
def product_alt_view(request: Request, pk=None,  *args, **kwargs):
    method = request.method

    print(method)
    if method == 'GET':
        if pk:
            product = get_object_or_404(Product, pk=pk)
            return Response(ProductSerializer(product).data)
        else:
            products = Product.objects.all()
            return Response(ProductSerializer(products, many=True).data)
    if method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            content = serializer.validated_data.get('content') or None
            if not content:
                content = serializer.validated_data.get('title')
            serializer.save(content=content)
            return Response(serializer.data)


# class ProductListAPIVIew(generics.ListAPIView):
#     '''
#     Not gonna use this view
#     '''
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
