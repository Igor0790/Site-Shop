from django.contrib.auth.models import User
from rest_framework import status
from rest_framework import views
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics

from app_goods.models import GoodCategoryModel, Items
from app_goods.serializers import CategorySerializer, ItemsSerializer
from app_users.models import UserShopModel
from app_users.serializers import UsersProfileSerializers, UsersAvatarSerializers


class UsersProfileApiView(views.APIView):
    serializer_class = UsersProfileSerializers
    queryset = UserShopModel.objects.all()




    def get(self, request):
        user = UserShopModel.objects.filter(user_id=request.user.id).first()
        serializer = UsersProfileSerializers(user)
        return Response(serializer.data)

    def get_queryset(self):
        return UserShopModel.objects.filter(fullName='igor1')

    def post(self, request):
        serializer = UsersProfileSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UsersProfilePasswordApiView(views.APIView):
    queryset = User.objects.all()

    def post(self, request):
        user = self.queryset.get(id=request.user.id)
        user.set_password(request.data['password'])  # replace with your real password
        user.save()
        return Response(status=status.HTTP_201_CREATED)

class UsersAvatarPostApiView(views.APIView):
    serializer_class = UsersAvatarSerializers
    queryset = UserShopModel.objects.all()

    def post(self, request):

        UserShopModel.objects.filter(user_id=request.user.id).update(avatar=request.FILES['avatar'])
        return Response(status=status.HTTP_201_CREATED)

class GoodCategoryApiView(views.APIView):
    queryset = GoodCategoryModel.objects.all()
    serializer_class = CategorySerializer

    def get(self, request):
        serializer = self.serializer_class(self.queryset.filter(id=1).select_related('sub').first())
        return Response(serializer.data)

class ItemsApiView(mixins.ListModelMixin, generics.GenericAPIView):
    serializer_class = ItemsSerializer
    queryset = Items.objects.all()

    def get(self, request):
        return self.list(request)