from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:item_id>/', views.add_random_rating, name='add_random_rating'),
    path('<int:item_id>/results/', views.results, name='results')
]