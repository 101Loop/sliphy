from allauth.account.forms import LoginForm
from django import forms
from django.contrib.auth import forms as admin_forms
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

User = get_user_model()


class UserChangeForm(admin_forms.UserChangeForm):
    class Meta(admin_forms.UserChangeForm.Meta):
        model = User


class UserCreationForm(admin_forms.UserCreationForm):
    error_message = admin_forms.UserCreationForm.error_messages.update(
        {"duplicate_username": _("This username has already been taken.")}
    )

    class Meta(admin_forms.UserCreationForm.Meta):
        model = User

    def clean_username(self):
        username = self.cleaned_data["username"]

        try:
            User.objects.get(username=username)
        except User.DoesNotExist:
            return username

        raise ValidationError(self.error_messages["duplicate_username"])


class CustomLoginForm(LoginForm):
    def __init__(self, *args, **kwargs):
        super(CustomLoginForm, self).__init__(*args, **kwargs)
        self.fields["login"] = forms.CharField(
            label="Username/Email",
            widget=forms.TextInput(
                attrs={"placeholder": _("Username or E-mail"), "autocomplete": "email"}
            ),
        )


# class CustomSignupForm(SignupForm):
#     mobile = forms.CharField(
#         label=_("Mobile"),
#         widget=forms.TextInput(
#             attrs={"placeholder": _("Mobile"), "autocomplete": "mobile"}
#         ),
#     )
