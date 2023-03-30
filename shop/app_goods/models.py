from django.db import models
from app_users.models import UserShopModel
from app_media.models import MediaCategoryModel



class GoodCategoryModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Title Category', db_index=True)
    image = models.OneToOneField(MediaCategoryModel, on_delete=models.CASCADE, related_name='image', default=None)
    sub = models.ForeignKey('self', on_delete=models.SET_NULL, blank=True, null=True, related_name='subcategories')
    #https://www.django-rest-framework.org/api-guide/relations/#nested-relationships
    #https://stackoverflow.com/questions/40541822/how-to-show-depth-of-a-single-field-in-django-rest-framework

    def __str__(self):
        return self.title


    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Items(models.Model):
    category = models.ForeignKey(GoodCategoryModel, on_delete=models.CASCADE, verbose_name='Category', default=None, related_name='items')
    price = models.IntegerField(verbose_name='Price')
    count = models.IntegerField(verbose_name='Count')
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    description = models.CharField(max_length=1000, verbose_name='Description')
    freeDelivery = models.BooleanField(default=False)
    images = models.ImageField(verbose_name='Images', upload_to='media/goods/items', blank=True, null=True)
    tags = models.CharField(verbose_name='Tags', max_length=100)
    reviews = models.IntegerField(verbose_name='Reviews')
    rating = models.FloatField(max_length=1000, verbose_name='Rating', default=0, blank=True, null=True)


    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Items'

    def __str__(self):
        return self.title


