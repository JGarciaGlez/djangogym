from django.db import models

# Create your models here.


class Todo(models.Model):
    title =  models.CharField(max_length=200)
    series=models.CharField(max_length=500)
    weights=models.CharField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)