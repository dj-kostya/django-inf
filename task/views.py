from django.shortcuts import render
from task.models import Tasks, Images, TaskImage
from inspect import getmembers
from pprint import pprint


def allTasks(request):
    tasks = Tasks.objects.order_by('id_task')
    return render(request, 'task/AllTasks.html', {'tasks': tasks})


# Create your views here.


def Task(request, id_task):
    urls_src = []
    task = Tasks.objects.filter(id_task=id_task).first()
    pprint(task.id)
    if task.with_image:
        urls = TaskImage.objects.filter(id_task=task.id)
        for url in urls:
            uri = Images.objects.filter(id=url.id_image_id).first()
            urls_src.append(uri)
        pprint(urls_src)
    return render(request, 'task/SingleTask.html', {'task': task, 'images': urls_src})
