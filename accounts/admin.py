from django.contrib import admin
from accounts.models import UserModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'first_name', 'last_name', 'is_active', 'date_joined',)
    list_filter = ('is_active', 'date_joined',)
    search_fields = ('email', 'first_name', 'last_name',)
