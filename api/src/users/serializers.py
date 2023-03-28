from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import State, City

class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = State
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'

class CustomRegisterSerializer(RegisterSerializer):
    image = serializers.ImageField(required=False)
    phone = serializers.CharField(required=False)
    state = StateSerializer(required=False)
    city = CitySerializer(required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'image', 'first_name', 'last_name', 'phone', 'state', 'city')

    def get_cleaned_data(self):
        super().get_cleaned_data()
        return {
            'username': self.validated_data.get('username', ''),
            'email': self.validated_data.get('email', ''),
            'password1': self.validated_data.get('password1', ''),
            'image': self.validated_data.get('image', ''),
            'first_name': self.validated_data.get('first_name', ''),
            'last_name': self.validated_data.get('last_name', ''),
            'phone': self.validated_data.get('phone', ''),
            'state': self.validated_data.get('state', ''),
            'city': self.validated_data.get('city', ''),
        }
        
    def create(self, validated_data):
        user = super().create(validated_data)
        user.image = validated_data.get('image', '')
        user.phone = validated_data.get('phone', '')
        state_id = validated_data.pop('state', None)
        city_id = validated_data.pop('city', None)
        if state_id is not None:
            try:
                state = State.objects.get(id=state_id)
                user.state = state
            except State.DoesNotExist:
                pass
        if city_id is not None:
            try:
                city = City.objects.get(id=city_id)
                user.city = city
            except City.DoesNotExist:
                pass
        user.save()
        return user

    def save(self, request):
        user = super().save(request)
        user.image = self.validated_data.get('image', '')
        user.phone = self.validated_data.get('phone', '')
        user.state = self.validated_data.get('state', '')
        user.city = self.validated_data.get('city', '')
        user.save()
        return user
    
    def validate(self, data):
        """
        Validate the extra fields.
        """
        if 'phone' in data and not data['phone'].isdigit():
            raise serializers.ValidationError("Phone number can only contain digits.")
        return data
    
class UpdateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('first_name', 'last_name', 'image', 'phone', 'state', 'city')
        
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        
    def to_representation(self, instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'first_name': instance['first_name'],
            'last_name': instance['last_name'],
            'image': instance['image'],
            'phone': instance['phone'],
            'state': instance['state'],
            'city': instance['city'],
        }
    