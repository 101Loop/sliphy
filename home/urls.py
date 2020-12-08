from django.urls import path

from .views import home_page_view

app_name = "home"
urlpatterns = [
    path("", view=home_page_view, name="home_page"),
]
