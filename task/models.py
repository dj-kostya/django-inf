from django.conf import settings
from django.db import models
from django.utils import timezone


class Tasks(models.Model):
    id_task = models.IntegerField(null=False, unique=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    with_image = models.BooleanField(default=False)

    def publish(self):
        self.save()

    def __int__(self):
        return self.id_task


class Images(models.Model):
    uri = models.CharField(max_length=255)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __str__(self):
        return self.uri


class TaskImage(models.Model):
    id_task = models.ForeignKey(to='Tasks', on_delete=models.CASCADE, to_field='id')
    id_image = models.ForeignKey(to='Images', to_field='id', on_delete=models.CASCADE)
    created_date = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.save()

    def __int__(self):
        return self.id
