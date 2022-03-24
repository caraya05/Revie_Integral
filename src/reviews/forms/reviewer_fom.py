from django.contrib.auth import password_validation
from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import ugettext_lazy as _

from django import forms

from users.models import Person


class ReviewerForm(UserCreationForm):
    GENDER_CHOICES = [
        ('----', '----'),
        ('M', _('M')),
        ('T', _('T')),
        ('F', _('F')),
    ]
    photo = forms.ImageField(widget=forms.FileInput(attrs={'class': 'form-control form-control-sm',
                                                           'accept': 'image/jpg, image/jpeg, image/png'}))
    password1 = forms.CharField(
        label=_("Password"),
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'placeholder': _('Enter your password'),
                                          'class': 'form-control form-control-sm input_register'}),
        help_text=password_validation.password_validators_help_text_html(),
    )
    password2 = forms.CharField(
        label=_("Password confirmation"),
        strip=False,
        widget=forms.PasswordInput(
            attrs={'autocomplete': 'new-password', 'placeholder': _('Enter the password again'),
                   'class': 'form-control form-control-sm input_register'}),
        help_text=password_validation.password_validators_help_text_html(), )

    first_name = forms.CharField(label=_('Name'),
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control form-control-sm input_register',
                                     'placeholder': _('Enter your name')}))
    last_name = forms.CharField(label=_('Last Name'),
                                widget=forms.TextInput(attrs={'placeholder': _('Enter your last name'),
                                                              'class': 'form-control form-control-sm input_register'}))

    email = forms.EmailField(label=_('Email'),
                             widget=forms.EmailInput(attrs={
                                 'class': 'form-control form-control-sm input_register',
                                 'placeholder': _('Enter your email')
                             }

                             ))
    phone = forms.IntegerField(label=_("Phone number"), required=False, widget=forms.TextInput(
        attrs={'placeholder': _('Enter your phone number'), 'class': 'form-control form-control-sm input_register'}))

    description = forms.CharField(label=_("Description"), widget=forms.Textarea(
        attrs={'placeholder': _('Enter your description'), 'rows': 5, 'cols': 20,
               'class': 'form-control form-control-sm input_register'}))

    age = forms.IntegerField(label=_("Age"), widget=forms.NumberInput(attrs={'placeholder': _('Enter your age'),
                                                                             'class': 'form-control form-control-sm input_register',
                                                                             'min': '18'}))

    gender = forms.ChoiceField(choices=GENDER_CHOICES, widget=forms.Select(attrs={
        'class': 'form-select form-select-sm', }), label=_("Gender"))

    class Meta:
        model = Person

        fields = [
            'first_name',
            'last_name',
            'age',
            'gender',
            'phone',
            'photo',
            'description',
            'email',
            'password1',
            'password2',
        ]
