from django.urls import path
from user.views import register, obtain_token, profile,change_password,list_users, delete_user, get_user, get_current_user_info

urlpatterns = [
    path('register/', register, name='register'),
    path('token/', obtain_token, name='token_obtain_pair'),
    path('profile/', profile, name='profile'),
    path('resetpass/',change_password, name='change-password'),
    path('get_current_user_info/',get_current_user_info, name='user_info'),
    
    path('admin/users/', list_users, name='list_users'),
    path('admin/users/<int:user_id>/', get_user, name='get_user'),
    path('admin/users/<int:user_id>/delete/', delete_user, name='delete_user'),

]
