import os
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.restaurant_manager import RestaurantManager


def create_path_photo_restaurant(instance, filename):
    full_name = str(instance.restaurant.name) + '' + str(instance.restaurant.date_create)
    return os.path.join(
        full_name,
        filename
    )


class PhotoRestaurant(Audit):
    """Model Reviewer.
        This Reviewer model have all the necessary fields to manage the photo restaurant.

        :param Audit: AuditModel acts as an abstract base class from which every other model in the project will inherit. This class provides
        :type Audit: Model.
        """
    model_name = 'PhotoRestaurant'
    restaurant: Optional = models.ForeignKey(to='reviews.restaurant', verbose_name='Restaurant',
                                             on_delete=models.CASCADE)
    """Unique code already generated automatically to identify the restaurant.It's is in a foreign key and is in UUID"""
    photo_one: str = models.ImageField(verbose_name=_('Photo One'), upload_to=create_path_photo_restaurant, blank=True,
                                       null=True)
    """Photo of the PhotoRestaurant."""
    order: int = models.IntegerField(verbose_name=_('Order'))
    """Number of the image."""
    objects = RestaurantManager()

    class Meta(Audit.Meta):
        verbose_name = _('Photo Restaurant')
        verbose_name_plural = _('Photos Restaurants')

    def __str__(self):
        return f'{self.restaurant}'

    @staticmethod
    def autocomplete_search_fields():
        return 'restaurant'
