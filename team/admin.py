from django.contrib import admin
from .models import *

class TeamAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку

   list_display = ['name','image_img']
   readonly_fields = ['image_img',]


class Meta:
    model = Team
# Register your models here.
admin.site.register(Team,TeamAdmin)

