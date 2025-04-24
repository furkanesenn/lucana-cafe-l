from django.urls import path

from . import views
 
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'), 
    path('search', views.SearchView.as_view(), name='search'),
    path('<str:category>', views.CategoryView.as_view(), name='category'),
]