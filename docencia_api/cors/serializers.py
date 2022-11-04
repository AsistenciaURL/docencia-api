from rest_framework import serializers

from .models import student, professor, course, semester, assistance, faculty, course_student, assistance_category, qr, device

class qrSerializer(serializers.ModelSerializer): 
        class Meta:
                model = qr
                fields = '__all__'
                #depth = 2

class courseSerializer(serializers.ModelSerializer):
        qr = qrSerializer(read_only=True, many=True)
        #course_id = serializers.PrimaryKeyRelatedField(queryset = course.objects.all(), many=True)
        #qr = serializers.SlugRelatedField(
        #        many = True,
        #        read_only = True,
        #        slug_field = 'id' 
        #)
        #qr = serializers.PrimaryKeyRelatedField(queryset = qr.objects.all())
        class Meta:
                model = course
                fields = '__all__' 
                depth = 1

class professorSerializer(serializers.ModelSerializer):
        course = courseSerializer(read_only=True, many=True)
        #course = serializers.SlugRelatedField(
        #        many = True,
        #        read_only = True,
        #        slug_field = 'name' 
        #)
        class Meta:
                model = professor
                fields = '__all__'

class studentSerializer(serializers.ModelSerializer):    
        class Meta:
                model = student
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
                

class deviceSerializer(serializers.ModelSerializer):
        class Meta:
                model = device
                fields = '__all__'

class pruebaSerializer(serializers.ModelSerializer): 
        class Meta:
                model = qr
                fields = '__all__'
                depth = 2

class prueba2Serializer(serializers.ModelSerializer): 
        qr = qrSerializer(read_only=True, many=True)
        class Meta:
                model = course
                fields = '__all__' 

class prueba3Serializer(serializers.ModelSerializer): 
        course = courseSerializer(read_only=True, many=True)
        class Meta:
                model = professor
                fields = '__all__' 