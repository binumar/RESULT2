from django.shortcuts import render, get_object_or_404, redirect
from profiles.models import StudentProfile, Level, AcademicCalender, Term, Session
from .models import SubjectEntry, Subject, Report, Pin
from .forms import PinVerificationForm
from profiles.models import Subject
from django.db.models import Q

from .forms import SubjectEntryForm
from django.forms import modelformset_factory
from django.contrib import messages

# def form_master_upload_view(request):
#     level = request.user.tprofile.level
#     subjects = Subject.objects.all()
#     context = {
#         'level':level,
#         'subjects':subjects,
#     }
#     return render(request, 'teacher_subjects_view.html', context)

def form_master_upload_view(request):
    level = request.user.fmprofile.level
    subjects = Subject.objects.all()
    context = {
        'level':level,
        'subjects':subjects,
    }
    return render(request, 'teacher_subjects_view.html', context)

def admin_upload_score_view(request):
    grade_levels = Level.objects.all()
    subjects = Subject.objects.all()
    context = {
        'grade_levels': grade_levels,
        'subjects': subjects,
    }
    return render(request, 'admin_upload_score_view.html', context)

def subject_teacher_upload_view(request):

    teacher = request.user.tprofile  # Assuming 'tprofile' is the related field for TeacherProfile
    
    # Get the subject from the teacher's profile (TeacherProfile has a foreign key to Subject)
    subject = teacher.subject  # This will give the specific subject associated with this teacher's profile
    
    # You can also retrieve multiple subjects if needed
    # subjects = Subject.objects.filter(teacher=teacher) # Only if you need multiple subjects linked to a teacher
    
    # Fetch all levels as before
    levels = Level.objects.all()
    
    context = {
        'teacher':teacher,
        'subject':subject,
        'levels':levels,
    }
    return render(request, 'teacher_classes_view.html', context)

def success(request):

    return render(request, 'grade_levels.html')
# Create your views here.
def score_students(request, grade_level_id, subject_id):
    grade_level = get_object_or_404(Level, id=grade_level_id)
    subject = get_object_or_404(Subject, id=subject_id)

    #change 1
    queryset =SubjectEntry.objects.filter(student__level=grade_level, subject=subject)
    
    students = StudentProfile.objects.filter(level=grade_level)

    ScoreFormSet = modelformset_factory(SubjectEntry, form=SubjectEntryForm, extra=0, can_delete=False)
    initial_data = [{
        'student': student, 
        'subject': subject
        } for student in students]


    if request.method == 'POST':
        formset = ScoreFormSet(request.POST, queryset=queryset,initial=initial_data)
        # formset = ScoreFormSet(request.POST, queryset=Score.objects.none(), initial=initial_data)
        if formset.is_valid():
            # for form in formset:
            #     form.save()
            formset.save()
            
            # Handle success, e.g., redirect or display a success message
        else:
            print(formset.errors)  # This will show validation errors in your console
            for form in formset:
                print(form.errors)
    else:
        # formset = ScoreFormSet(request.POST, queryset=Score.objects.none(), initial=initial_data)
        formset = ScoreFormSet(request.POST or None, queryset=queryset, initial=initial_data)
        
    context = {
        'grade_level': grade_level,
        'subject': subject,
        'formset': formset,
    }
    return render(request, 'score_students.html', context)


# def level_results(request, class_level_id):
#     # Retrieve the class level and associated students
#     class_level = get_object_or_404(Level, id=class_level_id)
#     students = StudentProfile.objects.filter(level=class_level)
    
#     # Initialize a list to hold each student's scores and total score
#     student_scores = []

#     # Calculate total score for each student
#     for student in students:
#         scores = StudentScore.objects.filter(student=student)
#         total_score = sum(score.total for score in scores)
#         student_scores.append({
#             'student': student,
#             'scores': scores,
#             'total_score': total_score,
#             'position': None
#         })

#     # Sort students by total_score in descending order
#     student_scores.sort(key=lambda x: x['total_score'], reverse=True)

#     # Apply ranking logic
#     current_rank = 0
#     global_rank = 0
#     current_total_score = None

#     for student_score in student_scores:
#         global_rank += 1
#         if student_score['total_score'] != current_total_score:
#             current_total_score = student_score['total_score']
#             current_rank = global_rank

#         # Insert the rank as the position after the total_score key
#         student_score['position'] = current_rank

