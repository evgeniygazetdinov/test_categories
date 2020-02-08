from rest_framework import serializers
from .models import Categories
import re





class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('find_property')

    def extract_digits(self,str):
        #extract digits for compare
        string_for_compare = str(str)
        res = re.findall(r'\d+',string_for_compare)
        return res

    def compare_categories(self,posible_children,name_category):
        #find less for children
        res = []
        category = extract_digits(name_category)
        maybe_children = extract_digits(posible_children)
        for category_digit in category:
            for children_digits in maybe_children:
                if category_digit < children_digits:
                    return
                else:



    def find_children(self,obj):
        name_category = obj.name
        #find all without current category
        all_names = Categories.objects.filter(name = name)
        
        for names in all_names:
            compare_categories(all_names,name_category)
        return self.extract_digits(name)


    def find_property(self,obj):
        return self.find_children(obj)


    class Meta:
        model = Categories
        fields = ['name','children']
