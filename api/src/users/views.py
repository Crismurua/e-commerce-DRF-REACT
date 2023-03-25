from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from dj_rest_auth.registration.views import RegisterView
from .serializers import CustomRegisterSerializer

from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter

class CustomRegisterView(RegisterView):
    serializer_class = CustomRegisterSerializer

class FacebookLogin(SocialLoginView):
    adapter_class = FacebookOAuth2Adapter
    
class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter