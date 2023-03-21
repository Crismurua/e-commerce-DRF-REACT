from django.db import models
from django.contrib.auth.models import User
  
class Avatar(models.Model):
    
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile/', null=True, blank=True, default='profile/blank.png')
    
    def __str__(self):
        return self.user.username
    
    class Meta:
        
        verbose_name = 'Avatar'    
        verbose_name_plural = 'Avatars'    
