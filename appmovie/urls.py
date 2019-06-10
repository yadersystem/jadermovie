from django.conf.urls import url
from django.urls import path
from django.views.static import serve
from JaderMovie import settings
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login.html',views.login, name='login'),
    #path('description.html', views.description, name='description')
]

if settings.DEBUG:
    urlpatterns += [
        url(r'^media/(?P<path>.*)$',serve, {'document_root' : settings.MEDIA_ROOT,}),
        #path('media/<path>.*',serve,{'document_root' : settings.MEDIA_ROOT,})
    ]