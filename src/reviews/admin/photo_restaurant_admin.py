from django.contrib import admin
from loducode_utils.admin import AuditAdmin

from reviews.models.photo_restaurant import PhotoRestaurant


@admin.register(PhotoRestaurant)
class PhotoRestaurantAdmin(AuditAdmin):
    list_display = ('restaurant',)
    list_display_links = ('restaurant',)
    search_fields = ('restaurant__name',)
    list_filter = ('restaurant__name',)
    raw_id_fields = ('restaurant',)
    ordering = ('restaurant',)

