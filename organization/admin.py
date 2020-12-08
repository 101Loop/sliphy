from django.contrib import admin

from organization.models import Company
from organization.models import Employee
from organization.models import SalarySlip


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    pass


@admin.register(SalarySlip)
class SalarySlipAdmin(admin.ModelAdmin):
    pass
