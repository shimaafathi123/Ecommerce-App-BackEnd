from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from category.views import CategoryListView
from product.views import ProductDetail, ProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('users/wishlist/', include('wishlist.urls')),
    path('cart/', include('shopping_cart.urls')),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('products/category/<int:category_id>/', ProductList.as_view(), name='products-by-category'),  # Use ProductList view for listing products by category
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
