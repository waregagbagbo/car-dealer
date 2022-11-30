from django.contrib import admin
from django.urls import path
from accounts.views import LoginView, RegistrationView
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', LoginView.as_view(), name='login_user'),
    path('register/', RegistrationView.as_view(), name='register'),   
    
    # authentication urls
     path('password_reset',auth_views.PasswordResetView.as_view(template_name="accounts/password_reset_form.html"),\
         name='password_reset'),

     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="accounts/password_reset_confirm_form.html"),\
         name='password_reset_confirm'),

    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name="accounts/password_reset_done.html"),\
         name='password_reset_done'),
    
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_complete.html"),\
         name='password_reset_complete'),     
    
    
]