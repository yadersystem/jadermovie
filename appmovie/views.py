import secrets
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse, request, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.base import View
from django.views.generic.list import BaseListView
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.renderers import JSONRenderer

from appmovie.api.permissions import IsAuthenticatedOrReadOnlyCustom
from appmovie.api.serializers import MovieSerializer, MovieRaitingSerializer, MovieRaitingSerializerCreate, \
    MovieRaitingSerializerUpdate, MovieRaitingSerializerAll
from appmovie.forms import UserForm, SimpleData
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from appmovie.models import Movie, MovieRaiting,Token
from appmovie.tasks import SearchMovieWebs
from appmovie.queryset import MovieRateQueryset



def index(request):
    return render(request, 'appmovie/index.html')


def login(request):
    return render(request, 'appmovie/registration/login.html')


def search(request):
    return render(request, 'appmovie/search.html')


#def searchcelery(request):
    #return render(request,'appmovie/searchcelery.html')


#def searchceleryresult(request):
 #   return render(request, 'appmovie/searchceleryresult.html')

class Searchceleryresult(DetailView):

    def __init__(self):
        self.template_name = 'appmovie/searchceleryresult.html'
        self.form_class = SimpleData

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'form':SimpleData})

    def post(self, request):
        my_form = SimpleData(request.POST)
        if my_form.is_valid():
            my_title = my_form.cleaned_data['title']
            my_reciver = my_form.cleaned_data['email']
            my_list_movie = my_title.split(", ")
            #SearchMovieWebs.delay(my_title)
            SearchMovieWebs.s(my_list_movie, my_reciver)
        return HttpResponseRedirect(reverse_lazy('appmovie:index'))


class CreateUser(CreateView):
    model = User
    template_name = 'appmovie/RegisterUser.html'
    form_class = UserForm
    success_url = reverse_lazy('appmovie:login')


class UserList(ListView):
    model = User
    template_name = 'appmovie/admin.html'


class description(DetailView):
    queryset = Movie.objects.all()
    template_name = 'appmovie/description.html'


class DescriptionRaiting(DetailView):
    queryset = MovieRaiting.objects.all()
    template_name = 'appmovie/description.html'


class UpdateUser(UpdateView):
    model = User
    form_class = UserForm
    template_name = 'appmovie/EditUser.html'
    success_url = reverse_lazy('appmovie:UserList')


class DeleteUser(DeleteView):
    model = User
    template_name = 'appmovie/deleteuser.html'
    success_url = reverse_lazy('appmovie:UserList')


class MovieList(ListView):
    model = Movie
    template_name = 'appmovie/index.html'
    queryset = Movie.objects.all()

    '''def get_queryset(self):
        qs = super(MovieList, self).get_queryset()
        return qs

    def get_context_data(self, **kwargs):
        data = super(MovieList, self).get_context_data(**kwargs)
        best_movie = MovieRaiting.id

        if best_movie:
            movie = Movie.objects.get(pk = best_movie.get('vote'))
            data.update({
                'best_rated_movie' : movie,
                'best_rated_value' : best_movie.get('vote',0),
            })
            return data'''


class MovieListView(BaseListView):

    model = Movie
    content_type = 'application/json'
    response_class = HttpResponse

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieListView, self).get_context_data(object_list=object_list, **kwargs)
        context.update({'serialized_data': MovieSerializer(self.get_queryset(), many=True).data})
        return context

    def render_to_response(self, context, **response_kwargs):
        response_kwargs.setdefault('content_type', self.content_type)
        response = JSONRenderer().render(context.get('serialized_data'))
        return self.response_class(response, content_type=self.content_type)


class MovieDetailView(DetailView):
    model = Movie
    pk_url_kwarg = 'id'

    def get_context_data(self, object = None, *kwarg,**kwargs):
        context = super(MovieDetailView, self).get_context_data(object=object, **kwargs)
        context.update({'object': self.get_object()})
        return context

    def render_to_response(self, context, **response_kwargs):
        response = JSONRenderer().render(MovieSerializer(context.get('object','')).data)
        return HttpResponse(response,content_type=self.content_type)


class MovieRateListView(ListAPIView):
    queryset = MovieRaiting.objects.all()
    serializer_class = MovieRaitingSerializer


class MovieRateDetailView(RetrieveAPIView):
    queryset = MovieRaiting.objects.all()
    serializer_class = MovieRaitingSerializer


class MovieRateCreateView(CreateAPIView):
    queryset = MovieRaiting.objects.all()
    serializer_class = MovieRaitingSerializerCreate


class MovieRateUpdateView(UpdateAPIView):
    queryset = MovieRaiting.objects.all()
    serializer_class = MovieRaitingSerializerUpdate


class MovieRateDeleteView(DestroyAPIView):
    queryset = MovieRaiting.objects.all()
    serializer_class = MovieRaitingSerializer


class MovieRaitingSerializerAllAll(viewsets.ModelViewSet):
    queryset = MovieRaiting.objects.all()
    serializer_class = MovieRaitingSerializerAll
    permission_classes = [IsAuthenticatedOrReadOnlyCustom]


class Login(LoginView):
    template_name = 'login.html'

    def form_valid(self, form):
        contex = super(Login,self).form_valid(form)
        try:
            token = Token.objects.get(user=self.request.user.pk)
        except:
            token = Token.obejects.create(user=self.request.user,token=secrets.token_hex())
        return contex


class LogOutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        try:
            Token.objects.get(user=self.request.user.pk).delete()
        except:
            return redirect('admin')
        logout(request)
        return super(LogOutView,self).dispatch(request,*args,**kwargs)


