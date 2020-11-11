from django.contrib import admin
from .models import InternshipRole ,Student, InternshipQuestion, InternshipAnswer, InternshipApplication
# Register your models here.
admin.site.register(InternshipRole)
admin.site.register(Student)
admin.site.register(InternshipQuestion)
admin.site.register(InternshipAnswer)
admin.site.register(InternshipApplication)
