from django.urls import include, path

from django.conf.urls import url

from userapp.views import login_view, profile, signup, logout_view,editprofile,update_profile,changepassword

from django.contrib.auth import views

urlpatterns = [
    path('login', login_view, name='login'),
    
    path('password_reset/', views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    
    path('signup',signup, name='signup'),
    
    path('profile/',profile, name='profile'),
    
    path('editprofile/',editprofile, name='editprofile'),
    
    path('updateprofile',update_profile, name='updateprofile'),
    
    path('changepassword',changepassword, name='changepassword'),
    
    path('logout', logout_view, name='logout'),
    
]