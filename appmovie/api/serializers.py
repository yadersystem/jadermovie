from django.contrib.auth.models import User, Group
from rest_framework import serializers
from appmovie.models import Movie, MovieRaiting


class MovieSerializer(serializers.Serializer):
    title= serializers.CharField()
    duration_q = serializers.IntegerField()
    director = serializers.CharField()
    actor = serializers.CharField()

    def get_movie_rate(self,obj):
        rates=MovieRaiting.objects.filter(movie__pk=obj)
        if rates.exists():
            return rates.first()['rate']

        return ''


class MovieRaitingSerializer(serializers.ModelSerializer):
    id = serializers.HyperlinkedIdentityField(view_name='appmovie:drf-movierate-detail')
    user = serializers.StringRelatedField()
    movie = serializers.HyperlinkedIdentityField(read_only=True,view_name='appmovie:drf-movierate-detail',lookup_field='pk')

    class Meta:
        model = MovieRaiting
        fields = ('movie','user','vote','id')


class MovieRaitingSerializerCreate(serializers.ModelSerializer):

    class Meta:
        model=MovieRaiting
        fields = ('movie','user','vote','comment')


class MovieRaitingSerializerUpdate(serializers.ModelSerializer):

    class Meta:
        model=MovieRaiting
        fields = ('movie','vote','comment')


class MovieRaitingSerializerDelete(serializers.ModelSerializer):

    class Meta:
        model = MovieRaiting
        field = ('id')


class MovieRaitingSerializerAll(serializers.ModelSerializer):
    class Meta:
        model = MovieRaiting
        fields = '__all__'
