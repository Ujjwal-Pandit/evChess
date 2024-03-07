from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
import django.views.generic as generic
"""
Bug: need to be fixed/ or approved
why does
from django.views.generic import CreateView

leads into an error when 

class SignUpView(generic.CreateView):

won't understand generic
"""


class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"
