from django import forms

from organization.models import Company


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = [
            "company_name",
            "company_mobile",
            "company_website_url",
            "company_address",
            "company_logo",
        ]
