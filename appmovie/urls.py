from django.conf.urls import url
from django.urls import path
from django.views.static import serve
from JaderMovie import settings
from . import views
from appmovie.views import UserList


urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login, name='login'),
    path('description', views.description, name='description'),
    path('search',views.search,name='search'),
    path('registeruser',views.CreateUser.as_view(),name='registeruser'),
    path('admin',views.UserList.as_view(),name='UserList'),
    path('admin/<int:pk>/EditUser',views.UpdateUser.as_view(),name='UpdateUser'),
    path('admin/<int:pk>/deleteuser',views.DeleteUser.as_view(),name='deleteuser'),
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve, {'document_root' : settings.MEDIA_ROOT,}),
        #path('media/<path>.*',serve,{'document_root' : settings.MEDIA_ROOT,})
    ]