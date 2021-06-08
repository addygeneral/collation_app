from django.contrib import admin
from .models import Employee
from import_export.admin import ImportExportModelAdmin

@admin.register(Employee)
class userdat(ImportExportModelAdmin):
    pass

