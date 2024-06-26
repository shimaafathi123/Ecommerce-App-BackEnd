from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from category.views import CategoryListView, CategoryProductListView
from product.views import ProductDetail, ProductList,RelatedProductList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('user.urls')),
    path('products/', ProductList.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('users/wishlist/', include('wishlist.urls')),
    path('cart/', include('shopping_cart.urls')),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('orders/', include('order.urls')),
    path('products/category/<int:category_id>/', ProductList.as_view(), name='products-by-category'),  
    path('products/<int:pk>/related/', RelatedProductList.as_view(), name='related-products'),
    path('categories/<int:category_id>/products/', CategoryProductListView.as_view(), name='category-products'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
