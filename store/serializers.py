from rest_framework import serializers
from .models import Product
from rest_framework.exceptions import ValidationError

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')

    def create(self, validated_data):
        price = validated_data.get('price')
        if price < 0:
            raise ValidationError('Цена должна быть больше 0')
        return super().create(validated_data)
