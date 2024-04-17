from django.urls import path
from .views import AddToCartView, UpdateCartItemView, CartDetailView, DeleteCartItemView

urlpatterns = [
    path('add-to-cart/', AddToCartView.as_view(), name='add_to_cart'),
    path('update-cart/<int:pk>/', UpdateCartItemView.as_view(), name='update_cart'),
    # path('cart/<int:pk>/', CartDetailView.as_view(), name='cart-detail'), 
     path('cart/', CartDetailView.as_view(), name='cart-detail'),
    path('delete-cart-item/<int:pk>/', DeleteCartItemView.as_view(), name='delete_cart_item'),
]
