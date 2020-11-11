from django.db import models

# Create your models here.

class InternshipRole(models.Model):
    """Model for storing the information of Startup"""
    startup_name = models.CharField(max_length = 100)
    role = models.CharField(max_length=100)
    poc_name = models.CharField(max_length = 100)
    poc_email = models.EmailField(max_length = 100)
    profile_doc = models.FileField(blank = True,null = True)
    incentives = models.CharField(max_length = 500)
    duration = models.CharField(max_length = 20)
    website = models.CharField(max_length = 100,blank = True)

    def __str__(self):
        return (self.startup_name + ' , ' + self.role)


class Student(models.Model):
    """Model for storing student records"""
    first_name = models.CharField(max_length = 100)
    middle_name = models.CharField(max_length = 100)
    last_name = models.CharField(max_length = 100)
    age = models.IntegerField()
    rollno = models.CharField(max_length = 20)
    student_email = models.EmailField(max_length = 100)
    dept = models.CharField(max_length = 50)
    resume = models.FileField()
    roles = models.ForeignKey(InternshipRole,on_delete=models.CASCADE,null = True)

    class Meta:
        unique_together = ('rollno','roles',)

    def __str__(self):
        return self.first_name

class InternshipQuestion(models.Model):
    internship = models.ForeignKey(InternshipRole, on_delete=models.CASCADE)
    question = models.CharField(max_length = 200)

    def __str__(self):
        return self.question

class InternshipAnswer(models.Model):
    internship_question = models.ForeignKey(InternshipQuestion,on_delete=models.CASCADE)
    applicant = models.ForeignKey(Student, on_delete=models.CASCADE)
    applicant_answer = models.CharField(max_length = 500)

    class Meta:
        unique_together = ('applicant','internship_question','applicant_answer')

    def __str__(self):
        return self.applicant_answer

class InternshipApplication(models.Model):
    applicant = models.ForeignKey(Student, on_delete=models.CASCADE)
    internship = models.ForeignKey(InternshipRole, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('applicant', 'internship',)

    def __str__(self):
        return self.applicant.first_name

    @classmethod
    def create(cls, applicant,internship):
        application = cls(applicant = applicant,internship = internship)
        # do something with the book
        return application
