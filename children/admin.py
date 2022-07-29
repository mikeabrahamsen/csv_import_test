from django.contrib import admin

# Register your models here.

from .models import children


@admin.register(children)
class childrenAdmin(admin.ModelAdmin):
    list_display = ["name", "sex", "age"]
