from django.contrib import admin
from loducode_utils.admin import AuditAdmin

from reviews.models.review import Review


@admin.register(Review)
class ReviewAdmin(AuditAdmin):
    list_display = ('title', 'date', 'description',)
    list_display_links = ('title', 'date', 'description',)
    search_fields = ('title', 'date',)
    list_filter = ('date', 'score_service', 'score_food', 'score_environment', 'score_quality_price',)
    ordering = ('title', 'date',)
