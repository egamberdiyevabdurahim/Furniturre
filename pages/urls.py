from django.urls import path
from pages import views

app_name = 'pages'

urlpatterns = [
    path('contact/', views.ContactView.as_view(), name="contact")
]
