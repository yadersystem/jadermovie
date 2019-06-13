from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.views.generic import TemplateView
from django.views.static import serve
from JaderMovie import settings
from . import views

from django.contrib.auth.views import login_required

urlpatterns = [
    path('', views.index, name='index'),
    path('description', views.description, name='description'),
    path('search',views.search,name='search'),
    path('registeruser',views.CreateUser.as_view(),name='registeruser'),
    path('admin',views.UserList.as_view(),name='UserList'),
    path('admin/<int:pk>/EditUser',views.UpdateUser.as_view(),name='UpdateUser'),
    path('admin/<int:pk>/deleteuser',views.DeleteUser.as_view(),name='deleteuser'),
    #path(login,'template_name':'appmovie:login.html'},name = 'login')
    #path('',TemplateView.as_view(appmovie='login.html'),name='login'),
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve, {'document_root' : settings.MEDIA_ROOT,}),
        #path('media/<path>.*',serve,{'document_root' : settings.MEDIA_ROOT,})
    ]