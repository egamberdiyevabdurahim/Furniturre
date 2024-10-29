from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pages/', include('pages.urls', namespace="pages")),
    path('accounts/', include('accounts.urls', namespace="accounts")),
    path('products/', include('products.urls', namespace="products")),
    path('orders/', include('orders.urls', namespace="orders")),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'conf.views.handler404'
# handler401 = 'conf.views.handler404'
# handler403 = 'conf.views.handler404'
# handler500 = 'conf.views.handler404'
