from django.http import HttpResponse
from django.shortcuts import render, redirect
from  django.contrib.auth.models import User
from .forms import RegistrationForm,LoginForm,AddSkillForm,AddWorkForm
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView,CreateView
from .models import skill,addSkill,addWork

# Create your views here.


class RegistrationView(TemplateView):
    model=User
    form_class=RegistrationForm
    template_name = "Homeapp/registeration.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("loginpage")
        else:
            self.context["form"] = form
            return render(request, self.template_name, self.context)


class loginView(TemplateView):
    model=User
    template_name = "Homeapp/login.html"
    form_class=LoginForm()
    context = {}
    def get(self, request, *args, **kwargs):
        self.context["form"] = self.form_class
        return render(request, self.template_name, self.context)
    def post(self, request, *args, **kwargs):
        form=LoginForm(request.POST)
        email=request.POST["email"]
        password=request.POST["password"]
        user=User.objects.get(email=email)
        uname=user.username
        print(uname)
        print(email,",",password)
        user=authenticate(username=uname,password=password)
        print(user)
        if user is not None:
            login(request,user)
            return redirect("index")
        else:
            print("login not success")
            return redirect("loginpage")



def indexpage(request):
    return render(request,"Homeapp/index.html")

class AddSkill(TemplateView):
    model=addSkill
    form_class=AddSkillForm
    template_name = "Homeapp/add_skill.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class(initial={'user':request.user})
        qs=self.model.objects.filter(user=request.user)
        self.context['skills']=qs
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form=AddSkillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addskill')

        else:
            return render(request,self.template_name,self.context)


class AddWork(TemplateView):
    model=addWork
    form_class= AddWorkForm
    template_name = "Homeapp/add_work.html"
    context={}
    def get(self, request, *args, **kwargs):
        self.context["form"]=self.form_class(initial={'user':request.user})
        qs=self.model.objects.filter(user=request.user)
        self.context['work']=qs
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        form=AddWorkForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addwork')
        else:
            return render(request,self.template_name,self.context)

class EditWork(TemplateView):
    model=addWork
    form_class=AddWorkForm
    template_name = "Homeapp/edit_work.html"
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.getQuery(id)
        form=AddWorkForm(instance=qs)
        self.context["form"]=form
        return render(request,self.template_name,self.context)

    def getQuery(self,id):
        return self.model.objects.get(id=id)
    def post(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.getQuery(id)
        form=AddWorkForm(instance=qs,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("addwork")
        else:
            return render(request,self.template_name,self.context)


class DeleteWork(TemplateView):
    model=addWork
    template_name = "Homeapp/deletework.html"
    form_class=AddWorkForm
    context={}
    def get(self, request, *args, **kwargs):
        id=kwargs.get("pk")
        qs=self.model.objects.get(id=id)
        self.context["form"]=AddWorkForm(instance=qs)
        return render(request,self.template_name,self.context)
    def post(self, request, *args, **kwargs):
        id = kwargs.get("pk")
        qs = self.model.objects.get(id=id)
        qs.delete()
        return redirect("addwork")
