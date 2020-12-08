from django.urls import path

from . import views

app_name = "organization"
urlpatterns = [
    path("create/", views.create_company_view, name="create-company"),
    path("list/", views.list_company_view, name="list-company"),
    path("<int:pk>/", views.detail_company_view, name="detail-company"),
]
