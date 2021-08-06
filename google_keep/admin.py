from django.contrib import admin

# Register your models here.
from google_keep.models import Note, KeepUser

admin.site.register(Note)
admin.site.register(KeepUser)