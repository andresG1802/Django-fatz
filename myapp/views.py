from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render
# Create your views here.
def index(request):
    #return HttpResponse("Index_page")
    title = "Django Course!!"
    return render(request,"index.html",{
        'title':title
    })

def hello(request,username):
    #para concatenar la variable pones %s al costado % con el nombre
    # de la varible
    return HttpResponse("<h1>Hello %s<h1>" % username)
    
def About(request):
    # return HttpResponse("<h1>About<h1>")
    username = 'Andres'
    return render(request,"About.html",{
        'username':username
    })

def project(request):
    # projects = list(Project.objects.values())

    projects = Project.objects.all()
    # return JsonResponse(projects,safe=False)
    return render(request,"projects.html",{
        'projects':projects
    })
def tasks(request):
    # task = Task.objects.get(id=id)

    # task = get_object_or_404(Task,id=id)
    # return HttpResponse('tasks %s' % task.title)
    tasks = Task.objects.all()
    return render(request,"task.html",{
        'tasks':tasks
    })