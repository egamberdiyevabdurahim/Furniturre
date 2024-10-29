from django.urls import path

from .views import *

app_name = 'common'

urlpatterns = [
    path('', home_page_view, name='home'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('login/', login_page_view, name='login'),
    path('logout/', logout_page_view, name='logout'),
    path('register/', register_page_view, name='register'),
]
