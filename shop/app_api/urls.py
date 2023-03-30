from django.urls import path
from app_api.views import UsersProfileApiView, UsersProfilePasswordApiView, UsersAvatarPostApiView, GoodCategoryApiView, ItemsApiView
from rest_framework import routers
from app_api.api import UsersViewSet


router = routers.DefaultRouter(trailing_slash=True)
router.register('users', UsersViewSet)


urlpatterns = [
    path('profile/', UsersProfileApiView.as_view(), name='profile'),
    path('profile/password', UsersProfilePasswordApiView.as_view(), name='password'),
    path('profile/avatar', UsersAvatarPostApiView.as_view(), name='avatar'),
    path('categories', GoodCategoryApiView.as_view(), name='categories'),
    path('catalog', ItemsApiView.as_view(), name='items')
] + router.urls


