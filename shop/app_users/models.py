from django.db import models
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType



class UserShopModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='usermodel', blank=True, null=True)
    fullName = models.CharField(verbose_name='Full Name', default=None, max_length=100, blank=True, null=True)
    phone = models.PositiveIntegerField(default=None, blank=True, null=True)
    email = models.EmailField(max_length=50, default=None, blank=True, null=True)
    balance = models.PositiveIntegerField(default=0, blank=True, null=True)
    avatar = models.ImageField(verbose_name='Avatar', default=None, upload_to='users/', blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def as_json(self, obj):
        return {obj: f'{obj}'}

    def __str__(self):
        return str(self.fullName)