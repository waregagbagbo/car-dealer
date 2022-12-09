from django.contrib.auth import views as auth_views
from django.views.generic import  CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from .forms import LoginForm, RegisterForm
from django.http import HttpResponseRedirect


class UserLoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'acc_pages/login.html'
    success_url = reverse_lazy('home')
    redirect_field_name = reverse_lazy('home')

    
    def form_valid(self,form):
        remember_me = form.cleaned_data['remember_me']
        if not remember_me:
            self.request.session.set_expiry(0)
            self.request.session.modified = True
            return HttpResponseRedirect(self.get_success_url())
      
     

class RegistrationView(CreateView):
    form_class = RegisterForm
    template_name = 'acc_pages/register.html'
    success_url = reverse_lazy('login')
