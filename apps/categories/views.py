from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import Categories
from .serializer import CategoriesSerializer, CategoriesRelationSerializer
from rest_framework.response import Response
from django.shortcuts import redirect



def redirect_to_main(request):
    return redirect('/categories/')


class CategoriesViewSet(GenericAPIView):


    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer

    def get(self,response):

        serializer = self.get_serializer(self.get_queryset(), many=True)
        return Response(serializer.data)

class CategoriesRelationViewSet(GenericAPIView):
    serializer_class = CategoriesRelationSerializer
    
    def get_queryset(self,*args,**kwargs):
        return Categories.objects.filter(id=self.kwargs['id'])

    def get(self,response,id):
        serializer = self.get_serializer(self.get_queryset(id), many=True)
        return Response(serializer.data)
