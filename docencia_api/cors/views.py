#Django Rest Framework
import json

from django.http import HttpResponse, JsonResponse
from rest_framework.views import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from .models import student, professor, course, semester, assistance, faculty, course_student, assistance_category, qr, device

from .serializers import studentSerializer, professorSerializer, courseSerializer, semesterSerializer, assistanceSerializer, facultySerializer, course_studentSerializer, assistance_categorySerializer, qrSerializer, deviceSerializer

# serializers


class studentViewSet(viewsets.ModelViewSet):
        queryset = student.objects.all()
        serializer_class = studentSerializer

class professorViewSet(viewsets.ModelViewSet):
        queryset = professor.objects.all()
        serializer_class = professorSerializer

class courseViewSet(viewsets.ModelViewSet):
        queryset = course.objects.all()
        serializer_class = courseSerializer

class semesterViewSet(viewsets.ModelViewSet):
        queryset = semester.objects.all()
        serializer_class = semesterSerializer

class assistanceViewSet(viewsets.ModelViewSet):
        queryset = assistance.objects.all()
        serializer_class = assistanceSerializer

class facultyViewSet(viewsets.ModelViewSet):
        queryset = faculty.objects.all()
        serializer_class = facultySerializer

class course_studentViewSet(viewsets.ModelViewSet):
        queryset = course_student.objects.all()
        serializer_class = course_studentSerializer

class assistance_categoryViewSet(viewsets.ModelViewSet):
        queryset = assistance_category.objects.all()
        serializer_class = assistance_categorySerializer

class qrViewSet(viewsets.ModelViewSet):
        queryset = qr.objects.all()
        serializer_class = qrSerializer

class deviceViewSet(viewsets.ModelViewSet):
        queryset = device.objects.all()
        serializer_class = deviceSerializer

def qr_validate(request, id):
        response_data = {}
        response_data['result'] = 'error'
        response_data['message'] = id 

        _qr = qr.objects.get(id=id)
        print('Test')
        print(_qr)

        response_data['qr'] = 'error'
        response_data['data'] = _qr.latitude

        return JsonResponse(response_data, safe=False)

def get_course_with_students(request, id):
        response_data = {}
        response_data['result'] = 'success'
        response_data['message'] = id

        obj = course.objects.filter(professor=id)
        print('Test')
        print(obj)

        response_data['qr'] = obj

        data = list(course.objects.filter(professor=id).values()) 
        return JsonResponse(data, safe=False)  # or JsonResponse({'data': data})
        # response_data['data'] = _qr.latitude

        return JsonResponse(list(obj), safe=False)
