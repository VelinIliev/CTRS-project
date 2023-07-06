from django.urls import reverse
from rest_framework import serializers

from CTRS_course_project.hall.models import Hall
from CTRS_course_project.movies.models import Movie
from CTRS_course_project.projection.models import Projection


class SingleMovieSerializer(serializers.ModelSerializer):
    link = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = ('id', 'title', 'link')

    @staticmethod
    def get_link(movie):
        return reverse('movies view api', args=[movie.id], )


class SingleHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ('id', 'name')


class ProjectionSerializer(serializers.ModelSerializer):
    movie = SingleMovieSerializer()
    hall = SingleHallSerializer()
    date = serializers.DateField(format="%d-%m-%Y")
    hour = serializers.TimeField(format="%H:%M")

    class Meta:
        model = Projection
        fields = ('id', 'date', 'hour', 'movie', 'hall')


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'image_url', 'runtime', 'plot', 'directors', 'writers',
                  'actors', 'genres', 'country', 'languages', 'contentRating', 'imbd_link', 'rating', 'votes')
