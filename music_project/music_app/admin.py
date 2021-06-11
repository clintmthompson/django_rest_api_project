from django.contrib import admin
from .models import Song
from .serializers import serializers
# Register your models here.

admin.site.register(Song)

