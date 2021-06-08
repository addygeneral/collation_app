from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(max_length=50)
    date_of_employment = models.DateField(max_length=50)
    position = models.ForeignKey(Position,on_delete=models.CASCADE)
    salary = models.CharField(max_length=50)
    supervisor = models.CharField(max_length=100)
class Meta:
    db_table='Employee'