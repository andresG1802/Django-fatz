from django.http import HttpResponse,JsonResponse
from .models import Project,Task
from django.shortcuts import get_object_or_404,render,redirect
from .forms import CreateNewTask,CreateNewProject
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
    return render(request,"projects/projects.html",{
        'projects':projects
    })
def tasks(request):
    # task = Task.objects.get(id=id)

    # task = get_object_or_404(Task,id=id)
    # return HttpResponse('tasks %s' % task.title)
    tasks = Task.objects.all()
    return render(request,"tasks/task.html",{
        'tasks':tasks
    })

def create_task(request):

    # print(request.GET['title'])
    # print(request.GET['description'])
    if request.method == 'GET':
        #show interface
        return render(request,'tasks/create_task.html',{
        'form':CreateNewTask()
        })
    else:
        Task.objects.create(title=request.POST['title'],     description=request.POST['description'],     project_id=2)
        #el slash al principio es para que redireccion
        #osea el local...tal y al comenzar al ruta
        #tiene un slash local..8000/task/ ya por eso
        #se pone al principio para redireccione
        # return redirect('/tasks/')
        return redirect('tasks')

def create_project(request):
    if request.method == 'GET':
        return render(request,'projects/create_project.html',{
            'form':CreateNewProject()
        })
    else:
        # project=Project.objects.create(name=request.POST["name"])

        # return render(request,'projects/create_project.html',{
        #     'form':CreateNewProject()
        # })
        Project.objects.create(name=request.POST["name"])
        redirect('projects')
    