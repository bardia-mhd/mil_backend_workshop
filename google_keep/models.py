from django.db import models


# Create your models here.

class KeepUser(models.Model):
    first_name = models.CharField(max_length=100, blank=True, null=True)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name


class Checkbox(models.Model):
    done = models.BooleanField(default=False)
    todo = models.CharField(max_length=100)


class Note(models.Model):
    title = models.CharField(max_length=100)
    note = models.TextField(max_length=1000, blank=True, null=True)
    deleted = models.BooleanField(default=False)
    archived = models.BooleanField(default=False)
    user = models.ForeignKey(KeepUser, on_delete=models.CASCADE, related_name='notes')
    todos = models.ManyToManyField(Checkbox, related_name='todos', null=True, blank=True)
