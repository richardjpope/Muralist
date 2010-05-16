import simplejson as json
from django.shortcuts import render_to_response
from django.template import RequestContext
import models

def index (request):

    murals = models.Mural.published_objects.all()
    murals_clean = []
    for mural in murals:
        murals_clean.append({'title': mural.title, 'lat': mural.lat, 'lng': mural.lng})

    return render_to_response('index.html', {'murals_json': json.dumps(murals_clean),}, context_instance = RequestContext(request))