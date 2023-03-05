from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('about/',views.About),
    #entre <> pedimos el request
    path('hello/<int:id>',views.hello),
    path('projects/',views.project),
    path('tasks/',views.tasks)
]