#         # Create a Report entry for each student
#         # Ensure you have the necessary fields to create the Report
#         Report.objects.create(
#             session=None,  # You need to set the correct session
#             term=None,  # You need to set the correct term
#             student=student_score['student'],
#             subjects=scores,  # Assuming subjects are the StudentScore records
#             level=class_level,
#             is_approved=False,  # Assuming it's not approved yet
#             overall_total=student_score['total_score'],
#             position=student_score['position'],
#             next_term_begin=None  # Optional, can be updated later
#         )

#     return render(request, 'class_overall_scores.html', {
#         'class_level': class_level,
#         'student_scores': student_scores
#     })

# def level_results(request, class_level_id):
#     # Retrieve the class level and associated students
#     class_level = get_object_or_404(Level, id=class_level_id)
#     students = StudentProfile.objects.filter(level=class_level)
    
#     # Initialize a list to hold each student's scores and total score
#     student_scores = []

#     # Calculate total score for each student
#     for student in students:
#         scores = StudentScore.objects.filter(student=student)
#         total_score = sum(score.total for score in scores)
#         student_scores.append({
#             'student': student,
#             'scores': scores,
#             'total_score': total_score,
#             'position': None
#         })

#     # Sort students by total_score in descending order
#     student_scores.sort(key=lambda x: x['total_score'], reverse=True)

#     # Apply ranking logic
#     current_rank = 0
#     global_rank = 0
#     current_total_score = None

#     for student_score in student_scores:
#         global_rank += 1
#         if student_score['total_score'] != current_total_score:
#             current_total_score = student_score['total_score']
#             current_rank = global_rank

#         # Insert the rank as the position after the total_score key
#         student_score['position'] = current_rank

#         # Use get_or_create to avoid duplicates
#         report, created = Report.objects.get_or_create(
#             session=None,  # You need to set the correct session
#             term=None,  # You need to set the correct term
#             student=student_score['student'],
#             level=class_level,
#             defaults={  # Fields to create if the report does not exist
#                 'subjects': scores,  # Assuming subjects are the StudentScore records
#                 'is_approved': False,  # Assuming it's not approved yet
#                 'overall_total': student_score['total_score'],
#                 'position': student_score['position'],
#                 'next_term_begin': None  # Optional, can be updated later
#             }
#         )

#     return render(request, 'class_overall_scores.html', {
#         'class_level': class_level,
#         'student_scores': student_scores
#     })

def generate_result_view(request):
    levels = Level.objects.all()
    context = {
        'levels':levels,
    }
    return render(request, 'level/generate_result_view.html', context)



def generate_class_result(request, class_level_id):
    # Get the active academic calendar
    calender = AcademicCalender.objects.get(is_active=True)
    session = calender.session
    term = calender.term
    next_term = calender.next_term_begins
    closes_on = calender.end
    
    # Retrieve the class level and associated students
    class_level = get_object_or_404(Level, id=class_level_id)
    students = StudentProfile.objects.filter(level=class_level)
    
    # Initialize a list to hold each student's scores and total score
    student_scores = []

    # Calculate total score for each student
    for student in students:
        out_of = StudentProfile.objects.filter(level = student.level).count()
        scores = SubjectEntry.objects.filter(student=student)
        total_score = sum(score.total for score in scores)
        student_scores.append({
            'student': student,
            'scores': scores,
            'total_score': total_score,
            'position': None,
            'report_pin': None,
        })

    # Sort students by total_score in descending order
    student_scores.sort(key=lambda x: x['total_score'], reverse=True)

    # Apply ranking logic
    current_rank = 0
    global_rank = 0
    current_total_score = None

    for student_score in student_scores:
        global_rank += 1
        if student_score['total_score'] != current_total_score:
            current_total_score = student_score['total_score']
            current_rank = global_rank

        # Insert the rank as the position after the total_score key
        student_score['position'] = current_rank
        scratch_pin = Pin.objects.create()

        # Use update_or_create to update existing reports or create new ones
        report, created = Report.objects.update_or_create(
            session=session,  # You need to set the correct session
            term=term,  # You need to set the correct term
            student=student_score['student'],
            level=class_level,
            defaults={  # Fields to update or create
                'is_approved': True,  # Assuming it's not approved yet
                'overall_total': student_score['total_score'],
                'position': student_score['position'],
                'next_term_begin': next_term  # Optional, can be updated later
            }
        )
        
        # Use set() to update the many-to-many relationship with the new subjects
        report.subjects.set(student_score['scores'])
        report.report_pin = scratch_pin.pin
        report.closes_on = closes_on
        report.out_of = out_of
        report.save()

    return redirect('reports:students-reports')
  

    # # Render the response with class-level and student score details
    # return render(request, 'class_overall_scores.html', {
    #     'class_level': class_level,
    #     'student_scores': student_scores
    # })

