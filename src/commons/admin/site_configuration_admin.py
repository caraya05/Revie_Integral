from django.contrib import admin

from solo.admin import SingletonModelAdmin
from commons.models.site_configuration import SiteConfigurationM

admin.site.register(SiteConfigurationM, SingletonModelAdmin)
