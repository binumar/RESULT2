from django.shortcuts import render, redirect
from  .forms import RegisterationForm, StudentProfileForm, TeacherProfileForm, FormMasterProfileForm
from .models import StudentProfile, TeacherProfile, AdminProfile, Level,FormMasterProfile, User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# from django.shortcuts import render
# from django.core.exceptions import ObjectDoesNotExist
# from django.db import IntegrityError
# from .models import User, StudentProfile, Level
# import logging

# # Set up logger
# logger = logging.getLogger(__name__)

# def bulk_create(request):
#     # List of students with user-related information
#     students_data = [
#         {"full_name": "ABBA M. AJI", "username": "FSTCG2024038", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "ADAMA BUKAR MAIGARI", "username": "FSTCG2024039", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "AISHA HARUNA ABUBAKAR", "username": "FSTCG2024043", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "ALI GARBA", "username": "FSTCG2024041", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "ZAINAB SAFIYANU BULAMA", "username": "FSTCG2024067", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "USMAN BABA SHEHU", "username": "FSTCG2024066", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "UMAR SAJE MUSA", "username": "FSTCG2024065", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "UMAR ABACHA", "username": "FSTCG2024064", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "SULEIMAN ALI KADUGUM", "username": "FSTCG2024063", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "SERAH HYGINUS", "username": "FSTCG2024062", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "SALEH SULEIMAN MAKINTA", "username": "FSTCG2024061", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUSA YAWALE", "username": "FSTCG2024060", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUSA MUHAMMAD KADIGA", "username": "FSTCG2024059", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUSA IBRAHIM AZAM", "username": "FSTCG2024058", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUHAMMAD TAHIR", "username": "FSTCG2024057", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUHAMMAD SHEHU YUSUF", "username": "FSTCG2024056", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUHAMMAD USMAN KARAGE", "username": "FSTCG2024055", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "MUHAMMAD ABDULMUMINI", "username": "FSTCG2024054", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "KHALID SALISU YAHAYYA", "username": "FSTCG2024053", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "ISHAQ ISHA", "username": "FSTCG2024052", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "IBRAHIM KHALIL HASSAN", "username": "FSTCG2024051", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "HANS MUSA FABIAN", "username": "FSTCG2024050", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "HADIZA ISAH KAGAMU", "username": "FSTCG2024049", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "FATIMA UMAR MUSA", "username": "FSTCG2024048", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "FATIMA UMAR GARBA", "username": "FSTCG2024047", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "FATIMA MUHAMMAD", "username": "FSTCG2024046", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "FATIMA BABANGIDA TALLE", "username": "FSTCG2024045", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "FATIMA ALI WAKILI", "username": "FSTCG2024044", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "ALIYU ALI UMAR", "username": "FSTCG2024042", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "AISHA KAIGAMA UMAR", "username": "FSTCG2024040", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
#         {"full_name": "AHMAD IDRIS ABUBAKAR", "username": "FSTCG2024043", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"}
#         # Add more students as needed...
#     ]
    
#     # Default password for all users
#     default_password = "CBT.2024"

#     # Step 1: Create Users (with password hashing)
#     users = []
#     for student in students_data:
#         user = User(
#             username=student["username"],
#             email=student["email"],
#             is_student=True
#         )
#         # Set the default password and hash it
#         user.set_password(default_password)
#         users.append(user)

#     # Bulk create users
#     try:
#         User.objects.bulk_create(users)
#         logger.info("Users created successfully.")
#     except IntegrityError as e:
#         logger.error(f"Error creating users: {e}")
#         return render(request, 'error.html', {"message": "Error creating users."})

#     # Step 2: Create Profiles for each user
#     profiles = []
#     for index, student in enumerate(students_data):
#         user = users[index]  # Get the corresponding user object
#         try:
#             level = Level.objects.get(name=student["level"])
#             logger.info(f"Level '{student['level']}' found for {student['full_name']}.")
#         except Level.DoesNotExist:
#             logger.error(f"Level '{student['level']}' does not exist for student '{student['full_name']}'.")
#             return render(request, 'error.html', {"message": f"Level '{student['level']}' does not exist."})
        
#         profile = StudentProfile(
#             user=user,
#             full_name=student["full_name"],
#             level=level,
#             year_of_admission='2023'
#         )
#         profiles.append(profile)

#     # Bulk create profiles
#     try:
#         StudentProfile.objects.bulk_create(profiles)
#         logger.info("Student profiles created successfully.")
#     except IntegrityError as e:
#         logger.error(f"Error creating student profiles: {e}")
#         return render(request, 'error.html', {"message": "Error creating student profiles."})

