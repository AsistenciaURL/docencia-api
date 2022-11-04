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

class course(models.Model):
        id = models.AutoField(primary_key = True)
        name = models.CharField(max_length=50) 
        section = models.IntegerField()
        class_total = models.IntegerField(default=0)

        semester = models.ForeignKey(semester, on_delete=models.CASCADE)
        faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
        professor = models.ForeignKey(professor, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.name}'

class qr(models.Model):
        id = models.AutoField(primary_key = True)
        limit_date = models.DateTimeField() 
        init_date = models.DateTimeField()
        latitude = models.FloatField()
        longitude = models.FloatField()
        
        course = models.ForeignKey(course, on_delete=models.CASCADE)
        def __str__(self):
                return f'{self.id}'

class device(models.Model):
        id = models.CharField(max_length=50, primary_key = True)
        name = models.CharField(max_length=45)
        
        qr = models.ForeignKey(qr, on_delete=models.CASCADE)
        def __str__(self):
                return f'{self.id}'

class student(models.Model):
        id = models.CharField(primary_key = True, max_length=20)
        name = models.CharField(max_length=50) 
        email = models.CharField(max_length=50)

        faculty = models.ForeignKey(faculty, on_delete=models.CASCADE)
        device = models.ForeignKey(device, on_delete=models.CASCADE, default=None, blank=True, null=True, unique=True)
        
        def __str__(self):
                return f'{self.name}'

class course_student(models.Model):
        id = models.AutoField(primary_key = True)
        course = models.ForeignKey(course, on_delete=models.CASCADE)
        student = models.ForeignKey(student, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.id}'


class assistance(models.Model):
        id = models.AutoField(primary_key = True)
        date = models.DateField()
        observations = models.CharField(max_length=200) 

        course = models.ForeignKey(course, on_delete=models.CASCADE)
        student = models.ForeignKey(student, on_delete=models.CASCADE)
        assistance_category = models.ForeignKey(assistance_category, on_delete=models.CASCADE)
        
        
        def __str__(self):
                return f'{self.id}'





