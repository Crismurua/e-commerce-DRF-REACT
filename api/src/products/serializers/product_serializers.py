from rest_framework import serializers

from products.models import Product
from .general_serializers import SizeSerializer, CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
    def validate_size(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Measure Unit required!')
        return value
    
    def validate_category(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Category required!')
        return value
    
    def validate(self, data):
        if 'size' not in data.keys():
            raise serializers.ValidationError({'size': 'Size required!'})
        
        if 'category' not in data.keys():
            raise serializers.ValidationError({'category': 'Category required!'})
        
        return data
    
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'price': instance.price,
            'image': instance.image.url if instance.image != '' else '',
            'size': instance.size.size if instance.size is not None else '',
            'category': instance.category.category if instance.category is not None else '',
            
        }
        
class ProductListSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
