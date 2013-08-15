from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from PostBox import views

urlpatterns = patterns('', url(r'^$', TemplateView.as_view(template_name='PostBox/index.html')),
                       #views.index, name='index'),
                       url(r'^selection/$', views.selection, name='selection'),
                       url(r'^thankyou/$', views.thankyou, name='thankyou'),
                       )
