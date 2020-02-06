from django.urls import path
from .views import CategoriesViewSet

urlpatterns = [
    path('', CategoriesViewSet.as_view(),name="categories")
]
