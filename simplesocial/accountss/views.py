from django.shortcuts import render
#from accountss.forms import UserCreateForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
# Create your views here.
from . import forms

class SignUp(CreateView):
    form_class  = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accountss/signup.html'
