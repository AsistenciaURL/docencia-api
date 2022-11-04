from django.db import models

class professor(models.Model):
        id = models.CharField(primary_key = True, max_length=50) 
        carnet = models.CharField(max_length=20)
        name = models.CharField(max_length=50) 
        email = models.CharField(max_length=50)

        def __str__(self):
                return f'{self.name}'


class semester(models.Model):
        id = models.AutoField(primary_key = True)
        name = models.CharField(max_length=50) 
        
        def __str__(self):
                return f'{self.name}'

class faculty(models.Model):
        id = models.AutoField(primary_key = True)
        name = models.CharField(max_length=50) 
        
        def __str__(self):
                return f'{self.name}'

class assistance_category(models.Model):
        id = models.AutoField(primary_key = True)
        name = models.CharField(max_length=50) 
        
        def __str__(self):
                return f'{self.id}'

class student(models.Model):
        id = models.CharField(primary_key = True, max_length=20)
        name = models.CharField(max_length=50) 
        email = models.CharField(max_length=50)

        faculty_id = models.ForeignKey(faculty, on_delete=models.CASCADE)
        
        def __str__(self):
                return f'{self.name}'

class course(models.Model):
        id = models.AutoField(primary_key = True)
        name = models.CharField(max_length=50) 
        section = models.IntegerField()
        date = models.DateField()
        class_total = models.IntegerField()

        semester_id = models.ForeignKey(semester, on_delete=models.CASCADE)
        faculty_id = models.ForeignKey(faculty, on_delete=models.CASCADE)
        professor_id = models.ForeignKey(professor, related_name='course' ,on_delete=models.CASCADE)
        student_id = models.ManyToManyField(student, related_name='courses')

        def __str__(self):
                return f'{self.name}'


class qr(models.Model):
        id = models.AutoField(primary_key = True)
        limit_date = models.DateField() 
        
        course_id = models.ForeignKey(course, related_name='qr', on_delete=models.CASCADE)
        def __str__(self):
                return f'{self.id}'

class device(models.Model):
        id = models.AutoField(primary_key = True)
        name = models.CharField(max_length=45)
        
        qr_id = models.ForeignKey(qr, on_delete=models.CASCADE)
        def __str__(self):
                return f'{self.id}'

class course_student(models.Model):
        id = models.AutoField(primary_key = True)
        course_id = models.ForeignKey(course, on_delete=models.CASCADE)
        student_id = models.ForeignKey(student, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.id}'


class assistance(models.Model):
        id = models.AutoField(primary_key = True)
        date = models.DateField()
        observations = models.CharField(max_length=200) 

        course_id = models.ForeignKey(course, on_delete=models.CASCADE)
        student_id = models.ForeignKey(student, on_delete=models.CASCADE)
        assistance_category_id = models.ForeignKey(assistance_category, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.id}'





