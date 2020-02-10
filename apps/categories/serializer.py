from rest_framework import serializers
from .models import Categories



class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('find_property')
    def calculate_dif(self, l1, l2):
        if len(l1)<len(l2):
            res = len(l2)-len(l1)
            for i in range(res):
                l1.append(0)
            return l1
        else:
            return l1


    def find_relation(self,obj):
        child = []
        name_category = (obj.name).split('.')
        all_names = Categories.objects.exclude(name = name_category)
        for obj_name in all_names:
            name_for_compare = (obj_name.name).split('.')
            ref = self.calculate_dif(name_category,name_for_compare)
            for i in range(len(name_for_compare)):
                if ref[-i] == name_for_compare[-i]:
                    if i !=1 :
                        if ref[i] != name_for_compare[i]:
                            child.append(obj_name.name)
        return child


    def find_property(self,obj):
        return self.find_relation(obj)

    class Meta:
        model = Categories
        fields = ['name','children']



class CategoriesRelationSerializer(CategoriesSerializer):

    def validate(self, data):
        if self.instance:
            object_id = self.instance.id
        return data

    fields = ['name',]
