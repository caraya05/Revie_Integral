from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.restaurant_manager import RestaurantManager


class TopRestaurant(Audit):
    model_name = 'toprestaurant'
    restaurant: Optional = models.ForeignKey(to='reviews.Restaurant', verbose_name=_('Restaurant'), blank=True,
                                             null=True, on_delete=models.CASCADE)
    top: int = models.IntegerField(verbose_name=_('Number Top'), blank=True, null=True, default=0)
    score: int = models.IntegerField(verbose_name=_('Score'), blank=True, null=True, default=0)
    objects = RestaurantManager()

    class Meta(Audit.Meta):
        verbose_name = _('Top Restaurant')
        verbose_name_plural = _('Top Restaurants')

    def __str__(self):
        return f'{self.top}/{self.restaurant}'

    # @staticmethod
    # def autocomplete_search_fields():
    #     return 'name'
