from django.db import models

# Create your models here.

class Project(models.Model):
    name = models.CharField(max_length=200)


class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

    #Hacemos la relacion con la otra tabla
    #Cascade significa que cuando se elimine un dato
    #el resto se elimina en cascada
    project = models.ForeignKey(Project,on_delete=models.CASCADE)