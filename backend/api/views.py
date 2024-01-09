from requests import Request
from products.serializers import ProductSerializer

from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


@api_view(["POST"])
def api_home(request: Request, *args, **kwargs):
    """
    DRF api view
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.data
        return Response(data)
