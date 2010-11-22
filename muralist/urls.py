from django.conf.urls.defaults import *
from django.contrib import admin
from murals import views as muralist_views
import settings

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', muralist_views.index, name="index"),
    url(r'^murals/$', muralist_views.murals, name="murals"),    
    url(r'^murals/(?P<uri_slug>[\w_\-]+)/$', muralist_views.mural, name="mural"),
    url(r'^murals/(?P<uri_slug>[\w_\-]+)/memories/$', muralist_views.mural_memories, name="mural_memories"),    
    url(r'^murals/(?P<uri_slug>[\w_\-]+)/photos/$', muralist_views.mural_photos, name="mural_photos"),        
    url(r'^artists/$', muralist_views.artists, name="artists"),        
    url(r'^artists/(?P<uri_slug>[\w_\-]+)/$', muralist_views.artist, name="artist"),    
    (r'^admin/', include(admin.site.urls)),    
    (r'^admin/(.*)', admin.site.root),
    
    # static media server for the dev sites / local dev
    url(r'^site-media/(?P<path>.*)$',       'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes':True}),    
    url(r'^admin-media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.ADMIN_MEDIA_ROOT, 'show_indexes':True}),        
)
