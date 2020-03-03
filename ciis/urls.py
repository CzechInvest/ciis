"""ciis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.urls import include, path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
import django.views.static
from .views import IndexView
from cigeo import views as cviews
from addresses import views as aviews
from circular_economy import views as ceviews
from ai import views as aiviews
from vtp import views as vtpviews

from .router import router



urlpatterns = [
    url('^$', IndexView.as_view(), name="index_page"),
    path('admin/', admin.site.urls),
    url(r'^nested_admin/', include('nested_admin.urls')),
    url('^brownfields/', include('brownfields.urls')),
    #url('^properties/', include('entrepreneurial_property.urls')),
    url('^address/', include('addresses.urls')),
    url('^whoiswho/', include('whoiswho.urls')),
    url('^cigeo/', include('cigeo.urls')),
    url('^socekon/', include('socekon.urls')),
    url(r'^api/', include(router.urls)),
    #url(r'^api/socekon/', include(socekon.api_urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace="cigeo")),
    path('accounts/', include('django.contrib.auth.urls')),
    path('microsoft/', include('microsoft_auth.urls', namespace='microsoft')),
]

if settings.DEBUG:
    urlpatterns.append(
        url(r'^media/(?P<path>.*)$',
            django.views.static.serve, {'document_root': settings.MEDIA_ROOT}))
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = 'CzechInvest data admin'
