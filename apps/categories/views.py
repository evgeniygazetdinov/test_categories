from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Categories
from .serializer import CategoriesSerializer
import random


class CategoriesViewSet(GenericAPIView):
    def create_randoms(self):
        pass


    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


    def list(self):
        serializer = self.get_serializer(queryset, many=True)
        return serializer.data
