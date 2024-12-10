from django.urls import path
from . import views


app_name = 'profiles'

urlpatterns = [
    path('bulk-create', views.bulk_create,name='bulk-create'),
    path('signup/', views.signup, name = 'signup'),
    path('staff-signup/', views.staff_signup, name = 'staff-signup'),
    path('form-master-signup/', views.form_master_signup, name = 'form-master-signup'),
    path('update-form-master/', views.update_form_master, name = 'update-form-master'),
    path('update-student/', views.update_student, name = 'update-student'),
    path('update-staff/', views.update_staff, name = 'update-staff'),
    path('login/', views.Login, name = 'login'),
    path('logout/', views.Logout, name = 'logout'),
    path('admin-dashboard/', views.admin_dashboard, name = 'admin-dashboard'),
    path('form-master-dashboard/', views.form_master_dashboard, name = 'form-master-dashboard'),
    path('teacher-dashboard/', views.teacher_dashboard, name = 'teacher-dashboard'),
    path('student-dashboard/', views.student_dashboard, name = 'student-dashboard'),
    path('students/', views.students, name = 'students'),
    path('staffs/', views.staffs, name = 'staffs'),
    path('subjects/', views.subjects, name = 'subjects'),
    path('levels/', views.levels, name = 'levels'),
    path('profiles/', views.profiles, name = 'profiles')
]