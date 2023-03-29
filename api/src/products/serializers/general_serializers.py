from products.models import Size, Category, Discount, Rating
from rest_framework import serializers

class SizeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Size
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
class DiscountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Discount
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'discount_value': instance.discount_value,
            'category_product': instance.category_product.__str__()
        }
        
class DiscountUpdateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Discount
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
        
class RatingSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Rating
        exclude = ('state', 'created_date', 'modified_date', 'deleted_date')
    