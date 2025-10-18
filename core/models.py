import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

date = timezone.now()

class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'

class Clinic(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Doctor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.IntegerField()
    speciality = models.CharField(max_length=100)
    available = models.BooleanField()

    def __str__(self):
        return self.full_name


class Receptionist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name

class Patient(models.Model):
    full_name = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    birth_date = models.DateField()
    gender = models.CharField(choices=Gender.choices, max_length=6)

    @property
    def age(self):
        return date.year - self.birth_date.year - ((date.month, date.day) < (self.birth_date.month, self.birth_date.day))

    def __str__(self):
        return self.full_name