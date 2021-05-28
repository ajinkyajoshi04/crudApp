from django.db import models


# Create your models here.

class StudentData(models.Model):
    student_id = models.CharField(max_length=100)
    student_first_name = models.CharField(max_length=100)
    student_last_name = models.CharField(max_length=100)
    student_email = models.EmailField(max_length=100)
    student_address = models.CharField(max_length=100)
    student_phone = models.CharField(max_length=10)
    class Meta:
        db_table = "student_data"