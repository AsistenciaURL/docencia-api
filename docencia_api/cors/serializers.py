from dataclasses import field
from rest_framework import serializers

from .models import student, professor, course, semester, assistance, faculty, course_student, assistance_category, qr, device

class studentSerializer(serializers.ModelSerializer):
        class Meta:
                model = student
                fields = '__all__'

class professorSerializer(serializers.ModelSerializer):
        class Meta:
                model = professor
                fields = '__all__'

class courseSerializer(serializers.ModelSerializer):
        class Meta:
                model = course
                fields = '__all__'

class semesterSerializer(serializers.ModelSerializer):
        class Meta:
                model = semester
                fields = '__all__'

class studentSerializer(serializers.ModelSerializer):
        class Meta:
                model = student
                fields = '__all__'

class assistanceSerializer(serializers.ModelSerializer):
        class Meta:
                model = assistance
                fields = '__all__'

class facultySerializer(serializers.ModelSerializer):
        class Meta:
                model = faculty
                fields = '__all__'

class course_studentSerializer(serializers.ModelSerializer):
        class Meta:
                model = course_student
                fields = '__all__'

class assistance_categorySerializer(serializers.ModelSerializer):
        class Meta:
                model = assistance_category
                fields = '__all__'
                
class qrSerializer(serializers.ModelSerializer):
        class Meta:
                model = qr
                fields = '__all__'

class deviceSerializer(serializers.ModelSerializer):
        class Meta:
                model = device
                fields = '__all__'

