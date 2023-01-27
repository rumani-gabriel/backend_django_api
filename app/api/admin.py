from django.contrib import admin
from .models import Service


# Register your models here.
# admin.site.register(Service)

@admin.register(Service)
class ServiceModel(admin.ModelAdmin):
    list_filter = ('title','description')
    list_display = ('title', 'description')