from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class ReviewsConfig(AppConfig):
    name = 'reviews'
    verbose_name = _('Reviews')

    def ready(self):
        import reviews.signals  # pylint: disable=C0415 W0611
