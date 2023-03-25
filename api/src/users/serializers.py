from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model

class CustomRegisterSerializer(RegisterSerializer):
    image = serializers.ImageField(required=False)
    phone = serializers.CharField(required=False)
    location = serializers.CharField(required=False)

    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'password1', 'password2', 'image', 'first_name', 'last_name', 'phone', 'location')

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
            'location': self.validated_data.get('location', ''),
        }
        
    def create(self, validated_data):
        user = super().create(validated_data)
        user.image = validated_data.get('image', '')
        user.phone = validated_data.get('phone', '')
        user.location = validated_data.get('location', '')
        user.save()
        return user

    def save(self, request):
        user = super().save(request)
        user.image = self.validated_data.get('image', '')
        user.phone = self.validated_data.get('phone', '')
        user.location = self.validated_data.get('location', '')
        user.save()
        return user
    
    def validate(self, data):
        """
        Validate the extra fields.
        """
        if 'phone' in data and not data['phone'].isdigit():
            raise serializers.ValidationError("Phone number can only contain digits.")
        return data