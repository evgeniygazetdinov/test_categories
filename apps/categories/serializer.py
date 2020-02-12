from rest_framework import serializers
from .models import Categories
import re


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('find_children')

    def find_relation(self, obj, relation):
        values = []
        #only list with values
        name_category = re.findall('\d+', obj.name)
        all_names_in_db = Categories.objects.exclude(name = name_category)
        for obj_name in all_names_in_db:
            name_for_compare = re.findall('\d+', obj_name.name)
            if relation == "children":
                if name_category[1] >= name_for_compare[1] and len(name_category) < len(name_for_compare):
                    values.append(obj_name.name)

            if relation == 'parents':
                if name_category[1] <= name_for_compare[1] and len(name_for_compare) < len(name_category):
                        values.append(obj_name.name)

            if relation == 'sublings':
                if name_category[1] >= name_for_compare[1] and name_category[-1] != name_for_compare[-1] and len(name_category) == len(name_for_compare):
                        values.append(obj_name.name)


        return values



    def find_children(self, obj):
        return self.find_relation(obj, 'children')

    class Meta:
        model = Categories

        fields = ['name','children']



class CategoriesRelationSerializer(CategoriesSerializer):
    children = serializers.SerializerMethodField('find_children')
    sublings = serializers.SerializerMethodField('find_sublings')
    parents = serializers.SerializerMethodField('find_parents')
    def find_parents(self, obj):
        return self.find_relation(obj, 'parents')


    def find_sublings(self, obj):
        return self.find_relation(obj, 'sublings')



    class Meta:
        model = Categories
        fields = ['name', 'id', 'children', 'sublings', 'parents']
