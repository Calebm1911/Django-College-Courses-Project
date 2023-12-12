from django.db import models

# Create your models here.

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_title = models.CharField(max_length=30)
    course_description = models.CharField(max_length=60)
    course_credits = models.IntegerField()
    course_instructor = models.CharField(max_length = 30)
    couse_start_date = models.DateField()

    def __str__(self):
        return self.course_title