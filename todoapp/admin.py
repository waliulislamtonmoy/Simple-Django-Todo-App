from django.contrib import admin


from .models import Todo
# Register your models here.

class todoAdmin(admin.ModelAdmin):
    list_display=['id','text','date']
    
admin.site.register(Todo,todoAdmin)