from django.contrib import admin
from .models import Tasks, Images, TaskImage

admin.site.register(Tasks)
admin.site.register(TaskImage)
admin.site.register(Images)
# Register your models here.
