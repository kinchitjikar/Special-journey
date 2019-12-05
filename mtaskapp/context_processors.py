from django.contrib.auth.models import User
# from django.utils.timezone import datetime

import datetime

from mtaskapp.models import Board, Notification, Task, NotificationLog


def add_variable_to_context(request):
    if request.user.is_authenticated:
        try:
            user = request.user
            boards = Board.objects.all().filter(user=user)
            
            notification_log = NotificationLog.objects.get(user=user)
            
            if notification_log.is_today == datetime.date.today():
                for board in boards:
                    tasks = Task.objects.all().filter(board=board, due_date=datetime.date.today())
                    for task in tasks:
                        try:
                            notification = Notification.objects.get(task=task)
                        except:
                            notification = Notification(title=task.get_notification(), user=user, task=task)
                            notification.save()
            elif notification_log.is_today != datetime.date.today() and notification_log.is_today == datetime.date.today() - datetime.timedelta(1):
                for board in boards:
                    tasks = Task.objects.all().filter(board=board, due_date=datetime.date.today())
                    for task in tasks:
                        notification = Notification(title=task.get_notification(), user=user, task=task)
                        notification.save()   
            else:
                dif = datetime.date.today() - notification_log.is_today
                for one in range(dif.days, -1, -1):
                    for board in boards:
                        tasks = Task.objects.all().filter(board=board, due_date=datetime.date.today()-datetime.timedelta(one))
                        for task in tasks:
                            notification = Notification(title=task.get_notification(), user=user, task=task)
                            notification.save()
            notifications = Notification.objects.all().filter(user=user).order_by('-pk')[:6]
            return {'notification':notifications}
        except Exception as e:
            #raise e
            return {'notification':None}
    return {'notification':None}