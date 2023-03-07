from django.urls import path
from . import views
urlpatterns = [
    path('',views.index,name="index"),
    path('about/',views.About,name="about"),
    #entre <> pedimos el request
    path('hello/<int:id>',views.hello,name="hello"),
    path('projects/',views.project,name="projects"),
    path('tasks/',views.tasks,name="tasks"),
    path('create_task/',views.create_task,name="create_task"),
    path('create_project/',views.create_project,name="create_project")
]