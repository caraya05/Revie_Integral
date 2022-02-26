from datetime import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _
from geoposition.fields import GeopositionField
from loducode_utils.models.audit import Audit

from reviews.managers.restaurant_manager import RestaurantManager


class Restaurant(Audit):
    """Model Reviewer.
        This Reviewer model have all the necessary fields to manage the health of the pets.

        :param Audit: AuditModel acts as an abstract base class from which every other model in the project will inherit. This class provides
        :type Audit: Model.
        """
    model_name = 'Restaurant'

    name: str = models.CharField(verbose_name=_('Name'), max_length=555)
    """Restaurant identifier name."""
    nit: str = models.CharField(verbose_name=_('NIT'), max_length=20)
    """Restaurant identifier nit."""
    phone: str = models.CharField(verbose_name=_('Phone'), max_length=10)
    """Cell phone number of the restaurant."""
    location: GeopositionField = GeopositionField(verbose_name=_('Location'), blank=True, null=True)
    """store the coordinates of the main office of the project contact us"""
    website: str = models.CharField(verbose_name=_('Web Site'), max_length=100, blank=True, null=True)
    """Official website of the restaurant."""
    description: str = models.TextField(verbose_name=_('Description'), null=True, blank=True)
    """Field to detail the status of restaurant."""
    score: str = models.CharField(verbose_name=_('Score'), max_length=10, blank=True, null=True, default='0')
    """Points of the restaurant."""
    date_create: datetime = models.DateField(verbose_name=_('Date Create'))
    """Create date of the restaurant."""
    objects = RestaurantManager()

    class Meta(Audit.Meta):
        verbose_name = _('Restaurant')
        verbose_name_plural = _('Restaurants')

    def __str__(self):
        return f'{self.name}'

    # @staticmethod
    # def autocomplete_search_fields():
    #     return 'name'
