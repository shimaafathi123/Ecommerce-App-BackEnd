from django.urls import path
from rest_framework.routers import DefaultRouter
from .views  import WishlistItem, user_wishlist

router = DefaultRouter()

urlpatterns = [
    path('',user_wishlist.as_view() , name='wishlist_details'),
    path('items/<int:pk>', WishlistItem.as_view(), name='wishlist_items'),
]
