import os

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers.person_manager import PersonManager


def create_path_reviewer(instance, filename):
    return os.path.join(
        instance.name, instance.lastname,
        filename
    )


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
                                default='RW',
                                max_length=10, help_text='Reviewer = RW, Admin = AD',
                                null=True, blank=True)
    first_name: str = models.CharField(verbose_name=_('Name'), max_length=555)
    """Reviewer identifier name."""
    last_name: str = models.CharField(verbose_name=_('Last Name'), max_length=555)
    """Reviewer identifier lastname."""
    age: int = models.IntegerField(verbose_name=_('Age'), default='0')
    """Reviewer identifier age."""
    gender: str = models.CharField(verbose_name=_('Gender'), max_length=3)
    """Gender of the Reviewer. (Male, Trans , Female)."""
    phone: str = models.CharField(verbose_name=_('Phone'), max_length=10)
    """Cell phone number of the phone."""
    photo: str = models.ImageField(verbose_name=_('Photo'), upload_to=create_path_reviewer, blank=True, null=True)
    """Photo of the Reviewer."""
    description: str = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    """Field to detail the status of Reviewer."""
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