#     # Return success page
#     return render(request, 'data/bulk.html', {"message": "Users and profiles created successfully."})


def bulk_create(request):

    # List of students with user-related information (username, email, phone number, address)
    students_data = [
        {"full_name": "ABBA M. AJI", "username": "FSTCG2024038", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "ADAMA BUKAR MAIGARI", "username": "FSTCG2024039", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "AISHA HARUNA ABUBAKAR", "username": "FSTCG2024043", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "ALI GARBA", "username": "FSTCG2024041", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "ZAINAB SAFIYANU BULAMA", "username": "FSTCG2024067", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "USMAN BABA SHEHU", "username": "FSTCG2024066", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "UMAR SAJE MUSA", "username": "FSTCG2024065", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "UMAR ABACHA", "username": "FSTCG2024064", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "SULEIMAN ALI KADUGUM", "username": "FSTCG2024063", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "SERAH HYGINUS", "username": "FSTCG2024062", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "SALEH SULEIMAN MAKINTA", "username": "FSTCG2024061", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUSA YAWALE", "username": "FSTCG2024060", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUSA MUHAMMAD KADIGA", "username": "FSTCG2024059", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUSA IBRAHIM AZAM", "username": "FSTCG2024058", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUHAMMAD TAHIR", "username": "FSTCG2024057", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUHAMMAD SHEHU YUSUF", "username": "FSTCG2024056", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUHAMMAD USMAN KARAGE", "username": "FSTCG2024055", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "MUHAMMAD ABDULMUMINI", "username": "FSTCG2024054", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "KHALID SALISU YAHAYYA", "username": "FSTCG2024053", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "ISHAQ ISHA", "username": "FSTCG2024052", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "IBRAHIM KHALIL HASSAN", "username": "FSTCG2024051", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "HANS MUSA FABIAN", "username": "FSTCG2024050", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "HADIZA ISAH KAGAMU", "username": "FSTCG2024049", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "FATIMA UMAR MUSA", "username": "FSTCG2024048", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "FATIMA UMAR GARBA", "username": "FSTCG2024047", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "FATIMA MUHAMMAD", "username": "FSTCG2024046", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "FATIMA BABANGIDA TALLE", "username": "FSTCG2024045", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "FATIMA ALI WAKILI", "username": "FSTCG2024044", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "ALIYU ALI UMAR", "username": "FSTCG2024042", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "AISHA KAIGAMA UMAR", "username": "FSTCG2024040", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"},
        {"full_name": "AHMAD IDRIS ABUBAKAR", "username": "FSTCG2024043", "password": "CBT.2024", "level": "JSS 2B","email":"STUDENT@GMAIL.COM"}
        
        # {"username": "student1", "email": "student1@example.com", "phone_number": "1234567890", "address": "123 Main St"},
        # {"username": "student2", "email": "student2@example.com", "phone_number": "0987654321", "address": "456 Elm St"},
        # Add more students as needed
    ]

    # Default password for all users
    default_password = "CBT.2024"  # Change this to whatever default password you want

    # # Step 1: Create Custom Users (with password hashing)
    users = []
    for student in students_data:
        user = User(
            username=student["username"],
            email=student["email"],
            is_student =True
        )
        # Set the default password and hash it
        user.set_password(default_password)  # This hashes the password
        users.append(user)

    # Bulk create users
    User.objects.bulk_create(users)

    # Step 2: Create Profiles for each user
    profiles = []
    for index, student in enumerate(students_data):
        user = users[index]  # Get the corresponding user object
        level = Level.objects.get(name = student["level"])
        profile = StudentProfile(
            user=user,
            full_name=student["full_name"],
            level=level,
            year_of_addmission = '2023'
        )
        profiles.append(profile)

    # Bulk create profiles
    StudentProfile.objects.bulk_create(profiles)

    print("Users and profiles created successfully.")


    return render(request, 'data/bulk.html')

def students(request):
    students = StudentProfile.objects.all()
    context = {
        'students':students,
    }
    return render(request, 'data/students.html', context)

def staffs(request):
    staffs = TeacherProfile.objects.all()
    context = {
        'staffs':staffs,
    }
    return render(request, 'data/staffs.html', context)

def subjects(request):
    subjects = StudentProfile.objects.all()
    context = {
        'subjects':subjects,
    }
    return render(request, 'data/subjects.html', context)

def levels(request):
    levels = Level.objects.all()
    context = {
        'levels':levels,
    }
    return render(request, 'data/classes.html', context)


def admin_dashboard(request):
    return render(request, 'dashboards/admin_dashboard.html')

def teacher_dashboard(request):
    return render(request, 'dashboards/teacher_dashboard.html')

def form_master_dashboard(request):
    return render(request, 'dashboards/form_master_dashboard.html')

def student_dashboard(request):
    student = request.user.profile
    context = {
        'student':student,
    }
    return render(request, 'dashboards/student_dashboard.html', context)

def Login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username =username, password = password)
        if user is not None and user.is_active:
            login(request,user)
            if request.user.is_support:
                return redirect('profiles:admin-dashboard')
            
            if request.user.is_teacher:
                return redirect('profiles:teacher-dashboard')
            
            if request.user.is_student:
                # return redirect('profiles:student-dashboard')
                return redirect('profiles:student-dashboard')
        else:
            return redirect('profiles:signup')
    else:
        return render(request, 'accounts/login.html')
    

