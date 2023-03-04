from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404
# Create your views here.
def index(request):
    return HttpResponse("Index_page")

def hello(request,username):
    #para concatenar la variable pones %s al costado % con el nombre
    # de la varible
    return HttpResponse("<h1>Hello %s<h1>" % username)
def About(request):
    return HttpResponse("<h1>About<h1>")

def project(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects,safe=False)

def tasks(request,name):
    # task = Task.objects.get(id=id)

    task = get_object_or_404(Task,id=id)
    return HttpResponse('tasks %s' % task.title)