from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('cart/<int:pk>/', views.add_or_remove, name='add-or-remove'),
    path('cart/', views.UserCartView.as_view(), name='cart'),
    path('order/', views.OrderCreateView.as_view(), name='order'),
]
