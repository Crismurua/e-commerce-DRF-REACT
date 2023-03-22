from rest_framework import serializers

from products.models import Product
from .general_serializers import MeasureUnitSerializer, CategorySerializer

class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
    def validate_measure_unit(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Measure Unit required!')
        return value
    
    def validate_category(self, value):
        if value == '' or value == None:
            raise serializers.ValidationError('Category required!')
        return value
    
    def validate(self, data):
        if 'measure_unit' not in data.keys():
            raise serializers.ValidationError({'measure_unit': 'Measure Unit required!'})
        
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
            'measure_unit': instance.measure_unit.measure_unit if instance.measure_unit is not None else '',
            'category': instance.category.category if instance.category is not None else '',
            
        }
        
class ProductListSerializer(serializers.ModelSerializer):
        
    class Meta:
        model = Product
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
