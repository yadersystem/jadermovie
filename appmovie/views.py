from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView
from appmovie.models import Movie


def index(request):

    return render(request,'appmovie/index.html')


def login(request):

    return render(request,'appmovie/login.html')


'''class ListMovie(ListView):
    model = Movie
    template_name = 'moviesfull.html'
    #form_class = ServiceForm
    success_url = reverse_lazy('appmovie:moviesfull')'''
