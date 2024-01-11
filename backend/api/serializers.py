from rest_framework import serializers


# class UserProductInlineSerializer(serializers.Serializer):
#     title = serializers.CharField(read_only=True)
#     url = serializers.HyperlinkedIdentityField(
#         view_name="product-detail", lookup_field="pk", read_only=True
#     )


class UserPublicSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True)
    id = serializers.PrimaryKeyRelatedField(read_only=True)

    # other_products = serializers.SerializerMethodField(read_only=True)

    # def get_other_products(self, obj):
    #     return UserProductInlineSerializer(
    #         obj.product_set.all(), many=True, context=self.context
    #     ).data
