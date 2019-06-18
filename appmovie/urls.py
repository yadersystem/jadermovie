from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from JaderMovie import settings
from appmovie.views import MovieRateListView, MovieRateDetailView, MovieRateCreateView, MovieRateUpdateView, \
    MovieRateDeleteView
from . import views

from django.contrib.auth.views import login_required

urlpatterns = [
    #path('', views.index, name='index'),
    path('', views.MovieList.as_view(), name='index'),
    path('description', views.description, name='description'),
    path('search',views.search,name='search'),
    path('registeruser',views.CreateUser.as_view(),name='registeruser'),
    path('admin',views.UserList.as_view(),name='UserList'),
    path('admin/<int:pk>/EditUser',views.UpdateUser.as_view(),name='UpdateUser'),
    path('admin/<int:pk>/deleteuser',views.DeleteUser.as_view(),name='deleteuser'),

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('api/', views.MovieListView.as_view(), name='apimovie'),
    path('api_detail/<int:id>',views.MovieDetailView.as_view(),name='api_detail'),
    path('movierate/',MovieRateListView.as_view(),name='drf-movierate-list'),
    path('movierate/<int:pk>/', MovieRateDetailView.as_view(), name='drf-movierate-detail'),
    path('movieratecreate',MovieRateCreateView.as_view(),name='drf-movierate-create'),
    path('movierateupdate/<int:pk>/',MovieRateUpdateView.as_view(),name='drf-movierate-update'),
    path('movieratedelete/<int:pk>/',MovieRateDeleteView.as_view(),name='drf-movierate-delete'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve, {'document_root' : settings.MEDIA_ROOT,}),
        #path('media/<path>.*',serve,{'document_root' : settings.MEDIA_ROOT,})
    ]