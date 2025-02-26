from django.urls import path
from .views import product_list
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
       path('products/', product_list, name='product_list'),
]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)