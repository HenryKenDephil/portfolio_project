from django.db import models
#from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete



# Create your models here.
class Members(models.Model):
    gender_choices = (
        ('M', 'Male'),
        ('F', 'Female'),    
    )
    occupation_choices = (
        ('FARMER', 'Farmer'),
        ('BUSINESS', 'Business'),
        ('TEACHER', 'Teacher'),
        ('ENGINEER', 'Engineer'),
        ('DOCTOR', 'Doctor'),
        ('ACCOUNTANT', 'Accountant'),
        ('OTHER', 'Other'),
    )
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=120, blank=True)
    last_name = models.CharField(max_length=120, blank=True)
    gender = models.CharField(max_length=1, choices=gender_choices, blank=True)
    member_id = models.IntegerField(blank=True)
    national_id = models.IntegerField(unique=True, blank=True)
    email = models.EmailField(max_length=70, blank=True, unique=True)
    phone = models.CharField(max_length=13, blank=False)
    address = models.CharField(max_length=250, blank=True)
    date_of_birth = models.DateField()
    next_of_kin = models.CharField(max_length=250, blank=False)
    contributions = models.IntegerField()
    occupation = models.CharField(max_length=60, choices=occupation_choices)
    profile_picture = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True)
    date = models.DateTimeField(auto_now_add=True)

    
    class Meta:
        verbose_name = 'Member Name'
        verbose_name_plural = 'Members Names'

    def __str__(self):
        return self.first_name + ' ' + self.last_name + ' ' + self.email + '___ ' + self.gender

    def get_absolute_url(self):
        return reverse('member_details', kwargs={'pk': self.pk})

