import json
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.forms.models import model_to_dict
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse

from mtaskapp.models import Board, Task, Notification, Contactus
from django.contrib import messages

# Create your views here.


def index(request):
    context = {}
    return render(request, 'index.html', context)

def aboutus(request):
    context = {}
    return render(request,'aboutus.html',context)

def services(request):
    context = {}
    return render(request,'services.html',context)

def contact(request):
    context = {}
    return render(request,'contact.html',context)

def addcontact(request):
    contactus = Contactus(name=request.POST['name'],email=request.POST['email'],subject=request.POST['subject'],message=request.POST['message'])
    contactus.save()
    return HttpResponse("Recorded Succesfully we will contact you in 48 hours")

@login_required
def notification_data(request):
    notifications = Notification.objects.all().filter(user=request.user).order_by('-pk')
    context = {'notification':notifications}
    return render(request,'notification.html',context)

@login_required
def dashboard(request):
    user = request.user
    context = {'boards': Board.objects.all().filter(user=user).order_by('-pk') }
    return render(request, 'dashboard.html', context)


@login_required
def tasks(request, slug):
    board = Board.objects.get(slug=slug, user=request.user)
    context = {
        'todo_tasks': Task.objects.all().filter(board=board,status="TODO").order_by('updated_at'),
        'doing_tasks': Task.objects.all().filter(board=board,status="DOING").order_by('updated_at'),
        'done_tasks': Task.objects.all().filter(board=board,status="DONE").order_by('updated_at'),
        'board':board,
    }
    return render(request, 'boardpage.html', context)


@login_required
def create_board(request):
    if request.method == "POST":

        board =  Board(title=request.POST.get('title'), user=request.user)
        board.save()

        return JsonResponse({"message": "Success", 'board':model_to_dict(board)})
    else:
        return JsonResponse({"message": "Failed"})


@login_required
def boardpage(request):
    context = {}
    return render(request, 'boardpage.html', context)


@login_required
def update_board(request):
    if request.method == "POST":
        board = Board.objects.get(id=request.POST.get('pk'))
        board.title = request.POST.get('title')
        board.save()
        return JsonResponse({"message": "Success"})
    else:
        return JsonResponse({"message": "Failed"})


@login_required
def delete_board(request):
    if request.method == "POST":
        board = Board.objects.get(id=request.POST.get('pk'))
        # board.title = request.GET.get('title')
        board.delete()
        return JsonResponse({"message": "Success"})
    else:
        return JsonResponse({"message": "Failed"})


@login_required
def create_task(request):
    if request.is_ajax():
        if request.method == 'POST':
            inp = {}
            inp['title'] = request.POST.get('title')
            if request.POST.get('description'):
                inp['description']=request.POST.get('description')
            print(Board.objects.get(pk=request.POST.get('board')))
            inp['board']=Board.objects.get(pk=request.POST.get('board'))
            if request.POST.get('due_date'):
                inp['due_date'] = request.POST.get('due_date')
            if request.POST.get('due_date') and request.POST.get('time'):
                inp['time'] =  request.POST.get('due_date') + ' ' + request.POST.get('time')
            task = Task(**inp)
            task.save()
            return JsonResponse({"message": "success", 'task': model_to_dict(task)})
        else:
            return JsonResponse({"message": "unauthorized no POST"})
    else:
        return JsonResponse({"message":"unauthorized no ajax"})


@login_required
def change_task_status(request):
    if request.is_ajax():
        if request.method == 'POST':
            task = Task.objects.get(slug=request.POST.get('task_id'))
            task.change_status(int(request.POST.get('status')))
            return JsonResponse({"message":"success"})
        else:
            return JsonResponse({"message":"unauthorized no post"})
    else:
        return JsonResponse({"message":"unauthorized no ajax"})

@login_required
def update_task(request):
    if request.is_ajax():
        if request.method == 'POST':
            task = Task.objects.get(pk=request.POST.get('task_id'))
            
            task.title = request.POST.get('title')
            if request.POST.get('due_date'):
                task.due_date = request.POST.get('due_date')
            if task.due_date and request.POST.get('time'):
                task.time = task.due_date + ' ' + request.POST.get('time') 
            if request.POST.get('description'):
                task.description = request.POST.get('description')
            task.save()
            return JsonResponse({"message":"success", 'task':model_to_dict(task)})
        else:
            return JsonResponse({"message":"unauthorized no post"})
    else:
        return JsonResponse({"message":"unauthorized no ajax"})

@login_required
def delete_task(request):
    if request.method == 'POST':
        task = Task.objects.get(id=request.POST.get('task_id'))
        task.delete()
        return JsonResponse({"message":"success"})
    else:
        return JsonResponse({"message":"success"})
