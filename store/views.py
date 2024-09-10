from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
from django.views.generic import TemplateView

class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class StoreHomeView(TemplateView):
    template_name = 'store/index.html'
    