from django.contrib import admin

from mtaskapp.models import Board, Notification, NotificationLog, Task,Contactus

# Register your models here.
admin.site.register(Board)
admin.site.register(Task)
admin.site.register(Notification)
admin.site.register(NotificationLog)
admin.site.register(Contactus)

