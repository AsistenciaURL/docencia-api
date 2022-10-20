# django
from django.db import router
from django.urls import path

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import *

router = DefaultRouter()
router.register(r'Estudiantes', EstudianteViewSet)
router.register(r'Docente', DocenteViewSet)
router.register(r'Curso', CursoViewSet)
router.register(r'Ciclo', CicloViewSet)
router.register(r'Asistencia', AsistenciaViewSet)
router.register(r'Facultad', FacultadViewSet)
router.register(r'Curso_has_estudiante', Curso_has_EstudianteViewSet)
router.register(r'CategoriaAsistencia', CategoriaAsistenciaViewSet)

urlpatterns = router.urls

urlpatterns += [

]