from django.db import models

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=110)
    address = models.TextField()
    phone = models.BigIntegerField()


    def __str__(self):
        return self.name