from django.contrib import admin

# Register your models here.

from .models import Estudiante, Docente, Curso, Ciclo, Asistencia, Facultad, Curso_has_Estudiante, CategoriaAsistencia


admin.site.register(Estudiante)
admin.site.register(Docente)
admin.site.register(Curso)
admin.site.register(Ciclo)
admin.site.register(Facultad)
admin.site.register(Curso_has_Estudiante)
admin.site.register(Asistencia)
admin.site.register(CategoriaAsistencia)