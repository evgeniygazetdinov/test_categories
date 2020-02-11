from django.urls import path
from .views import CategoriesViewSet, CategoriesRelationViewSet

urlpatterns = [
    path('', CategoriesViewSet.as_view(),name="categories"),
    path('<int:id>/',CategoriesRelationViewSet.as_view(),name="categories_by_id")
]
