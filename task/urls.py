from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.allTasks, name='AllTasks'),
    path('<int:id_task>', views.Task, name='id_task'),
]
