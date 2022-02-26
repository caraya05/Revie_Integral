from django.contrib import admin
from loducode_utils.admin import AuditAdmin

from reviews.models.restaurant import Restaurant


@admin.register(Restaurant)
class RestaurantAdmin(AuditAdmin):
    list_display = ('name', 'nit', 'description',)
    list_display_links = ('name', 'nit', 'description',)
    search_fields = ('name', 'nit',)
    ordering = ('name',)
    list_filter = ('name',)

