from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Categories
from .serializer import CategoriesSerializer



class CategoriesViewSet(GenericAPIView):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
