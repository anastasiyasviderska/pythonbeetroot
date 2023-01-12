from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:book_id>/random/', views.add_random_rating, name='add_random_rating'),
    path('<int:book_id>/results/', views.results, name='results')
]