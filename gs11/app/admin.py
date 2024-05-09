from django.contrib import admin
from .models import Group,Chat
# Register your models here.

@admin.register(Group)
class Mygroup(admin.ModelAdmin):
    list_display = [field.name for field in Group._meta.fields]

@admin.register(Chat)
class AdminChat(admin.ModelAdmin):
    list_display = [field.name for field in Chat._meta.fields]