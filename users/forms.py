from django.forms import ModelForm, fields
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class UserForm(UserCreationForm):
    '''
    Form that use built-in UserCreationForm to handle user creation.
    '''
    first_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
                    attrs={'placeholder': 'your first name'}))
    last_name = forms.CharField(max_length=30, required=True, widget=forms.TextInput(
                    attrs={'placeholder': 'your last name'}))
    username = forms.EmailField(max_length=254, required=True, widget=forms.EmailInput(
                    attrs={'placeholder': '*Email..'}))
    password1 = forms.CharField(widget=forms.PasswordInput(
                    attrs={'placeholder': 'password', 'class': 'password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(
                    attrs={'placeholder': '*confirm password', 'class': 'password'}))
    
    #reCAPTCHA token
    token=forms.CharField(widget=forms.HiddenInput())
    
    class Meta:
        model =User
        fields=('username','first_name','last_name', 'password1', 'password2')
       
    

class AuthForm(AuthenticationForm):
    '''
    Forms that uses built-in AuthenticationForm to handle user authentication
    '''
    username=forms.EmailField(max_length=254, required=True, 
                              widget=forms.TextInput(attrs={'placeholder':'*Email..'}))
    password = forms.CharField(widget=forms.PasswordInput(
                    attrs={'placeholder': 'password', 'class': 'password'}))
                              
    class Meta:
        model =User
        fields=('username', 'password')
        
class UserProfileForm(forms.ModelForm):
    '''
    Basic model-form for our user profile that extends Django User Model
    '''
    address = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    county = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    post_code = forms.CharField(max_length=8, required=True, widget=forms.HiddenInput())
    country = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    longtitude = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    latitude = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
    
    class Meta:
        model = UserProfile
        fields = ('address', 'town', 'county', 'post_code', 'country','longtitude','latitude')