from django.urls import path
from .views import ProductAPIView, StoreHomeView


urlpatterns = [
    path('api/v1/productlist/', ProductAPIView.as_view()),
    path('', StoreHomeView.as_view(), name='home'),
]