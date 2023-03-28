from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework import viewsets
from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer, UpdateUserSerializer, UserListSerializer

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    
class UserViewSet(viewsets.GenericViewSet):
    model = get_user_model()
    serializer_class = UpdateUserSerializer
    list_serializer_class = UserListSerializer
    queryset = None
    
    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)
    
    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active=True).values('id', 'username', 'email', 'first_name', 'last_name', 'image', 'phone', 'state', 'city')
        return self.queryset
    
    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.list_serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = UpdateUserSerializer(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message': 'User successfully updated!'}, status=status.HTTP_200_OK)
        return Response({'message': 'Error updating user!', 'errors': user_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, pk=None):
        user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
        if user_destroy == 1:
            return Response({'message': 'User successfully deleted!'}, status=status.HTTP_200_OK)
        return Response({'message': 'User not found!'}, status=status.HTTP_404_NOT_FOUND)
        