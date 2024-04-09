from django.urls import path

from .views import user_orders, order_details, create_order, cancel_order,CreateCheckout

urlpatterns = [
    # path('', user_orders.as_view(), name='order_list'),
    path('create/', create_order.as_view(), name='order_create'),
    path('', order_details.as_view(), name='order_detail'),
    path('<int:pk>/cancel', cancel_order.as_view(), name='order_cancel'),
    path('checkout/', CreateCheckout.as_view(), name='order-checkout'),
]

