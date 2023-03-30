from django.contrib import admin
from app_users.models import UserShopModel

@admin.register(UserShopModel)
class UsersProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'fullName', 'email', 'avatar']
