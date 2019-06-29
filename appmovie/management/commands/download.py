from os import mkdir
import re
import requests
from django.core.files import File
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand
from django.conf import settings
from appmovie.models import *


class Command(BaseCommand):
    help = 'fetch movie from OMDB API'

    def add_arguments(self, parser):
        #positional arguments
        parser.add_argument('title', type=str)

        #kwars likes arguments
        parser.add_argument('-s', '--search', action='store_true', default=False)

    def handle(self, *args, **options):
        """
            para descargar las peliculas
        """
        search = options['search']
        title = options['title']

        if search:
            url = 'http://www.omdbapi.com/?t=' + title + '&plot=full&apikey=9ab58ab8&type=movie'
            list = requests.get(url)

            for i in list.json()['Search']:
                codigo = i['imdbID']
                l_url = 'http://www.omdbapi.com/?i=' + codigo + '&apikey=9ab58ab8&type=movie'
                Command.saveMovie(l_url)
        else:
            url = 'http://www.omdbapi.com/?t=' + title + '&plot=full&apikey=9ab58ab8&type=movie'
            if Command.saveMovie(url):
                return str(title)
            else:
                return 'no se pudo descargar la pelicula ' + str(title)


    @staticmethod
    def saveMovie(url):
        peli = requests.get(url)
        M = Movie.objects.get_or_create(
            title=peli.json()['Title'],
            duration_q=peli.json()['Runtime'].split(" ")[0],
            detail=peli.json()['Plot'],
            gender=peli.json()['Genre'].split(",")[0],
            lenguage=peli.json()['Language'].split(",")[0],
            year=peli.json()['Year'][0],
            country=peli.json()['Country'].split(",")[0],
            poster=Command.saveImage(peli.json()['Poster'], re.sub('[^a-zA-Z0-9]', '', peli.json()['Title'])),
        )

        a = Actor.objects.get_or_create(
            name=peli.json()['Actors'].split(",")[0]
        )

        d = Director.objects.get_or_create(
            name=peli.json()['Director'].split(",")[0]
        )

    @staticmethod
    def saveImage(poster_url, title):
        relativo = '/appmovie/' + title + '/'
        fs = FileSystemStorage(location='media' + relativo)
        if poster_url != "N/A":
            ext = poster_url[-3:]
            mkdir(settings.MEDIA_ROOT + relativo)
            up_file = requests.get(poster_url)
            my_file = File(open(settings.MEDIA_ROOT + relativo + 'myImage.' + ext, 'wb'))
            my_file.name = 'myImage,' + ext
            my_file.write(up_file.content)
        else:
            my_file = File(open('media/myImage.jpg', 'rb'))
            my_file.name = 'myImage.jpg'
            fs.save(my_file.name, my_file)

            my_file.close()
        return relativo + my_file.name