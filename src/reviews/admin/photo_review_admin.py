from django.contrib import admin
from loducode_utils.admin import AuditAdmin

from reviews.models.photo_review import PhotoReview


@admin.register(PhotoReview)
class PhotoReviewAdmin(AuditAdmin):
    list_display = ('review',)
    list_display_links = ('review',)
    search_fields = ('review__title',)
    ordering = ('review',)
    list_filter = ('review__title',)
    raw_id_fields = ('review',)
