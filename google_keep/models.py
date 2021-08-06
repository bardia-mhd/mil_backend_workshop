from django.db import models


# Create your models here.

class KeepUser(models.Model):
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)


class Checkbox(models.Model):
    done = models.BooleanField(default=False)
    todo = models.CharField(max_length=100)


class Note(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    note = models.CharField(max_length=1000, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    user = models.ForeignKey(KeepUser, on_delete=models.CASCADE, related_name='users')
    # todos = models.ManyToManyField(Checkbox, related_name='todos', null=True)
