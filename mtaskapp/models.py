from django.db import models
from django.db.models import Model
from mtaskapp.utils import slug_save
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
# Create your models here.
STATUS_CHOICES = ((True, 'Active'), (False, 'Inactive'))
TASK_CHOICES = (('TODO', 'TODO'), ('DOING', 'DOING'), ('DONE', 'DONE'))

class Board(Model):
    title = models.CharField(max_length=40)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True, choices=STATUS_CHOICES)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title



# __str__ = prints the value of title
pre_save.connect(slug_save, sender=Board)


class Task(Model):
    title = models.CharField(max_length=60)
    due_date = models.DateField(auto_now=False,null=True,blank=True)
    time = models.DateTimeField(auto_now=False,null=True,blank=True)
    description = models.CharField(max_length=300,null=True,blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE)
    status = models.CharField(max_length=6, default='TODO', choices=TASK_CHOICES)
    is_active = models.BooleanField(default=True, choices=STATUS_CHOICES)
    slug = models.SlugField(unique=True, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_notification(self):
        return f'{self.title} expected to complete on {self.due_date.strftime("%d %B, %Y")}'
    
    def activate(self):
        self.is_active = True
        self.save()
    
    def deactivate(self):
        self.is_active = False
        self.save()
 
    def change_status(self, index):
        self.status = TASK_CHOICES[index][0]
        self.save()

class Notification(Model):
    title = models.CharField(max_length=60)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    task = models.ForeignKey(Task,on_delete=models.CASCADE)
    status = models.CharField(max_length=6,default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} {self.task} at {self.created_at}"



pre_save.connect(slug_save, sender=Task)
# pre save = operation before save done on the data must and it is unique
# slug = it is field which contains a url in human readable content
# slug_Save logic


class NotificationLog(Model):
    is_today = models.DateField(auto_now=True)
    user =  models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=6,default=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Contactus(models.Model):
    name = models.CharField(max_length=30,blank=True)
    email = models.CharField(max_length=30,blank=True)
    subject = models.CharField(max_length=30,blank=True)
    message = models.CharField(max_length=200,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return str(self.name)