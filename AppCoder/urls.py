from django.urls import path
from AppCoder.views import *




urlpatterns = [
    path('', inicio),
    path('curso', curso),
    path('entregables', entregables),
    path('estudiantes', estudiantes),
    path('profesores', profesores),
    path('home', home),
    
]