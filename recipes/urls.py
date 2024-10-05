from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='home'),
    path('recipe/category/<slug:slug>/', views.category, name='category'),
    path('recipe/<slug:slug>/', views.recipe_detail, name='detail'),
]
