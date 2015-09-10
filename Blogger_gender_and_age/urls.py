from django.conf.urls import patterns, url

from Blogger_gender_and_age import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/results/
    url(r'^result/$', views.result, name='result'),
    url(r'^add/(?P<pred_gender>\w+)/$', views.add, name='add'),
)
