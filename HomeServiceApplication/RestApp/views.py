from django.shortcuts import render
from httplib2 import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from .serializers import UserCreationSerializer,addWorkSerializer
from rest_framework.response import Response#
from rest_framework import status
from django.http import Http404
from Homeapp.models import addWork
# Create your views here.

#@api_view(['GET', 'POST'])

class UserView(APIView):
    def get(self,request):
        user=User.objects.all()
        serializer=UserCreationSerializer(user,many=True)
        return Response(serializer.data)
    def post(self,request):
        serializer=UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    # def put(self,request):
    #     serializer = UserCreationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    #
    # def patch(self,request):
    #     serializer = UserCreationSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserDetails(APIView):
    def get_object(self,pk):
        try:
            return User.objects.get(email=pk)
        except:
            raise Http404

    def get(self,request,pk):
        user=self.get_object(pk)
        serializer=UserCreationSerializer(user)
        return Response(serializer.data)

    def put(self,request,pk):
        user = self.get_object(pk)
        serializer = UserCreationSerializer(user,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)


        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        user=self.get_object(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class AddWork(APIView):
    def get_object(self,pk):
        try:
            return addWork.objects.filter(user=pk)
        except:
            raise Http404


    def get(self,request,pk):
        works=self.get_object(pk)
        serializer=addWorkSerializer(works,many=True)
        return Response(serializer.data)
    def post(self,request,pk):
        serializer=addWorkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class EditWork(APIView):
    def get_object(self,pk):
        try:
            return addWork.objects.get(id=pk)
        except:
            raise Http404

    def get(self,request,pk):
        work=self.get_object(pk)
        serializer=addWorkSerializer(work)
        return Response(serializer.data)



    def put(self,request,pk):
        work=self.get_object(pk)
        serializer=addWorkSerializer(work,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)