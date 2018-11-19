from django.contrib.auth.views import login, logout
from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from btt.core.views import (
    mainlogin,
    home,
    password,
    picture,
    profile,
    public_profile,
    settings,
)
from btt.search.views import search
from btt.profile.views import signup


admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', home, name='home'),
    url(r'^accounts/', include('django.contrib.auth.urls')),
    url(r'^logout', logout, {'next_page': '/'}, name='logout'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^public_profile/(?P<id>\d+)/$', public_profile, name='public_profile'),
    url(r'^settings/$', settings, name='settings'),
    url(r'^settings/profile/$', profile, name='profile'),
    url(r'^settings/password/$', password, name='password'),
    url(r'^questions/', include('btt.questions.urls')),
    url(r'^search/$', search, name='search'),
    url(r'^(?P<username>[^/]+)/$', profile, name='profile'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
]
