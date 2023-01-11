
from rest_framework import serializers

from .models import Tag


class TagSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=65)
    slug = serializers.CharField(max_length=65)


class RecipeSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField(max_length=65)
    description = serializers.CharField(max_length=165)
    public = serializers.BooleanField(source='is_published')
    preparation = serializers.SerializerMethodField()
    category = serializers.StringRelatedField()
    author = serializers.StringRelatedField()
    tags = serializers.PrimaryKeyRelatedField(
        queryset=Tag.objects.all(), many=True
    )
    tag_objects = TagSerializer(
        many=True, source='tags'
    )
    tag_links = serializers.HyperlinkedRelatedField(
        many=True,
        source='tags',
        queryset=Tag.objects.all(),
        view_name='recipes:recipes_api_v2_tag'
    )

    def get_preparation(self, recipe):
        return f'{recipe.preparation_time} {recipe.preparation_time_unit}'