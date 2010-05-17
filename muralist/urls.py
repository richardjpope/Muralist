from django.conf.urls.defaults import *
from django.contrib import admin
from murals import views as muralist_views
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', muralist_views.index, name="index"),
    (r'^admin/', include(admin.site.urls)),    
    
    # static media server for the dev sites / local dev
    url(r'^media/(?P<path>.*)$',       'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),
    url(r'^media-admin/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ADMIN_DIR, 'show_indexes':True}),    
    
)
