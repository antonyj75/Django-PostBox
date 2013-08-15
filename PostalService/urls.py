from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

#from PostBox import views

urlpatterns = patterns('',
    # url(r'^PostBox/', include('PostBox.urls')),
    url(r'^', include('PostBox.urls', namespace='PostBox')),
    # Examples:
    # url(r'^$', 'PostBox.views.index', name='index'),
    # url(r'^PostalService/', include('PostalService.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
