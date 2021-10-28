from django import forms
from django.contrib.auth.forms import UserCreationForm , UserChangeForm
# from django.contrib.auth import forms
# from django import forms
from django.contrib.auth.models import User
from django.db import models
from django.db.models import fields

class signupform(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email']

class userdetailForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