def Logout(request):
    logout(request)
    return redirect('profiles:login')

def signup(request):
    level = Level.objects.get(id = 1)
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            my_user = form.save(commit = False)
            my_user.is_student = True
            my_user.save()
            StudentProfile.objects.create(user = my_user, year_of_admission='2023',level=level)
            login(request,my_user)
            return redirect('profiles:update-student')
        else:
            return redirect('profiles:signup')
    else:
        form = RegisterationForm()
        context = {
            'form':form,
        }

    return render(request, 'accounts/signup.html', context)

def update_student(request):
    stdnt = StudentProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = StudentProfileForm(request.POST, instance=stdnt)
        if form.is_valid():
            student = form.save()
            messages.success(request, f'student {student.full_name} successifully updated')
            return redirect('profiles:student-dashboard')
    else:
        form = StudentProfileForm(instance=stdnt)

    context = {
        'form':form,
    }
    return render(request, 'accounts/profile.html', context)

def staff_signup(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            my_user = form.save(commit = False)
            my_user.is_teacher = True
            my_user.save()
            TeacherProfile.objects.create(user = my_user)
            login(request,my_user)
            return redirect('profiles:update-staff')
        else:
            return redirect('profiles:staff-signup')
    else:
        form = RegisterationForm()
        context = {
            'form':form,
        }

    return render(request, 'accounts/staff_signup.html', context)

def update_staff(request):
    staff = TeacherProfile.objects.get(user = request.user)
    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, instance=staff)
        if form.is_valid():
            teacher = form.save()
            messages.success(request, f'student {teacher.full_name} successifully updated')
            return redirect('profiles:teacher-dashboard')
    else:
        form = TeacherProfileForm(instance=staff)

    context = {
        'form':form,
    }
    return render(request, 'accounts/profile.html', context)

def form_master_signup(request):
    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            my_user = form.save(commit = False)
            my_user.is_form_master = True
            my_user.save()
            FormMasterProfile.objects.create(user = my_user)
            login(request,my_user)
            return redirect('profiles:update-form-master')
        else:
            return redirect('profiles:form-master-signup')
    else:
        form = RegisterationForm()
        context = {
            'form':form,
        }

    return render(request, 'accounts/staff_signup.html', context)

# def update_form_master(request):
#     form_master = FormMasterProfile.objects.get(user = request.user)
#     if request.method == 'POST':
#         form = TeacherProfileForm(request.POST, instance=form_master)
#         if form.is_valid():
#             fmaster = form.save()
#             messages.success(request, f'student {fmaster.full_name} successifully updated')
#             return redirect('profiles:form-master-dashboard')
#     else:
#         form = FormMasterProfile(instance=fmaster)

#     context = {
#         'form':form,
#     }
#     return render(request, 'accounts/profile.html', context)

def update_form_master(request):
    # Fetch the FormMasterProfile associated with the current user
    form_master = FormMasterProfile.objects.get(user=request.user)

    if request.method == 'POST':
        # Bind the form with POST data and the existing instance of form_master
        form = FormMasterProfileForm(request.POST, instance=form_master)
        
        if form.is_valid():
            # Save the updated form data and store it in fmaster
            fmaster = form.save()
            messages.success(request, f'student {fmaster.full_name} successfully updated')
            return redirect('profiles:form-master-dashboard')  # Redirect after success
    else:
        # Initialize the form with the existing data from form_master
        form = FormMasterProfileForm(instance=form_master)

    context = {
        'form': form,
    }
    return render(request, 'accounts/profile.html', context)

def profiles(request):
    level = Level.objects.get(id = 1)
    my_students = StudentProfile.objects.filter(level = level)
    context = {
        'my_students':my_students
    }
    return render(request, 'student_profiles.html', context)
