from django.db import models
from django.contrib.auth.models import User


class ToDoList(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='todolist', null=True)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name  # daca vrei sa arate numele in loc de object1


class Item(models.Model):
    todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
