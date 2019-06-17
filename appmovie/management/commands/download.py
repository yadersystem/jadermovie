import requests
from django.core.files.storage import FileSystemStorage
from django.core.management.base import BaseCommand
from pprint import pprint


from appmovie.models import Movie, Actor,Director


class Command(BaseCommand):
    help = 'fetch movie from OMDB API'

    def add_arguments(self, parser):
        #positional arguments
        parser.add_argument('title',type=str)

        #kwars likes arguments
        parser.add_argument('-s','--search',action='store_true',default=False)

    def handle(self, *args, **options):
        search = options['search']
        title = options['title']
        #print(search)
        #print(title)

        #url = 'http://www.omdbapi.com/?t=' + title + '&plot=full&apikey=9ab58ab8&type=movie'
        #peli = requests.get(url)

        #pprint(peli.json())

        if search:
            url = 'http://www.omdbapi.com/?s='+title+'&plot=full&apikey=9ab58ab8&type=movie'
            list=requests.get(url)

            for i in list.json()['Search']:
                pass

        else:
            url = 'http://www.omdbapi.com/?t='+title+'&plot=full&apikey=9ab58ab8&type=movie'
            peli = requests.get(url)

            '''@staticmethod
            def saveImage(title, poster_url):
                relativo = '/movie/'+ title+'/'
                fs = FileSystemStorage(location='media'+relativo)
                if poster_url != "N/A":
                    ext = poster_url[-3:]
                    mkdir(settings.MEDIA_ROOT+relativo)'''


            M = Movie.objects.get_or_create(
                title = peli.json()['Title'],
                duration_q = peli.json()['Runtime'].split(" ")[0],
                detail = peli.json()['Plot'],
                gender = peli.json()['Genre'].split(",")[0],
                lenguage = peli.json()['Language'].split(",")[0],
                year = peli.json()['Year'][0],
                country = peli.json()['Country'].split(",")[0],
                poster = peli.json()['Poster'][0],
                )

            a = Actor.objects.get_or_create(
                name=peli.json()['Actors'].split(",")[0]
            )

            d = Director.objects.get_or_create(
                name=peli.json()['Director'].split(",")[0]
            )



            m=peli.json()['Genre'].split(",")[0]
            #pprint(peli.headers['Title'])
            print(m)

