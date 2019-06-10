from django.contrib import admin
from .models import Director, Actor, Movie, MovieRaiting


admin.site.register(Director)
admin.site.register(Actor)
admin.site.register(Movie)
admin.site.register(MovieRaiting)
