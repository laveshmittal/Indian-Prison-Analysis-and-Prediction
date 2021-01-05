from django.contrib import admin

# Register your models here.
from .models import *
from import_export.admin import ImportExportActionModelAdmin

@admin.register(agegroup)
@admin.register(education)
@admin.register(escapes)
@admin.register(periodofsentence)
class ViewAdmin(ImportExportActionModelAdmin):
    pass

