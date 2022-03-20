from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth import password_validation

from reviews.models.reviewer import Reviewer
from django import forms


class ReviewerForm(UserCreationForm):
    GENDER_CHOICES = [
        ('----', '----'),
        ('M', _('M')),
        ('T', _('T')),
        ('F', _('F')),
    ]
    email = forms.EmailField(label=_('Email'),
                             widget=forms.EmailInput(attrs={
                                 'placeholder': _('Enter your email')
                             }))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': _('Enter your password')}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': _('Enter the password again')}),
        help_text=password_validation.password_validators_help_text_html(),
    )

    name = forms.CharField(label=_('Name'),
                           widget=forms.TextInput(attrs={'class': 'form-control form-control-sm input_register',
                                                         'placeholder': _('Enter your name')}))
    lastname = forms.CharField(label=_('Last Name'),
                               widget=forms.TextInput(attrs={'placeholder': _('Enter your last name'),
                                                             'class': 'form-control form-control-sm input_register'}))

    phone = forms.IntegerField(label=_("Phone number"), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Enter your phone number'), 'class': 'form-control form-control-sm input_register'}))

    description = forms.CharField(label=_("Description"), widget=forms.Textarea(
        attrs={"rows": 5, "cols": 20, 'class': 'form-control form-control-sm input_register'}))

    age = forms.IntegerField(label=_("Age"), widget=forms.NumberInput(attrs={
        'class': 'form-control form-control-sm input_register', }), max_length=100)

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control form-control-sm input_register', }), label=_("Gender"))

    class Meta:
        model = Reviewer

        fields = [
            'name',
            'lastname',
            'age',
            'gender',
            'phone',
            'photo',
            'description',
            'password1',
            'password2'
        ]
