from dataclasses import field
from rest_framework import serializers

from .models import Estudiante, Docente, Curso, Ciclo, Asistencia, Facultad, Curso_has_Estudiante, CategoriaAsistencia

class EstudianteSerializer(serializers.ModelSerializer):
        class Meta:
                model = Estudiante
                fields = '__all__'

class DocenteSerializer(serializers.ModelSerializer):
        class Meta:
                model = Docente
                fields = '__all__'

class CursoSerializer(serializers.ModelSerializer):
        class Meta:
                model = Curso
                fields = '__all__'

class CicloSerializer(serializers.ModelSerializer):
        class Meta:
                model = Ciclo
                fields = '__all__'

class EstudianteSerializer(serializers.ModelSerializer):
        class Meta:
                model = Estudiante
                fields = '__all__'

class AsistenciaSerializer(serializers.ModelSerializer):
        class Meta:
                model = Asistencia
                fields = '__all__'

class FacultadSerializer(serializers.ModelSerializer):
        class Meta:
                model = Facultad
                fields = '__all__'

class Curso_has_EstudianteSerializer(serializers.ModelSerializer):
        class Meta:
                model = Curso_has_Estudiante
                fields = '__all__'

class CategoriaAsistenciaSerializer(serializers.ModelSerializer):
        class Meta:
                model = CategoriaAsistencia
                fields = '__all__'
                


