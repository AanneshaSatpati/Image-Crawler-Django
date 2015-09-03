from django.conf.urls import patterns, include, url
from myapp import views
import myapp
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Image_Crawler.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^myapp/', include('myapp.urls')),
    url(r'^uinput/$', myapp.views.uinput, name='uinput'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url('', include('django.contrib.auth.urls', namespace='auth')),
    url(r'^admin/', include(admin.site.urls)),
)