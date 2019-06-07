from django.db import models


class Cargo(models.Model):
    id = models.AutoField(primary_key=True)
    roll=models.CharField(max_length=50)

    class Meta:
        ordering = ['roll']

    def __str__(self):
        return '{0}'.format(self.roll)


'''class Person(models.Model):
    id = models.AutoField(primary_key=True)
    id_roll = models.ForeignKey('Cargo', on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(max_length=3)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return '{0},{1},{2},{3}'.format(self.name, self.last_name, self.age,self.id_roll)


class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    id_movie = models.ForeignKey('Person',on_delete=models.SET_NULL,null=True)
    title =models.CharField(max_length=50)
    duration =models.TimeField()
    poster = models.ImageField(upload_to='/home/jader/Escritorio/LSV-TECH/Luis/jadermovie/appmovie/img')
    detail = models.TextField(max_length=400)
    trailer_url = models.URLField(max_length=200)
    director = models.ForeignKey('Person',on_delete=models.SET_NULL,null=True)
    actor = models.ForeignKey('Person',on_delete=models.SET_NULL,null=True)
    select_gender = (
        (1,'Accion'),
        (2,'Romantic'),
        (3,'Scient Ficcion'),
        (4,'Humor'),
    )
    gender = models.CharField(max_length=1, choices=select_gender,blank=True)
    lenguage = models.CharField(max_length=30)
    date = models.DateField()
    country = models.CharField(max_length=30)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return '{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10},{11}'.\
            format(self.title, self.duration, self.poster,self.detail,self.trailer_url,
                   self.gender,self.lenguage,self.date,self.country,
                   self.id_movie,self.director,self.actor)


class MovieRaiting(models.Model):
    id = models.AutoField(primary_key=True)
    id_movie_name = models.ForeignKey('Movie',on_delete=models.SET_NUL,null=True)
    id_user_django = models.ForeignKey('auth_user',on_delete=models.SET_NULL,null=True)
    comment = models.TextField(max_length=400)
    select_vote = (
        (1,'I Like'),
        (2, 'I Dont Like'),
    )
    vote = models.CharField(max_length=1, choices=models.SET_NULL,null=True)

    class Meta:
        ordering = ['id_movie_name']

    def __str__(self):
        return '{0},{1},{2},{3}'.\
            format(self.id_movie_name, self.id_user_django, self.comment,self.vote)'''