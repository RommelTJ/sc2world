from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^sc2world/', include('sc2world.foo.urls')),

    # Navigation
    (r'^', include('sc2world.main.urls')),
    (r'^players/', include('sc2world.player.urls')),
    (r'^monitor/', include('sc2world.monitor.urls')),
    (r'^feeds/', include('sc2world.feeds.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
                       
    # Administration
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)

import os
from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('', (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': os.path.join(os.path.dirname(__file__), 'static')}),
                            )
