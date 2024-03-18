from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length = 10)
    age = models.IntegerField()

    def __str__(self):
        return self.name + ' ' + str(self.age)
    
class Logger(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField( help_text="Enter correct field")
    time = models.TimeField()

class Reservations(models.Model):
    name = models.CharField(max_length= 100)
    count = models.IntegerField()
    time = models.TimeField()

    def __str__(self) -> str:
        return self.name + ' with ' + str(self.count)