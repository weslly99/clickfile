from django.contrib import admin
from .models import File, Directory

@admin.register(File)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name','size','mime_type','directory')
    fields = ('content','directory')

@admin.register(Directory)
class FileAdmin(admin.ModelAdmin):
    list_display = ('name','size','path','children_quantity')
    fields = ('name','parent')
    ordering: ('updated_at')