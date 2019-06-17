from django.db import models
from django.contrib.auth import get_user_model
from appmovie.queryset import MovieRateQueryset

User = get_user_model()


def movie_directory_path(instance, filename):
    return f'{instance.meta.app_label}/img/{instance.title}/{filename}'


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0}'.format(self.name)


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0}'.format(self.name)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(max_length=20)
    poster = models.ImageField(upload_to=movie_directory_path)
    duration_q = models.IntegerField()
    detail = models.TextField(default=None)
    trailer_url = models.URLField(null=True, blank=True)
    director = models.ForeignKey('Director',on_delete=models.SET_NULL,null=True)
    actor = models.ForeignKey('Actor',on_delete=models.SET_NULL,null=True)
    gender = models.CharField(max_length=20)
    lenguage = models.CharField(max_length=20)
    year = models.IntegerField(default=None)
    country = models.CharField(max_length=20,default=None)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '{0}'.\
            format(self.title)

    @property
    def meta(self):
        return self._meta


class MovieRaiting(models.Model):
    id = models.AutoField(primary_key=True)
    movie = models.ForeignKey('Movie',on_delete=models.SET_NULL,null=True)
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment = models.TextField(max_length=400 , default=None)
    select_vote = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )
    vote = models.FloatField(choices=select_vote,blank=True, default=None)

    objects = MovieRateQueryset.as_manager()

    class Meta:
        unique_together = ('user', 'movie')
        permissions = (
            ('can_vote_two_times', 'Can vote two times'),
        )

    def __str__(self):
        return f'{self.user} : {self.vote}'