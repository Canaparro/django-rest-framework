from rest_framework import serializers

from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    serializer_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "price",
            "sale_price",
            "serializer_discount",
        ]

    def get_serializer_discount(self, obj: Product):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
