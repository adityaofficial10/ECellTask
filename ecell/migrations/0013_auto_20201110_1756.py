# Generated by Django 2.1.5 on 2020-11-10 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecell', '0012_auto_20201110_0831'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='internshipanswer',
            unique_together={('applicant', 'internship_question', 'applicant_answer')},
        ),
    ]
