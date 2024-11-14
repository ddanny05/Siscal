from django.contrib import admin
from .models import Estudiante, Docente, Calificacion

# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Calificacion)