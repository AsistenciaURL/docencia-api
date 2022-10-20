from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.

class Docente(models.Model):
        carnet = models.CharField(primary_key = True, max_length=20)
        nombre = models.CharField(max_length=50) 
        correo = models.CharField(max_length=50) 
        firebaseid = models.CharField(max_length=50) 


        def __str__(self):
                return f'{self.nombre}'


class Ciclo(models.Model):
        idCiclo = models.IntegerField(primary_key = True)
        nombre = models.CharField(max_length=50) 
        
        def __str__(self):
                return f'{self.nombre}'

class Facultad(models.Model):
        idFacultad = models.IntegerField(primary_key = True)
        nombre = models.CharField(max_length=50) 
        
        def __str__(self):
                return f'{self.nombre}'

class CategoriaAsistencia(models.Model):
        idFacultad = models.IntegerField(primary_key = True)
        Tipo = models.CharField(max_length=50) 
        
        def __str__(self):
                return f'{self.idFacultad}'


class Estudiante(models.Model):
        Carnet = models.CharField(primary_key = True, max_length=20)
        Nombre = models.CharField(max_length=50) 
        Correo = models.CharField(max_length=50)
        Facultad_idFacultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.Nombre}'

class Curso(models.Model):
        idCurso = models.IntegerField(primary_key = True)
        Nombre = models.CharField(max_length=50) 
        Seccion = models.IntegerField()
        Anio = models.DateField()

        Ciclo_idciclo = models.ForeignKey(Ciclo, on_delete=models.CASCADE)
        Facultad_idFacultad = models.ForeignKey(Facultad, on_delete=models.CASCADE)
        Docente_Carnet = models.ForeignKey(Docente, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.Nombre}'

class Curso_has_Estudiante(models.Model):
        Curso_idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        Estudiante_carnet = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.id}'


class Asistencia(models.Model):
        idAsistencia = models.IntegerField(primary_key = True)
        Fecha = models.DateField()
        Observacion = models.CharField(max_length=200) 

        Curso_idCurso = models.ForeignKey(Curso, on_delete=models.CASCADE)
        Estudiante_Carnet = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
        CategoriasAsistencia_idCategoria = models.ForeignKey(CategoriaAsistencia, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.idAsistencia}'





