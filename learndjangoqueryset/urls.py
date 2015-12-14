from django.conf.urls import include, url, patterns
from django.contrib import admin
from django.conf import settings

from queries.views import home_view, insert_view


urlpatterns = [
    # Examples:
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', home_view, name='home'),
    url(r'^insert/$', insert_view, name='insert'),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
