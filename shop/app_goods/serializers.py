from rest_framework import serializers
from app_media.models import MediaCategoryModel
from app_goods.models import GoodCategoryModel, Items





class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaCategoryModel
        fields = ['src', 'alt']



class FilterCategorySerializer(serializers.ListSerializer):
    def to_representation(self, data):
        data = data.filter(sub=None)
        return super().to_representation(data)



class RecursiveCategorySerializer(serializers.Serializer):
    """
    Рекурсивный обход-сериализация связанных записей модели
    """
    def to_representation(self, instance):
        ser = self.parent.parent.__class__(instance, context=self.context)
        return ser.data

class CategorySerializer(serializers.ModelSerializer):
    """
    Рекурсивный обход-сериализация связанных записей модели
    """
    subcategories = RecursiveCategorySerializer(many=True)
    image = ImageSerializer()

    href = serializers.SerializerMethodField('get_href')


    def get_href(self, obj):
        return f'/catalog/{obj.id}'

    class Meta:
        list_serializer_class = FilterCategorySerializer
        model = GoodCategoryModel
        fields = ('id', 'title', 'image', 'href', 'subcategories')

class ItemsSerializer(serializers.ModelSerializer):

    href = serializers.SerializerMethodField('get_href')


    def get_href(self, obj):
        return f'/catalog/{obj.id}'

    class Meta:
        """
        Перечислены все поля модели Items и добавлено поле href
        """
        model = Items
        fields = ['id', 'category', 'price', 'count', 'date', 'title', 'description', 'href', 'freeDelivery', 'images',
                  'tags', 'reviews', 'rating']

