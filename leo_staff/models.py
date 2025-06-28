from django.db import models

# Base Staff model
class Staff(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20)

    class Meta:
        abstract = True

    def __str__(self):
        return self.full_name

# Manager model inherits from Staff
class Manager(Staff):
    department = models.CharField(max_length=100)
    office_number = models.CharField(max_length=10)

# Intern model inherits from Staff
class Intern(Staff):
    school = models.CharField(max_length=100)
    duration_months = models.PositiveIntegerField()

