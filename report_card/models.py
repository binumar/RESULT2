from django.db import models
import secrets
import random
from django.core.exceptions import ValidationError
from django.db.models.signals import post_save
from profiles.models import Level,Session,Term,StudentProfile, AcademicCalender
from profiles.models import Subject
    
class SubjectEntry(models.Model):
    session = models.ForeignKey(Session, on_delete = models.CASCADE)
    term = models.ForeignKey(Term, on_delete = models.CASCADE) 
    student = models.ForeignKey(StudentProfile, on_delete = models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete = models.CASCADE)
    level = models.ForeignKey(Level,blank=True, null=True, on_delete=models.CASCADE)
    ca1 = models.IntegerField()
    ca2 = models.IntegerField()
    exam = models.IntegerField()
    generated = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.student.full_name}- {self.student.level} - {self.subject.name} - {self.total}'

    class Meta:
        unique_together = ['student','subject','level']

    
    @property
    def total(self):
        return self.ca1 + self.ca2 + self.exam
    
    @property
    def grade(self):
        grade = ''
        if self.total <=39:
            grade ='F'
        elif self.total >= 40 and self.total <=49:
            grade = 'D'
        elif self.total >= 50 and self.total <=59:
            grade = 'C'
        elif self.total >= 60 and self.total <=69:
            grade = 'B'
        elif self.total >= 70 and self.total <=79:
            grade = 'A'
        elif self.total >= 71 and self.total <=100:
            grade = 'A+'
        return grade
    
    def subject_registeration(sender, instance,created,**kwargs):
        calender = AcademicCalender.objects.get(is_active = True)
        session = calender.session
        term= calender.term
        next_term = calender.next_term_begins
        subjects = Subject.objects.all()
        if created:
            srepo, created = Report.objects.get_or_create(session = session, term = term, next_term_begin = next_term,student = instance, level = instance.level)
            for subject in subjects:
                sub_entry = SubjectEntry.objects.create(session=session, term = term, student = instance, level = instance.level, subject = subject,ca1 =0,ca2 =0, exam =0 )
                repo_filter = Report.objects.filter(student = instance, term =term,session = session,is_approved = False).first()
                if repo_filter:
                    repo_filter.subjects.add(sub_entry)
                    repo_filter.save()

    post_save.connect(subject_registeration,sender =StudentProfile)
        
    
class Report(models.Model): 
    session = models.ForeignKey(Session, related_name='session_reports', on_delete = models.CASCADE)
    term = models.ForeignKey(Term, related_name='term_reports', on_delete = models.CASCADE)
    student = models.ForeignKey(StudentProfile, related_name='student_reports', on_delete = models.CASCADE)
    subjects = models.ManyToManyField(SubjectEntry, related_name = 'subjects')
    level = models.ForeignKey(Level, related_name='level_results', on_delete=models.CASCADE)
    is_approved = models.BooleanField(default = False)
    date_created = models.DateTimeField(auto_now_add = True)
    overall_total = models.IntegerField(blank = True,null=True)
    next_term_begin = models.CharField(max_length=255,blank=True, null=True)
    position = models.IntegerField(blank = True, null =True)
    out_of = models.CharField(max_length=255,blank = True,null=True)
    closes_on = models.CharField(max_length=255,blank = True,null=True)
    pin = models.CharField(max_length=255,blank = True,null=True)

    class Meta:
        unique_together = ('session', 'term', 'student', 'level')

    def __str__(self):
        return f'{self.student.full_name}'
    

    def generate_pin(self):
        """Generate a random 11-digit PIN."""
        pin = str(secrets.randbelow(10**11)).zfill(11)  # Ensure it is always 11 digits
        return pin

    def save(self, *args, **kwargs):
        if not self.pin:
            self.pin = self.generate_pin()  # Automatically generate a PIN if not provided
            # Ensure the PIN is unique before saving
            while Pin.objects.filter(pin=self.pin).exists():
                self.pin = self.generate_pin()  # Regenerate PIN if it's not unique
        super().save(*args, **kwargs)
    
    def get_total(self):
        total = 0
        for score in self.subjects.all():
            total += score.total
        return total



# class Pin(models.Model):
#     pin = models.CharField(max_length=10, unique=True, blank=True)  # Store the PIN itself
#     date_created = models.DateTimeField(auto_now_add=True)  # When the PIN was created
#     is_used = models.BooleanField(default=False)  # Tracks if the PIN has been used or not

#     def __str__(self):
#         return f"PIN {self.pin}"

#     def generate_pin(self):
#         """Generate a random 6-digit PIN."""
#         pin = str(random.randint(100000, 999999))  # Generate a 6-digit number
#         return pin

#     def save(self, *args, **kwargs):
#         if not self.pin:
#             self.pin = self.generate_pin()  # Automatically generate a PIN if not provided
#         super().save(*args, **kwargs)

#     def check_pin(self, entered_pin):
#         """Check if the entered PIN matches the stored one."""
#         return self.pin == entered_pin


class Pin(models.Model):
    pin = models.CharField(max_length=11, unique=True, blank=True)  # 11-digit PIN
    date_created = models.DateTimeField(auto_now_add=True)  # When the PIN was created
    is_used = models.BooleanField(default=False)  # Tracks if the PIN has been used or not

    def __str__(self):
        return f"{self.pin}"

    def generate_pin(self):
        """Generate a random 11-digit PIN."""
        pin = str(secrets.randbelow(10**11)).zfill(11)  # Ensure it is always 11 digits
        return pin

    def save(self, *args, **kwargs):
        if not self.pin:
            self.pin = self.generate_pin()  # Automatically generate a PIN if not provided
            # Ensure the PIN is unique before saving
            while Pin.objects.filter(pin=self.pin).exists():
                self.pin = self.generate_pin()  # Regenerate PIN if it's not unique
        super().save(*args, **kwargs)

    def check_pin(self, entered_pin):
        """Check if the entered PIN matches the stored one."""
        return self.pin == entered_pin


