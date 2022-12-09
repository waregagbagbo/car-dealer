from django.contrib.auth import views as auth_views
from django.views.generic import  CreateView, TemplateView
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'acc_pages/login.html'
        
    #def form_valid(self,form):
        #remember_me = form.cleaned_data['remember_me']
        #if not remember_me:
            #self.request.session.set_expiry(0)
            #self.request.session.modified = True
           
      
     

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'acc_pages/register.html'
    success_url = reverse_lazy('login')


 
class LogoutView(TemplateView):
    template_name = "acc_pages/logout.html"