# Generated by Django 2.1.5 on 2020-11-09 07:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ecell', '0002_auto_20201109_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='startup',
            name='companies',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='ecell.Student'),
        ),
    ]
