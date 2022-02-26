import os

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.reviewer_manager import ReviewerManager


def create_path_reviewer(instance, filename):
    return os.path.join(
        instance.name, instance.lastname,
        filename
    )


class Reviewer(Audit):
    """Model Reviewer.
        This Reviewer model have all the necessary fields to manage the health of the pets.

        :param Audit: AuditModel acts as an abstract base class from which every other model in the project will inherit. This class provides
        :type Audit: Model.
    """
    model_name = 'Reviewer'

    name: str = models.CharField(verbose_name=_('Name'), max_length=555)
    """Reviewer identifier name."""
    lastname: str = models.CharField(verbose_name=_('Last Name'), max_length=555)
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
    objects = ReviewerManager()

    class Meta(Audit.Meta):
        verbose_name = _('Reviewer')
        verbose_name_plural = _('Reviewers')

    def __str__(self):
        return f'{self.name} {self.lastname}'

    # @staticmethod
    # def autocomplete_search_fields():
    #     return 'name', 'lastname'
