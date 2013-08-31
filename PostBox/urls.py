from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from PostBox import views

urlpatterns = patterns('',
                       #url(r'^$', TemplateView.as_view(template_name='PostBox/index.html')),
                       url(r'^$', views.index, name='index'),
                       url(r'^selection/$', views.selection, name='selection'),
                       url(r'^(?P<user_id>\d+)/thankyou/$', views.thankyou, name='thankyou'),
                       url(r'^(?P<user_id>\d+)/feedback/$', views.feedback, name='feedback'),
                       )
