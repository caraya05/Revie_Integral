import os
from typing import Optional

from django.db import models
from django.utils.translation import gettext_lazy as _
from loducode_utils.models.audit import Audit

from reviews.managers.photo_review_manager import PhotoReviewManager


def create_path_photo_review(instance, filename):
    full_name = str(instance.review.title) + '' + str(instance.review.date)
    return os.path.join(
        full_name,
        filename
    )


class PhotoReview(Audit):
    """Model Reviewer.
        This Reviewer model have all the necessary fields to manage the health of the pets.

        :param Audit: AuditModel acts as an abstract base class from which every other model in the project will inherit. This class provides
        :type Audit: Model.
        """
    model_name = 'PhotoReview'
    review: Optional = models.ForeignKey(to='reviews.review', verbose_name='Review',
                                         on_delete=models.CASCADE)
    """Unique code already generated automatically to identify the PhotoReview .It's is in a foreign key and is in UUID"""
    photo_one: str = models.ImageField(verbose_name=_('Photo One'), upload_to=create_path_photo_review, blank=True,
                                       null=True)
    """Photo of the PhotoReview."""
    order: int = models.IntegerField(verbose_name=_('Order'))
    """Number of the image."""
    objects = PhotoReviewManager()

    class Meta(Audit.Meta):
        verbose_name = _('Photo Review')
        verbose_name_plural = _('Photos Reviews')

    def __str__(self):
        return f'{self.review}'

    @staticmethod
    def autocomplete_search_fields():
        return 'review'
