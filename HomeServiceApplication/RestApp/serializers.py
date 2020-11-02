from django.contrib.auth.models import User
from rest_framework import serializers
from Homeapp.models import addWork



class UserCreationSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","email","password"]

class addWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=addWork
        fields="__all__"