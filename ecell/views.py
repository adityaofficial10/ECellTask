from django.shortcuts import render,redirect
from django.forms import modelformset_factory
# Create your views here.

from ecell.models import InternshipRole,Student,InternshipQuestion,InternshipAnswer,InternshipApplication
from .forms import InternshipRoleForm, StudentForm,InternshipAnswerForm,InternshipQuestionForm
from django.http import HttpResponseRedirect

def index(request):

    num_startups = InternshipRole.objects.all().count()
    num_students = Student.objects.all().count()


    context = {
       'num_startups':num_startups,
       'num_students':num_students,
    }

    return render(request,'index.html',context = context)

def current(request):

    num_startups = InternshipRole.objects.all().count()
    applied = InternshipRole.objects.all()
    roles = []
    for vac in applied:
        roles.append(vac.role+' , '+ vac.startup_name)
    context = {
      'num_startups':num_startups,
      'applied':applied,
      'roles':roles,
    }
    return render(request,'current.html',context = context)

def readytoanswer(request):

    dummy = "dummy"
    context = {'dummy':dummy,}

    return render(request,'readytoanswer.html',context = context)

def thanks(request):

    dummy = "dummy"
    context = { 'dummy':dummy,}

    return render(request,'thanks.html',context = context)

def question(request,pk,roll):

    role = InternshipRole.objects.all().filter(pk=pk)
    questions = InternshipQuestion.objects.all().filter(internship=role[0])
    cnt = questions.count()
    applicant = Student.objects.all().filter(rollno = roll)
    question_set = modelformset_factory(InternshipAnswer, fields=('internship_question','applicant_answer',),extra = cnt)
    formset = question_set(queryset = InternshipAnswer.objects.none())
    if request.method == 'POST':
        formset = question_set(request.POST,request.FILES)
        print(request.POST)
        if formset.is_valid():
          for form in formset:
              record = form.save(commit = False)
              record.applicant = applicant[0]
              record.save()
          return redirect(index)

    else:
        formset = question_set(queryset = InternshipAnswer.objects.none())

    context = {
      'questions':questions,
      'formset':formset,
      'cnt':cnt,
    }

    return render(request,'question.html',context = context)

def student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST,request.FILES)
        if form.is_valid():
            applicant = form.save()
            role_obj = form.cleaned_data.get('roles')
            rollno = form.cleaned_data.get('rollno')
            application = InternshipApplication.create(applicant = applicant,internship = role_obj)
            application.save()
            context = {
                'role_obj':role_obj,
                'rollno':rollno,
            }
            return render(request,'readytoanswer.html',context = context)

    else:
        form = StudentForm()
    num_students = Student.objects.all().count()

    context = {
      'num_students':num_students,
      'form':form
    }
    return render(request,'student.html',context = context)


def more(request):

    return redirect(addQuestion)

def addQuestion(request):

    if request.method == 'POST':
        form = InternshipQuestionForm(request.POST)
        if form.is_valid():
            form.save()
            context = {}
            return render(request,"more.html",context)

    else:
        form = InternshipQuestionForm()

    context = {
       'form':form,
    }
    return render(request,'addQuestion.html',context = context)


def startup(request):

    if request.method == 'POST':

        form = InternshipRoleForm(request.POST,request.FILES)
        if form.is_valid():
            role_obj=form.save(commit = False)
            role_obj.save()
            context = {
              'role_obj':role_obj,
            }
            return redirect(addQuestion)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = InternshipRoleForm()

    context = {
      'form':form,
    }
    return render(request,'startup.html',context = context)


def internshiprole_detail(request,pk):

    try:
        Role = InternshipRole.objects.get(pk=pk)
        students = Student.objects.filter(roles=Role)
        description = Role.role + ' , '+ Role.startup_name
        cnt = Student.objects.filter(roles = Role).count()
        context = {
           'role':Role,
           'students':students,
           'description':description,
           'cnt':cnt,
        }
    except InternshipRole.DoesNotExist:
        raise Http404('The internship role you are looking for, does not exist')

    return render(request,'role_detail.html',context = context)
