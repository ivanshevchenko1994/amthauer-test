"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from ninja import NinjaAPI

from config import settings
from config.constants import app_const, api_const

import debug_toolbar

from django.conf.urls.static import static
from django.contrib import admin
from src.amthauer.api import amthauer_router
from src.security.views import auth_router
from django.urls import include, path
from django.utils.translation import gettext as _
from django.contrib.admin.views.decorators import staff_member_required

admin.site.site_header = app_const.BRAND_NAME
admin.site.site_title = app_const.BRAND_NAME + _("Admin")
admin.site.index_title = app_const.BRAND_NAME + _("Admin")

api = NinjaAPI(title=app_const.BRAND_NAME, version=api_const.API_VERSION_1, docs_decorator=staff_member_required)

api.add_router("/auth/", auth_router)
api.add_router("/amthauer/", amthauer_router)

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('__debug__/', include(debug_toolbar.urls)),
    path("api/v1/", api.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
