from rest_framework import serializers
from .models import Categories

class CategoriesSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Categories
        fields = ['url', 'username', 'email', 'is_staff']
