from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import hello.views

from gettingstarted.settings import STATIC_ROOT_DEVELOPMENT, DEBUG

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'gettingstarted.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
urlpatterns += patterns('',
url(r'^static/(.*)$', 'django.views.static.serve', {'document_root': STATIC_ROOT_DEVELOPMENT, 'show_indexes': True}),
)
