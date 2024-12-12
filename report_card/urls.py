from django.urls import path
from . import views

app_name = 'reports'

urlpatterns = [
    path('scratch-cards/', views.scratch_cards, name='scratch-cards'),
    path('check/', views.report_search, name='check'),
    path('generate-result-view/', views.generate_result_view, name='generate-result-view'),
    path('form-master-upload-view/', views.form_master_upload_view, name='form-master-upload-view'),
    path('students-reports/', views.students_reports, name='students-reports'),
    path('class-reports/<str:class_id>/', views.class_reports, name = 'class-reports'),
    path('student-report/<str:student_id>/', views.student_report,name = 'student-report'),
    path('admin-upload-score-view/', views.admin_upload_score_view, name='admin-upload-score-view'),
    path('generate-class-result/<int:class_level_id>', views.generate_class_result, name='generate-class-result'),
    path('success/', views.success, name='success'),
    path('score-students/<int:grade_level_id>/<int:subject_id>/', views.score_students, name='score_students'),
    path('verify-pin/', views.verify_pin_and_get_report, name='verify_pin_and_get_report'),

    path('subject-teacher-upload-view/', views.subject_teacher_upload_view, name='subject-teacher-upload-view'),
    path('checked-result/<str:report_id>', views.checked_result, name ='checked-result'),
    path('uploaded-scores/', views.uploaded_score, name ='uploaded-score')
]
