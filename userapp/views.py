from django.shortcuts import render, redirect
from django.http.response import JsonResponse,HttpResponse
from userapp.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from mtaskapp.models import NotificationLog

@login_required
def editprofile(request):
    context = {}
    return render(request,'editprofile.html',context)


def changepassword(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'changepassword.html', {
        'form': form
    })

@login_required
def update_profile(request):
    if request.method == 'POST':
        profile = Profile.objects.get(user=request.user)
        user  = User.objects.get(pk=request.user.pk)
        user.first_name = request.POST.get('firstname')
        user.last_name = request.POST.get('lastname')
        # print(request.FILES['profilepic'])
        profile.image = request.FILES['profilepic']
        user.save()
        profile.save()
        return redirect('profile')
    else:
        return JsonResponse({"message": "Failed"})

@login_required
def profile(request):
    context = {'profile':Profile.objects.get(user=request.user)}
    return render(request,'profile.html',context)

def login_view(request):
    try:
        if request.method == 'POST':
            # do login
            c_user = authenticate(username=request.POST.get('username'),password=request.POST.get('password'))
            if c_user is not None:
                if c_user.is_active:
                    login(request, c_user)
                    # return render(request, 'index.html', {})
                    return redirect('dashboard')
                else:
                    # Return a 'disabled account' error message
                    return render(request, 'login.html', {'MSG':'Disable acccount'})
            else:
                #return redirect('index')        
                return render(request, 'login.html')
        elif request.method == 'GET':
            # open login page
            if request.user.username:
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {})
    except Exception:
        return render(request, 'login.html',{'msg':'Invalid Login'})
@login_required
def logout_view(request):
    logout(request)
    return redirect('login')

def signup(request):

    try:
        if request.method == "POST":
            print(request.POST)
            if request.POST.get('password') == request.POST.get('confirmpassword'):
                user = User(
                    username = request.POST.get('username'),
                    email = request.POST.get('email'),
                    first_name = request.POST.get('firstname'),
                    last_name = request.POST.get('lastname')
                )
                user.set_password(request.POST.get('password'))
                user.save()
                profile = Profile(user=user)
                profile.save()
                notification_log = NotificationLog(user=user)
                notification_log.save()
                return  redirect('login')
            else:
                return JsonResponse({"message":"Password did not match"})
        elif request.method == "GET":
            if request.user.username:
                return redirect('dashboard')
            else:
                return render(request,'signup.html',{})
    except Exception:
        return render(request,'signup.html',{'message':'username already exists'})