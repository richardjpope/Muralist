import simplejson as json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
import models
import settings
import flickrapi
import feedparser

def index (request):

    #get blog rss feed
    blog_items = feedparser.parse(settings.BLOG_FEED)    

    #get murals for map
    murals = models.Mural.published_objects.all()
    murals_clean = []
    for mural in murals:
        murals_clean.append({'title': mural.title, 'uri_slug': mural.uri_slug, 'lat': mural.lat, 'lng': mural.lng, 'condition_tag': mural.condition_tag(),'condition_text': mural.condition_text(),})

    return render_to_response('index.html', {'murals_json': json.dumps(murals_clean), 'blog_items': blog_items['entries'][:2]}, context_instance = RequestContext(request))

def murals (request):

    murals = models.Mural.published_objects.all()
    return render_to_response('murals.html', {'murals': murals,}, context_instance = RequestContext(request))

def mural_memories(request, uri_slug):
    return mural(request, uri_slug, 'memories')

def mural_photos(request, uri_slug):
    return mural(request, uri_slug, 'photos')
        
def mural(request, uri_slug, page='history'):

    #get mural
    mural = get_object_or_404(models.Mural.published_objects, uri_slug=uri_slug)

    #show timeline?
    show_timeline = mural.muralevent_set.count() > 2

    #size representation
    pictogram_width = None
    pictogram_height = None    
    if mural.aspect_ratio():
        pictogram_width = 200
        pictogram_height = pictogram_width * mural.aspect_ratio()

    #get photos
    thumbnails = []
    if page == 'photos':
        flickr = flickrapi.FlickrAPI(settings.FLICKR_API_KEY)
        photos = flickr.photos_search(tag_mode='all', machine_tags='lmps:mural=' + str(mural.id), page=1, per_page=5)
        thumbnails = []
        for photo in photos[0]:
        	photoSizes = flickr.photos_getSizes(photo_id=photo.attrib['id'])
        	thumbnails.append(photoSizes[0][4].attrib['source'])

    #work out template
    template = 'mural.html'
    if page == 'photos':
        template = 'mural_photos.html'        
    if page == 'memories':
        template = 'mural_memories.html'        

    return render_to_response(template, {'mural': mural, 'thumbnails': thumbnails, 'show_timeline': show_timeline, 'pictogram_width': pictogram_width, "pictogram_height": pictogram_height, 'page': page}, context_instance = RequestContext(request))        


def artists (request):

    artists = models.Artist.published_objects.all()
    return render_to_response('artists.html', {'artists': artists,}, context_instance = RequestContext(request))
    
def artist(request, uri_slug):    

    artist = get_object_or_404(models.Artist.published_objects, uri_slug=uri_slug)
    return render_to_response('artist.html', {'artist': artist,}, context_instance = RequestContext(request))