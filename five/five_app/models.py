from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Userprofil(models.Model):
    """docstring for Userprofil."""

    user = models.OneToOneField(User,on_delete=models.CASCADE, related_name='profile_name')
    profelio = models.URLField(blank= True)
    profil_pic = models.ImageField(upload_to =  'profile_pics', blank =True)

    def __str__(self):
        return self.user.username
