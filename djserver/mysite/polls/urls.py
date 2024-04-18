from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('inference/', views.inference, name='inference'),
    path('cw/', views.cw, name='cw'),
    path('consistency/', views.consistency, name='consistency'),
    path('partition/', views.partition, name='partition'),
]
