from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Director(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0},{1},{2}'.format(self.name, self.last_name, self.age)


class Actor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField()

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0},{1},{2}'.format(self.name, self.last_name, self.age)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title =models.CharField(max_length=50)
    poster = models.ImageField(default=None)
    duration_q = models.IntegerField()
    detail = models.TextField(default=None)
    trailer_url = models.URLField(default=None)
    director = models.ForeignKey('Director',on_delete=models.SET_NULL,null=True)
    actor = models.ForeignKey('Actor',on_delete=models.SET_NULL,null=True)
    select_gender = (
        (1,'Accion'),
        (2,'Romantic'),
        (3,'Scient Ficcion'),
        (4,'Humor'),
    )
    gender = models.CharField(max_length=1, choices=select_gender,blank=True)
    lenguage = models.CharField(max_length=50)
    date = models.DateField(default=None)
    country = models.CharField(max_length=30,default=None)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}'.\
            format(self.title, self.duration, self.poster,self.detail,self.trailer_url,
                   self.gender,self.lenguage,self.date,self.country,
                   self.director,self.actor)


class MovieRaiting(models.Model):
    id = models.AutoField(primary_key=True)
    id_movie_name = models.ForeignKey('Movie',on_delete=models.SET_NULL,null=True)
    id_user_django = models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    comment = models.TextField(max_length=400 , default=None)
    select_vote = (
        (1,'I Like'),
        (2, 'I Dont Like'),
    )
    vote = models.CharField(max_length=1, choices=select_vote,blank=True, default=None)

    class Meta:
        ordering = ['comment']

    def __str__(self):
        return '{0},{1},{2},{3}'.format(self.comment,self.vote,self.id_movie_name,self.id_user_django)