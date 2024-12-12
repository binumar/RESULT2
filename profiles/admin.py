from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import  User, StudentProfile, TeacherProfile, AdminProfile, Session,Section,Term,AcademicCalender, SchoolInfo


class CustomUserAdmin(UserAdmin):
    fieldsets = (
        * UserAdmin.fieldsets,
        (
            'Custom Field Heading',
            {
                'fields':('is_teacher', 'is_student', 'is_support')
            }
        )
    )

admin.site.register(User, CustomUserAdmin)

admin.site.register([StudentProfile, TeacherProfile, AdminProfile, Session,Section,Term,AcademicCalender])
admin.site.register(SchoolInfo)