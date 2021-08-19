from django.urls import path
from .views import (
    AccountView,
    profile_view,
    SignInView,
    SignUpView,
    sign_out_view,
)

app_name='users'

urlpatterns = [
    path('', AccountView.as_view(), name="account"),
    path('profile', profile_view, name="profile"),
    path('sign-up', SignUpView.as_view(), name="sign-up"),
    path('sign-in', SignInView.as_view(), name="sign-in"),
    path('sign-out', sign_out_view, name="sign-out")
]
