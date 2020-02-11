from rest_framework import serializers
from .models import Categories



class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('find_property')
    def calculate_dif(self, refirence, for_compare):
        #add zero into list for same length
        if len(refirence)<len(for_compare):
            res = len(for_compare)-len(refirence)
            for i in range(res):
                refirence.append(0)
            return refirence
        return refirence


    def find_relation(self,obj,one_name_for_search = False):
        child = []
        name_category = (obj.name).split('.')
        if one_name_for_search:
            all_names_in_db = Categories.objects.filter(id = one_name_for_search)
        else:
            all_names_in_db = Categories.objects.exclude(name = name_category)
        for obj_name in all_names_in_db:
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
    children = serializers.SerializerMethodField('find_property')

    def find_property(self,obj):
        return self.find_relation(obj)

    class Meta:
        model = Categories
        fields = ['name', 'id','children']
