from django.contrib import admin
from miniapp.apps.ieso.models import horario,materia,grupo,profesor,alumno

admin.site.register(horario)
admin.site.register(materia)
admin.site.register(grupo)
admin.site.register(profesor)
admin.site.register(alumno)
