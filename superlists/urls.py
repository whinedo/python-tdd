from django.conf.urls import patterns, include, url
import lists.views

from django.contrib import admin
admin.autodiscover()

#urlpatterns = patterns('',
#    # Examples:
#    url(r'^$', 'lists.views.home_page', name='home'),
#    # url(r'^blog/', include('blog.urls')),
#
#    # url(r'^admin/', include(admin.site.urls)),
#)


urlpatterns = [
    url(r'^$', lists.views.home_page, name='home'),
    url(r'^lists/the-only-list-in-the-world/$', lists.views.view_list, name='view_list'),
]
