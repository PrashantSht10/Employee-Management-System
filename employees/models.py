from django.db import models

# Creating my models here.
class Employee(models.Model):
    eid = models.AutoField(primary_key=True)
    ename = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    phone_no = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    address = models.TextField()

    def __str__(self):
        return self.ename

