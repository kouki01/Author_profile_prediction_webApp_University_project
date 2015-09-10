from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'blogger_predict.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^Blogger_gender_and_age/', include('Blogger_gender_and_age.urls', namespace='Blogger_gender_and_age')),
    url(r'^admin/', include(admin.site.urls)),
)
