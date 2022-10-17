from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=40, unique=True)

    def __str__(self):
        return f"{self.name}"


class Employee(models.Model):
    name = models.CharField(max_length=40)
    email = models.EmailField(unique=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"{self.name}"
