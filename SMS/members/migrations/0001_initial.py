# Generated by Django 4.1.4 on 2022-12-24 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('first_name', models.CharField(blank=True, max_length=120)),
                ('last_name', models.CharField(blank=True, max_length=120)),
                ('gender', models.CharField(blank=True, choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('member_id', models.IntegerField(blank=True)),
                ('national_id', models.IntegerField(blank=True, unique=True)),
                ('email', models.EmailField(blank=True, max_length=70, unique=True)),
                ('phone', models.CharField(max_length=13)),
                ('address', models.CharField(blank=True, max_length=250)),
                ('date_of_birth', models.DateField()),
                ('next_of_kin', models.CharField(max_length=250)),
                ('contributions', models.IntegerField()),
                ('occupation', models.CharField(choices=[('FARMER', 'Farmer'), ('BUSINESS', 'Business'), ('TEACHER', 'Teacher'), ('ENGINEER', 'Engineer'), ('DOCTOR', 'Doctor'), ('ACCOUNTANT', 'Accountant'), ('OTHER', 'Other')], max_length=60)),
                ('profile_picture', models.ImageField(upload_to='photos/%Y/%m/%d')),
                ('date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
