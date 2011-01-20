from django.shortcuts import render_to_response
from django.template import RequestContext
import models
import settings

def volunteer (request):

    new_tasks = models.Task.objects.filter(completed=True)
    completed_tasks = models.Task.objects.filter(completed=True)
    return render_to_response('tasks.html', {'new_tasks': new_tasks, 'completed_tasks': completed_tasks,}, context_instance = RequestContext(request))