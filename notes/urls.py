from django.urls import path
from . import views

urlpatterns = [
    path('', views.note_list, name='note_list'),
    path('new/', views.note_create, name='note_create'), 
    path('edit/<uuid:pk>/', views.note_update, name='note_update'), # <uuid:pk> captures the ID
    path('delete/<uuid:pk>/', views.note_delete, name='note_delete'),
]