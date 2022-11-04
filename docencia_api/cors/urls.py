# django
from django.contrib import admin
from django.db import router
from django.urls import path, include

# rest framework
from rest_framework.routers import DefaultRouter

# views Sets
from .views import *

router = DefaultRouter()
router.register(r'student', studentViewSet)
router.register(r'professor', professorViewSet)
router.register(r'course', courseViewSet)
router.register(r'qr', qrViewSet)
router.register(r'device', deviceViewSet)
router.register(r'semester', semesterViewSet)
router.register(r'assistance', assistanceViewSet)
router.register(r'faculty', facultyViewSet)
router.register(r'course_student', course_studentViewSet)
router.register(r'assistance_category', assistance_categoryViewSet)

urlpatterns = router.urls

urlpatterns += [
        path('get_qr/', qr_list),
        path('get_course/', course_list),
        path('get_professor/', professor_list),
        
]