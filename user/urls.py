from django.urls import path
from user.views import register, obtain_token, profile

urlpatterns = [
    path('register/', register, name='register'),
    path('token/', obtain_token, name='token_obtain_pair'),
    path('profile/', profile, name='profile'),
]
