from rest_framework import serializers
from .models import Categories
import re


class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('find_children')

    def calculate_dif(self, refirence, for_compare):
        #add zero into list for same length
        if len(refirence)<len(for_compare):
            res = len(for_compare)-len(refirence)
            for i in range(res):
                refirence.append(0)
            return refirence
        if len(for_compare) <len(refirence):
            res = len(refirence)-len(for_compare)
            for i in range(res):
                refirence.pop()
            return refirence
        return refirence


    def find_relation(self, obj, number,relation):
        values = []
        name_category = re.findall('\d+', obj.name)
        all_names_in_db = Categories.objects.exclude(name = name_category)
        for obj_name in all_names_in_db:
            name_for_compare = re.findall('\d+', obj_name.name)
            ref = self.calculate_dif(name_category,name_for_compare)
            for i in range(len(name_for_compare)):
                if relation == "children":
                    if ref[1] > name_for_compare[1]:
                        print('^'*1000)
                        print('ref')
                        print(ref)
                        print(ref[1])
                        print('name_or')
                        print(name_for_compare)
                        print(name_for_compare[1])
                        print('^'*1000)
                        values.append(obj_name.name)

            if relation == 'parents':
                    pass

            if relation == 'sublings':
                    pass
        return values



    def find_children(self, obj):
        return self.find_relation(obj, 1, 'children')

    class Meta:
        model = Categories

        fields = ['name','children']



class CategoriesRelationSerializer(CategoriesSerializer):
    children = serializers.SerializerMethodField('find_children')
    sublings = serializers.SerializerMethodField('find_sublings')
    parents = serializers.SerializerMethodField('find_parents')
    def find_parents(self, obj):
        return self.find_relation(obj, 3, 'parents')


    def find_sublings(self, obj):
        return self.find_relation(obj, 3, 'sublings')



    class Meta:
        model = Categories
        fields = ['name', 'id', 'children', 'sublings', 'parents']
