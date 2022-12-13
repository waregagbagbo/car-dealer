from django.contrib.auth import views as auth_views
from django.views.generic import  CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'acc_pages/login.html'      
      
       

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'acc_pages/register.html'
    success_url = reverse_lazy('accounts:login')    
    
    def form_valid(self, form):        
        return super(RegistrationView,self).form_valid(form)
    
    
    
    
    


 
class LogoutView(TemplateView):
    template_name = "acc_pages/logout.html"