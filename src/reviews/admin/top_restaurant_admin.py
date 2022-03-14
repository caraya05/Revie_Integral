from django.contrib import admin
from loducode_utils.admin import AuditAdmin

from reviews.models.top_restaurant import TopRestaurant


@admin.register(TopRestaurant)
class TopRestaurantAdmin(AuditAdmin):
    list_display = ('restaurant', 'top', 'score')
    list_display_links = ('restaurant', 'top', 'score')
    search_fields = ('restaurant__name',)
    ordering = ('top',)
    readonly_fields = ('restaurant', 'top', 'score')
    raw_id_fields = ('restaurant',)
