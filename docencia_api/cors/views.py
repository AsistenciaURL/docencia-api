#Django Rest Framework
from rest_framework.views import Response
from rest_framework import viewsets

from .models import Estudiante, Docente, Curso, Ciclo, Asistencia, Facultad, Curso_has_Estudiante, CategoriaAsistencia

from .serializers import EstudianteSerializer, DocenteSerializer, CursoSerializer, CicloSerializer, AsistenciaSerializer, FacultadSerializer, Curso_has_EstudianteSerializer, CategoriaAsistenciaSerializer

# serializers


class EstudianteViewSet(viewsets.ModelViewSet):
        queryset = Estudiante.objects.all()
        serializer_class = EstudianteSerializer

class DocenteViewSet(viewsets.ModelViewSet):
        queryset = Docente.objects.all()
        serializer_class = DocenteSerializer

class CursoViewSet(viewsets.ModelViewSet):
        queryset = Curso.objects.all()
        serializer_class = CursoSerializer

class CicloViewSet(viewsets.ModelViewSet):
        queryset = Ciclo.objects.all()
        serializer_class = CicloSerializer


class AsistenciaViewSet(viewsets.ModelViewSet):
        queryset = Asistencia.objects.all()
        serializer_class = AsistenciaSerializer

class FacultadViewSet(viewsets.ModelViewSet):
        queryset = Facultad.objects.all()
        serializer_class = FacultadSerializer

class Curso_has_EstudianteViewSet(viewsets.ModelViewSet):
        queryset = Curso_has_Estudiante.objects.all()
        serializer_class = Curso_has_EstudianteSerializer

class CategoriaAsistenciaViewSet(viewsets.ModelViewSet):
        queryset = CategoriaAsistencia.objects.all()
        serializer_class = CategoriaAsistenciaSerializer


