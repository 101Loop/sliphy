from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import CreateView
from django.views.generic import DetailView
from django.views.generic import ListView

from organization.forms import CompanyForm
from organization.models import Company


class CompanyCreateView(LoginRequiredMixin, CreateView):
    model = Company
    form_class = CompanyForm
    template_name = "organization/create_company.html"

    def get_success_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})

    def form_valid(self, form):
        form.instance.user = self.request.user
        messages.add_message(
            self.request, messages.INFO, _("Company Created Successfully.")
        )
        return super().form_valid(form)


create_company_view = CompanyCreateView.as_view()


class CompanyListView(LoginRequiredMixin, ListView):
    model = Company
    context_object_name = "companies"
    template_name = "organization/list_company.html"

    def get_queryset(self):
        return self.model.objects.filter(user=self.request.user)


list_company_view = CompanyListView.as_view()


class CompanyDetailView(LoginRequiredMixin, DetailView):
    model = Company
    template_name = "organization/detail_company.html"
    context_object_name = "company"


detail_company_view = CompanyDetailView.as_view()
