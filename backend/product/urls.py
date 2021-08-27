
from django.urls import path
from .import views


urlpatterns = [
    path('products/', views.ProductsList.as_view()),
    path('category/', views.CategoryTree.as_view()), 
    path('category2/', views.CategoryTree2.as_view()),
    path('fakedata/', views.FakedataList.as_view({'get': 'list'})),
    path('products/search/', views.search),
    path('products/<slug:category_slug>/', views.CategoryDetail.as_view()),
]