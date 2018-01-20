from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy
# Create your views here.

class SignUp(CreateView):
    form_class = forms.NewUserForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')
