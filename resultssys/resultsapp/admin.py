from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(School)   
admin.site.register(SchoolAdministrator)
admin.site.register(AcademicPeriod)
admin.site.register(Subject)
admin.site.register(Student)
admin.site.register(GradingStructure)
admin.site.register(Result)
