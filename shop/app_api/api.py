from app_users.models import UserShopModel
from app_users.serializers import UsersProfileSerializers
from rest_framework import viewsets


class UsersViewSet(viewsets.ModelViewSet):
    queryset = UserShopModel.objects.all()
    serializer_class = UsersProfileSerializers