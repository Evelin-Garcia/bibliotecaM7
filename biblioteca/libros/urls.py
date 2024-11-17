from django.urls import path
from . import views

app_name = 'libros'

urlpatterns = [
    path('registrar_libros', views.registro_libros, name='registro_libros'),
    path('analytics/', views.analytics, name='analytics')
]
