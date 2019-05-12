from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/<int:id>/', views.details, name='details'),
    path('user/<int:id>/github/', views.repolist, name='repolist')
]