from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
#from appmovie.forms import UserForm
from appmovie.forms import UserForm
from appmovie.models import Movie
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from django.core.urlresolvers import reverse_lazy


def index(request):

    return render(request,'appmovie/index.html')


def login(request):

    return render(request,'appmovie/login.html')


def description(request):
    #model = Movie
    return render(request,'appmovie/description.html')


def search(request):
    return render(request,'appmovie/search.html')


class CreateUser(CreateView):
    model = User
    template_name = 'appmovie/RegisterUser.html'
    form_class = UserForm
    success_url = reverse_lazy('appmovie:login')

    def form_invalid(self, form):
        print(form.errors)
        return super(CreateUser, self).form_invalid(form)


class UserList(ListView):
    model = User
    template_name = 'appmovie/admin.html'


class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'appmovie/EditUser.html'
    success_url = reverse_lazy('appmovie:UserList')


class DeleteUser(DeleteView):
    model = User
    template_name = 'appmovie/deleteuser.html'
    success_url = reverse_lazy('appmovie:UserList')