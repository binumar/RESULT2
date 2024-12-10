from django.contrib import admin
from .models import Level, SubjectEntry, Subject, Report, Pin

# Register your models here.
admin.site.register([Level, SubjectEntry, Subject, Report, Pin])