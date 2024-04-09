from django.urls import path
from user.views import register, obtain_token, profile,change_password

urlpatterns = [
    path('register/', register, name='register'),
    path('token/', obtain_token, name='token_obtain_pair'),
    path('profile/', profile, name='profile'),
    path('resetpass/',change_password, name='change-password'),
]
