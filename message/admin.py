from django.contrib import admin

# Register your models here.
from .models import *
# Register your models here.
class MessageAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку

   list_display = ['name','email','phone','message']



class Meta:
    model = Message
# Register your models here.
admin.site.register(Message,MessageAdmin)
