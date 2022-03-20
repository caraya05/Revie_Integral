from django import forms
from django.utils.translation import ugettext_lazy as _
from users.models.person import Person


class LoginModelForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(
        attrs={
            'class': 'form-control',
            'placeholder': _("Enter your email")}
    ), label=_("Email"))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': _("Enter your password"),
        }
    ), label=_("Password"))

    class Meta:
        model = Person
        fields = [
            'email', "password"
        ]