def students_reports(request):
    students_reports = Report.objects.all()
    context = {
        'students_reports':students_reports,
    }
    return render(request, 'students_reports.html', context)



def class_reports(request):
    level = request.user.tprofile.level
    class_reports = Report.objects.filter(level=level, is_approved = True)
    print(class_reports)
    context = {
        'class_reports':class_reports,
    }
    return render(request, 'class_reports.html',context)


def student_report(request, student_id):
    my_student = StudentProfile.objects.filter(id = student_id)
    report = Report.objects.filter(is_approved =True, student = student_id).first()
    print(my_student)
    context = {
        'report':report,
    }
    return render(request, 'student_report.html',context)

def scratch_cards(request):
    scratch_cards = Report.objects.all()
    context = {
        'scratch_cards':scratch_cards,
    }
    return render(request, 'scratch_cards.html',context)

def report_search(request):
    report = None  # Initialize the report variable outside the GET block to avoid potential errors.
    
    if request.method == 'GET':
        pin = request.GET.get('scratchPin')  # Get the pin from the query params
        
        if pin:  # Ensure a pin was provided.
            report = Report.objects.filter(pin=pin).first()  # Get the report(s) matching the pin.
            print(report)
            
            # If no report is found, report will be an empty queryset.
            if not report:
                print('no report found')
                report = None  # Set report to None if no match is found.
    
    context = {'report': report}
    return render(request, 'report_search.html',context)

def verify_pin_and_get_report(request):
    # Initialize form correctly for GET requests
    if request.method == 'POST':
        form = PinVerificationForm(request.POST)
        if form.is_valid():
            admission_number = form.cleaned_data['admission_number']
            entered_pin = form.cleaned_data['pin']
            print(f'{admission_number} {entered_pin}')  # Debug output to see form data

            try:
                # Step 1: Check if there's a valid PIN in the system
                pin = Pin.objects.filter(pin=entered_pin).first()
            except Pin.DoesNotExist:
                messages.error(request, 'Invalid PIN. Please try again.')
                return redirect('verify_pin_and_get_report')  # Redirect to the form again

            # Step 2: If the PIN is valid, retrieve the student based on admission number
            try:
                student = StudentProfile.objects.filter(admission_number=admission_number).first()
            except StudentProfile.DoesNotExist:
                messages.error(request, 'Invalid admission number.')
                return redirect('verify_pin_and_get_report')  # Redirect to the form again

            # Step 3: Fetch the report for this student
            try:
                report = Report.objects.get(student=student)
            except Report.DoesNotExist:
                messages.error(request, 'No report found for this student.')
                return redirect('verify_pin_and_get_report')  # Redirect to the form again

            # Step 4: Update the report's is_approved field to True
            report.is_approved = True
            report.save()

            # Step 5: Mark the PIN as used
            pin.is_used = True
            pin.save()

            messages.success(request, 'Access granted to the report.')
            return render(request, 'report_detail.html', {'report': report, 'student': student})
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = PinVerificationForm()  # Initialize the form for GET requests

    return render(request, 'verify_pin.html', {'form': form})


def checked_result(request, report_id):
    
    report = Report.objects.get(id=report_id)
    context = {
        'report':report
    }
    return render(request, 'checked_result.html',context)


def uploaded_score(request):
    subject = Subject.objects.get(id = 2)
    level = Level.objects.get(id =5)
    # scores = SubjectEntry.objects.filter(subject = subject, level = level)
    # scores = SubjectEntry.objects.filter(Q(ca1=0,ca2=0,exam=0) | Q(ca1=0)| Q(ca2=0)| Q(exam=0))
    scores = SubjectEntry.objects.filter(subject = subject)
    context = {
        'scores':scores,
        'level':level,
    }
    return render(request, 'uploaded_score.html', context)



