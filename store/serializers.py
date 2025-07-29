from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from store.models import Category


class CategorySerializer(serializers.ModelSerializer):
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        validators=[UniqueValidator(queryset=Category.objects.all())]
    )
    nested_parent = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent', 'nested_parent']
        depth = 5

    def get_nested_parent(self, obj):
        if obj.parent is not None:
            return CategorySerializer(obj.parent).data
        return None


class ProductSerializer(serializers.ModelSerializer):
    pass
