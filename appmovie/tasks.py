from celery._state import get_current_app
from django.core.management import call_command
from JaderMovie.celery import app
from celery import Task

#app = get_current_app()


class Multiply(Task):
    name ='multiply_task'

    def run(self, x, y, *args, **kwargs):
        return x * y


app.register_task(Multiply())


'''@app.task
def multiply(x,y):
    print(x*y)

@app.task
def add(x,y):
    print(x+y)
    multiply.delay(x,y)
    return x+y'''

#------------------- Descargando la Pelicula --------------------------


@app.task
def send_email(receiver):
    send_email(
        'Te Envio la Informacion',
        'Las Peliculas son',
        'jyepez@lsv-tech.com',
        [receiver],
        fail_silently=False
    )


@app.task
def SearchMovieWebs(title,receiver):
    for title in title:
        call_command('download', title)
    send_email.delay(receiver)
