from django.contrib import admin
from app_goods.models import GoodCategoryModel, Items

@admin.register(GoodCategoryModel)
class GoodCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'sub')


@admin.register(Items)
class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'price', 'count', 'date', 'title', 'description', 'freeDelivery', 'images',
                  'tags', 'reviews', 'rating']