from django.contrib import admin
from django.urls import path
from accounts.views import UserLoginView, RegistrationView,LogoutView
from django.contrib.auth import views as auth_views
app_name ='accounts'

urlpatterns = [
    path('login', UserLoginView.as_view(), name='login'),
    path('register/', RegistrationView.as_view(), name='register'),   
    path('logout', LogoutView.as_view(), name='sign_out'),  
    
    # authentication urls
     path('password_reset',auth_views.PasswordResetView.as_view(template_name="acc_pages/password_reset_form.html"),\
         name='password_reset'),

     path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="acc_pages/password_reset_confirm_form.html"),\
         name='password_reset_confirm'),

    path('password_reset_done',auth_views.PasswordResetDoneView.as_view(template_name="acc_pages/password_reset_done.html"),\
         name='password_reset_done'),
    
    path('password_reset_complete',auth_views.PasswordResetCompleteView.as_view(template_name="acc_pages/password_reset_complete.html"),\
         name='password_reset_complete'),     
    
    
]
