from rest_framework import serializers
from .models import Categories
import re





class CategoriesSerializer(serializers.HyperlinkedModelSerializer):
    children = serializers.SerializerMethodField('find_property')

    def do_same_length(self,category,children):
        good_len =[]
        if len(category) == len(children):
            return children
        else:
            #do work here
            cut_len = len(children) - len(category)
            for _ in range(cut_len):
                good_len = children.pop()
            return good_len

    def extract_digits(self,name_category):
        #extract digits for compare
        string_for_compare = str(name_category)
        res = re.findall(r'\d+',string_for_compare)
        return res

    def compare_categories(self,posible_children,name_category):
        #find less for children
        res = []
        category = self.extract_digits(name_category)
        maybe_children = self.extract_digits(posible_children)
        #do maybe children good len for compare
        children_for_compare = self.do_same_length(category,maybe_children)
        print(children_for_compare)
        for category_digit in category:
            for children_digits in children_for_compare:
                if category_digit < children_digits:
                    break
                else:
                    res.append(children_digits)



    def find_relation(self,obj):
        res =[]
        name_category = obj.name
        #find all without current category
        all_names = Categories.objects.exclude(name = name_category)

        for posible_children in all_names:
            res.append(self.compare_categories(posible_children,name_category))
        return res


    def find_property(self,obj):
        return self.find_relation(obj)


    class Meta:
        model = Categories
        fields = ['name','children']
