from django.contrib import admin
from loducode_utils.admin import AuditAdmin

from reviews.models.reviewer import Reviewer


@admin.register(Reviewer)
class ReviewerAdmin(AuditAdmin):
    list_display = ('name', 'lastname', 'description',)
    list_display_links = ('name', 'lastname', 'description',)
    search_fields = ('name', 'lastname', 'gender')
    ordering = ('name', 'lastname', 'age',)
    list_filter = ('gender', 'age')


