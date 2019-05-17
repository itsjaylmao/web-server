from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=255)
    decription = models.TextField()
    backend_used = models.CharField(max_length=48)
    database_used = models.CharField(max_length=48)

    def __str__(self):
        return self.title