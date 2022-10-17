from django.contrib import admin
from django.contrib.admin import AdminSite

from app.models import Department, Employee


class EmployeeAdmin(admin.ModelAdmin):
    pass


class DepartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Department, DepartmentAdmin)
