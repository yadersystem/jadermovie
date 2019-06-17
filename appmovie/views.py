from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic.list import BaseListView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.renderers import JSONRenderer
from appmovie.api.serializers import MovieSerializer,MovieRaitingSerializer
from appmovie.forms import UserForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from appmovie.models import Movie, MovieRaiting


def index(request):
    return render(request, 'appmovie/index.html')


def login(request):
    return render(request, 'appmovie/registration/login.html')


def description(request):
    # model = Movie
    return render(request, 'appmovie/description.html')


def search(request):
    return render(request, 'appmovie/search.html')


class CreateUser(CreateView):
    model = User
    template_name = 'appmovie/RegisterUser.html'
    form_class = UserForm
    success_url = reverse_lazy('appmovie:login')


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


class MovieList(ListView):
    model = Movie
    template_name = 'appmovie/index.html'


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
