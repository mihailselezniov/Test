from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^list_of_discounts/', include('list_of_discounts.urls', namespace="list_of_discounts")),

    url(r'^admin/', include(admin.site.urls)),
)
