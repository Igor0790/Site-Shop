from django.contrib import admin
from app_media.models import MediaCategoryModel

@admin.register(MediaCategoryModel)
class MediaCategoryAdmin(admin.ModelAdmin):
    list_display = ('src', 'alt')
