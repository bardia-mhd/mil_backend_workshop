from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views.generic import FormView

from .models import KeepUser, Note, Checkbox
from django.core import serializers
import json

# Create your views here.

def create_note(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('index'))
    if request.method == "POST":
        data = json.loads(request.body)
        note = Note.objects.create(title=data["title"], note=data["note"], user=request.user)
        for i in data["tasks"]:
            task = Checkbox(todo=i)
            task.save()
            note.todos.add(task)
            note.save()
        return JsonResponse(
            {"message": "Success", "tasks": serializers.serialize('json', note.todos.all()), "pk": note.pk})

