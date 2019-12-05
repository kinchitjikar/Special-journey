
from django.urls import path

from mtaskapp.views import (boardpage, change_task_status, create_board,
                            create_task, dashboard, delete_board, delete_task,
                            index, tasks, update_board, update_task,aboutus,contact,services,notification_data,addcontact)

urlpatterns = [
    path('', index, name='index'),
    path('aboutus', aboutus, name='aboutus'),
    path('contact', contact, name='contact'),
    path('addcontact', addcontact, name='addcontact'),
    path('services', services, name='services'),
    path('notification', notification_data, name='notification'),

    path('dashboard', dashboard, name='dashboard'),
    path('boards/<str:slug>',tasks,name='tasks'),
    path('create_board', create_board, name='create_board'),
    path('update_board', update_board, name='update_board'),
    path('delete_board', delete_board, name='delete_board'),
    path('create_task', create_task, name='create_task'),
    path('update_task', update_task, name='update_task'),
    path('change_task_status', change_task_status, name='change_task_status'),
    path('delete_task', delete_task, name='delete_task'),
    
]
