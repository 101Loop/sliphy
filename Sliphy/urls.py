"""Sliphy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include
from django.urls import path

urlpatterns = [
    # Django Admin
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path("users/", include("users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    # Home
    path("", include("home.urls", namespace="home")),
    # Org
    path("org/", include("organization.urls", namespace="organization")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
