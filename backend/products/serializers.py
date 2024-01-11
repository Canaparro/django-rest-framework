from requests import Request
from rest_framework.reverse import reverse
from rest_framework import serializers

from .models import Product
from . import validators
from api.serializers import UserPublicSerializer


class ProductSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    serializer_discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name="product-detail", lookup_field="pk"
    )
    # email = serializers.EmailField(write_only=True)
    title = serializers.CharField(
        validators=[
            validators.validate_title_no_hello,
            validators.unique_product_title,
        ]
    )
    body = serializers.CharField(source="content")

    class Meta:
        model = Product
        fields = [
            "id",
            "title",
            "content",
            "body",
            "price",
            "sale_price",
            "serializer_discount",
            "url",
            "edit_url",
            # "email",
            "user",
            "public",
        ]

    def get_serializer_discount(self, obj: Product):
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()

    def get_edit_url(self, obj: Product):
        request: Request = self.context.get("request")
        if not request:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)
