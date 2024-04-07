from django.urls import path

from .views import user_order, order_details, create_order, cancel_order

urlpatterns = [
    path('', user_order.as_view(), name='order_list'),
    path('create/', create_order.as_view(), name='order_create'),
    path('<int:pk>/', order_details.as_view(), name='order_detail'),
    path('<int:pk>/cancel', cancel_order.as_view(), name='order_cancel'),
]

