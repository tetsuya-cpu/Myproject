from django.urls import path
from . import views

urlpatterns = [
    path('', views.person_list, name='person_list'),
    path('add/', views.person_create, name='person_add'),
    path('edit/<int:pk>/', views.person_update, name='person_edit'),
    path('delete/<int:pk>/', views.person_delete, name='person_delete'),
]