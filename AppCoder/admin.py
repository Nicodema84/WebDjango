from django.contrib import admin

from AppCoder.views import curso, entregables, estudiantes, profesores
from .models import *
# Register your models here.


admin.site.register(Curso)
admin.site.register(Estudiante)
admin.site.register(Profesor)
admin.site.register(Entregable)
