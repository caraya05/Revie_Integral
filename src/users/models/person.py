from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers.person_manager import PersonManager


class Person(AbstractUser):
    """Model Person.
        The Person model contains the authentication system, along with all the necessary fields to manage user information.

       :param AbstractUser: is a full User model, complete with fields, as an abstract class so that you can inherit from it and add your own profile fields and methods.
       :type AbstractUser: Model.
    """
    model_name = 'Person'
    username = None
    email = models.EmailField('email address', unique=True)
    """Email of the person, it is unique, that is, unrepeatable."""
    rol: str = models.CharField(verbose_name='Rol',
                                max_length=10, help_text='Reviewer = RW, Restaurant = RT, Admin = AD',
                                null=True, blank=True)
    """Person's role"""

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['rol', ]

    objects = PersonManager()

    class Meta:
        verbose_name = _('Person')
        verbose_name_plural = _('Persons')

    def __str__(self):
        return f'{self.email}'

    # @staticmethod
    # def autocomplete_search_fields():
    #     return 'email'
