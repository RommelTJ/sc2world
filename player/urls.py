from django.conf.urls.defaults import *

from views import *


urlpatterns = patterns('',
    url(r'^show/(?P<id>\d+)/$', show, name='player-show'),
    url(r'^create/$', create, name='player-create'),
    url(r'^update/(?P<id>\d+)/$', update, name='player-update'),
    url(r'^title/(?P<slug>[\d\w-]+)/$', title, name='player-title'),
)
