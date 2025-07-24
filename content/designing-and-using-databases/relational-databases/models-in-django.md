---
title: Models in Django
---

```SQL
from django.db import models
class Student(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(unique=True)
class Course(models.Model):
	name = models.CharField(max_length=100)
	instructor = models.CharField(max_length=100)
class Enrollment(models.Model):
	student = models.ForeignKey(Student, on_delete=models.CASCADE)
	course = models.ForeignKey(Course, on_delete=models.CASCADE)
``` 

[Data Structures in Databases](/designing-and-using-databases/introduction/data-structures-in-databases)