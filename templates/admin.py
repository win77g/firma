from django.contrib import admin
from .models import *

class TemplateAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку

   list_display = ['name','category','image_img']
   readonly_fields = ['image_img',]


class Meta:
    model = Template
# Register your models here.
admin.site.register(Template,TemplateAdmin)

class CategoryTemplateAdmin (admin.ModelAdmin):
   #  вывод всех полей в админку
   list_display = ['name']

class Meta:
    model = CategoryTemplate
# Register your models here.
admin.site.register(CategoryTemplate,CategoryTemplateAdmin)
# Register your models here.
