from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfile(models.Model):
    '''
    our User profile model extends the built-in django User model
    '''
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    user =models.OneToOneField(User, on_delete=models.CASCADE)
    
    address= models.CharField(max_length=100, verbose_name=('Address'), null=True, blank=True)
    town= models.CharField(max_length=100, verbose_name=('Town/City'), null=True, blank=True)
    county= models.CharField(max_length=100, verbose_name=('County'), null=True, blank=True)
    post_code= models.CharField(max_length=8, verbose_name=('Post Code'), null=True, blank=True)
    country= models.CharField(max_length=100, verbose_name=('Country'), null=True, blank=True)
    longtitude= models.CharField(max_length=50, verbose_name=('Longtitude'), null=True, blank=True)
    latitude= models.CharField(max_length=50, verbose_name=('Latitude'), null=True, blank=True)

    captcha_score=models.FloatField(default=0.0)
    has_profile= models.BooleanField(default=False)
    is_active= models.BooleanField(default=True)
    
    def __str__(self) -> str:
        return f'{self.user}'    