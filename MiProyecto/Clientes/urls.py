from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_lectores, name='listar_lectores'),
    path('crear/', views.crear_lector, name='crear_lector'),
    path('editar/<int:pk>/', views.editar_lector, name='editar_lector'),
    path('eliminar/<int:pk>/', views.eliminar_lector, name='eliminar_lector'),
]