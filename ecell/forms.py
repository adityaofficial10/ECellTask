from django import forms
from .models import InternshipRole,Student,InternshipAnswer,InternshipQuestion

class InternshipRoleForm(forms.ModelForm):
    class Meta:
        model = InternshipRole
        fields=('startup_name','role','poc_name','poc_email','profile_doc','incentives','incentives','duration','website',)

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields=('first_name','middle_name','last_name','age','rollno','student_email','dept','resume','roles',)

class InternshipAnswerForm(forms.ModelForm):
    class Meta:
        model = InternshipAnswer
        fields=('internship_question','applicant_answer',)
        exclude = ['applicant']

class InternshipQuestionForm(forms.ModelForm):
    class Meta:
        model = InternshipQuestion
        fields=('internship','question',)
