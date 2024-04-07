from django.contrib import admin
from django.urls import path, include  # Import include function
from django.urls import path,include

from django.conf import settings
from django.conf.urls.static import static

from product.views import ProductDetail, ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('users/wishlist/', include('wishlist.urls')),
    path('orders/', include('order.urls')),
    ]



urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
