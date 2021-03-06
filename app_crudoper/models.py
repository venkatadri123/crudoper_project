from django.db import models


class Student(models.Model):
    Image = models.ImageField(upload_to='images', blank=True, null=True)
    Student_ID = models.IntegerField()
    Username = models.CharField(max_length=100)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Approvel = models.BooleanField(verbose_name="Approved", default=False)
    School = models.CharField(max_length=100)
    Program = models.CharField(max_length=100)
    Batch = models.IntegerField()
    password = models.CharField(max_length=50)
