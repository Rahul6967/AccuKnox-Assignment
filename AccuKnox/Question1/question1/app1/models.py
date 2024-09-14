from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=100)
    status = models.CharField(max_length=100, default="Active")

    def __str__(self):
        return self.name
    