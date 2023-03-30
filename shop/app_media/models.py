from django.db import models

class MediaCategoryModel(models.Model):
    src = models.ImageField(default=None, upload_to='goods/categories/')
    alt = models.CharField(max_length=100, default=None, verbose_name='ALT SRC')

    def __str__(self):
        return self.alt

    class Meta:
        verbose_name = 'Media of Category'
        verbose_name_plural = 'Media of Categories'
