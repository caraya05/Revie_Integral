"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from rest_framework_swagger.views import get_swagger_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns_api = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
schema_view = get_swagger_view(title='Backend API', patterns=urlpatterns_api)

urlpatterns_root = i18n_patterns(
    path('jet/', include('jet.urls', 'jet')),
    path('admin/', admin.site.urls),
    # path('admin/defender/', include('defender.urls')),  # defender admin
    # path('hijack/', include('hijack.urls', namespace='hijack')),
    path('api/api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api-doc/', schema_view, name='api-doc'),  # swagger
)
urlpatterns = urlpatterns_root + urlpatterns_api + static(
    settings.STATIC_URL, document_root=settings.STATIC_ROOT
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Administración Backend'
admin.site.index_title = 'Backend'
admin.site.site_title = 'Administración'
