import simplejson as json
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.shortcuts import get_object_or_404
import models

def index (request):

    murals = models.Mural.published_objects.all()
    murals_clean = []
    for mural in murals:
        murals_clean.append({'title': mural.title, 'lat': mural.lat, 'lng': mural.lng})

    return render_to_response('index.html', {'murals_json': json.dumps(murals_clean),}, context_instance = RequestContext(request))
    

def murals (request):

    murals = models.Mural.published_objects.all()
    return render_to_response('murals.html', {'murals': murals,}, context_instance = RequestContext(request))

def mural(request, uri_slug):    

    mural = get_object_or_404(models.Mural.published_objects, uri_slug=uri_slug)
    return render_to_response('mural.html', {'mural': mural,}, context_instance = RequestContext(request))        


def artists (request):

    artists = models.Artist.published_objects.all()
    return render_to_response('artists.html', {'artists': artists,}, context_instance = RequestContext(request))
    
def artist(request, uri_slug):    

    artist = get_object_or_404(models.Artist.published_objects, uri_slug=uri_slug)
    return render_to_response('artist.html', {'artist': artist,}, context_instance = RequestContext(request))