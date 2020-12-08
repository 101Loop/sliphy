from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    """Default user for Sliphy."""

    #: First and last name do not cover name patterns around the globe
    name = models.CharField(_("Full Name"), blank=True, max_length=255)
    mobile = models.CharField(
        _("Mobile Number"),
        validators=[RegexValidator(regex=r"^[0][1-9]\d{9}$|^[6-9]\d{9}$")],
        max_length=150,
        unique=True,
        null=True,
        error_messages={
            "unique": _("A user with that mobile already exists."),
        },
    )
    update_date = models.DateTimeField(_("Date Modified"), auto_now=True)
    profile_image = models.ImageField(
        verbose_name=_("Profile Photo"), upload_to="user_images", null=True, blank=True
    )

    def get_absolute_url(self):
        """Get url for user's detail view.
        Returns:
            str: URL for user detail.
        """
        return reverse("users:detail", kwargs={"username": self.username})
