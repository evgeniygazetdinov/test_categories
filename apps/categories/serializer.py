from rest_framework import serializers
from .models import *






class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    parent = serializers.SerializerMethodField('find_parent')

    def find_children(self):
        return 'children'


    class Meta:
        model = Categories
        fields = ['name','parent']
