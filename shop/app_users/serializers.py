from django.contrib.auth.models import User
from rest_framework import serializers
from app_users.models import UserShopModel





class UsersProfileSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserShopModel
        fields = ['fullName', 'phone', 'avatar', 'email']

class UsersChangePasswordSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =['password', 'password1', 'password2']


class UsersAvatarSerializers(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = UserShopModel
        fields = ['avatar']

