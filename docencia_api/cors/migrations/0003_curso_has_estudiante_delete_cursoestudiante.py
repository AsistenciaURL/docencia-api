# Generated by Django 4.1.2 on 2022-10-21 07:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cors', '0002_rename_curso_has_estudiante_cursoestudiante'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso_has_Estudiante',
            fields=[
                ('idCurso_has_Estudiante', models.AutoField(primary_key=True, serialize=False)),
                ('Curso_idCurso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cors.curso')),
                ('Estudiante_carnet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cors.estudiante')),
            ],
        ),
        migrations.DeleteModel(
            name='CursoEstudiante',
        ),
    ]