from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import skill,addSkill,addWork,WorkResponses


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['first_name','last_name','email','username','password1','password2']

class LoginForm(forms.Form):
    email=forms.CharField(max_length=100)
    password=forms.CharField(widget=forms.PasswordInput)

class AddSkillForm(ModelForm):
    class Meta:
        model=addSkill
        fields="__all__"
        widgets={
            'user':forms.HiddenInput()
        }

class AddWorkForm(ModelForm):
    class Meta:
        model=addWork
        fields="__all__"
        widgets={
            'user':forms.HiddenInput()
        }


class WorkResponseForm(ModelForm):
    class Meta:
        model=WorkResponses
        fields="__all__"
        widgets={
            'workid': forms.HiddenInput(),
            'user':forms.HiddenInput()

        }

class WorkAssignForm(ModelForm):
    class Meta:
        model=addWork
        fields=["workstatus"]
