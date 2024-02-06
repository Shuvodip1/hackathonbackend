from django.db import models

# Create your models here.


class Bed(models.Model):
    bed_no = models.IntegerField(default=0)


class Appointment(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    doctor = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_book = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
