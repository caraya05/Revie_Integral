import os
from datetime import datetime
from typing import Optional

from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.timezone import now
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.review_manager import ReviewManager


def create_path_photo_review(instance, filename):
    full_name = str(instance.title) + '' + str(instance.date)
    return os.path.join(
        full_name,
        filename
    )


class Review(Audit):
    """Model Reviewer.
        This Reviewer model have all the necessary fields to manage the reviews.

        :param Audit: AuditModel acts as an abstract base class from which every other model in the project will inherit. This class provides
        :type Audit: Model.
        """
    model_name = 'Review'

    score1 = '1'
    score2 = '2'
    score3 = '3'
    score4 = '4'
    score5 = '5'

    SCORE_CHOICES = [
        ('1', score1),
        ('2', score2),
        ('3', score3),
        ('4', score4),
        ('5', score5)
    ]

    title: str = models.CharField(verbose_name=_('Title'), max_length=555)
    """Title of the Review."""

    date: datetime = models.DateField(verbose_name=_('date'), default=now, editable=False   )
    """Date on which the review was performed."""
    description: str = models.TextField(verbose_name=_('Description'))
    """description of the review."""
    score: int = models.IntegerField(verbose_name=_('Score'), blank=True, null=True, default=0,
                                     validators=[
                                         MinValueValidator(0), MaxValueValidator(5)])
    score_service: str = models.CharField(verbose_name=_('Score Service'), max_length=6, choices=SCORE_CHOICES,
                                          default='0')
    """score of the service."""
    score_food: str = models.CharField(verbose_name=_('Score Food'), max_length=6, choices=SCORE_CHOICES,
                                       default='0')
    """score of the food."""

    score_environment: str = models.CharField(verbose_name=_('Score Environment'), max_length=6, choices=SCORE_CHOICES,
                                              default='0')
    """score of the environment."""

    score_quality_price: str = models.CharField(verbose_name=_('Score Quality Price'), max_length=6,
                                                choices=SCORE_CHOICES, default='0')
    """score of the quality price."""
    photo_one: str = models.ImageField(verbose_name=_('Photo One'), upload_to=create_path_photo_review, blank=True,
                                       null=True)
    """Photo of the PhotoReview."""
    photo_two: str = models.ImageField(verbose_name=_('Photo Two'), upload_to=create_path_photo_review, blank=True,
                                       null=True)
    """Photo of the PhotoReview."""
    photo_three: str = models.ImageField(verbose_name=_('Photo Three'), upload_to=create_path_photo_review, blank=True,
                                         null=True)
    """Photo of the PhotoReview."""

    place: Optional = models.ForeignKey(to='reviews.restaurant', verbose_name='restaurant', on_delete=models.CASCADE)

    person: Optional = models.ForeignKey(to='users.person', verbose_name='person', on_delete=models.CASCADE)

    # def photo_person(self):
    #     return self.person.photo

    objects = ReviewManager()

    class Meta(Audit.Meta):
        verbose_name = _('Review')
        verbose_name_plural = _('Reviews')

    def __str__(self):
        return f'{self.title} {self.date}'

    @staticmethod
    def autocomplete_search_fields():
        return 'title'
