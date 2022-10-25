from django.contrib import admin

# Register your models here.

from .models import student, professor, course, semester, assistance, faculty, course_student, assistance_category, qr, device


admin.site.register(student)
admin.site.register(professor)
admin.site.register(course)
admin.site.register(semester)
admin.site.register(faculty)
admin.site.register(course_student)
admin.site.register(assistance)
admin.site.register(assistance_category)
admin.site.register(qr)
admin.site.register(device)