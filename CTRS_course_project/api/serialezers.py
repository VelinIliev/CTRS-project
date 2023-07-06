from rest_framework import serializers

from CTRS_course_project.hall.models import Hall
from CTRS_course_project.movies.models import Movie
from CTRS_course_project.projection.models import Projection


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title', 'year', 'image_url', 'runtime', 'plot', 'directors', 'writers',
                  'actors', 'genres', 'country', 'languages', 'contentRating', 'imbd_link', 'rating', 'votes')


class SingleMovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('id', 'title',)


class SingleHallSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hall
        fields = ('id', 'name')


class ProjectionSerializer(serializers.ModelSerializer):
    movie = SingleMovieSerializer()
    hall = SingleHallSerializer()

    class Meta:
        model = Projection
        fields = ('id', 'date', 'hour', 'movie', 'hall')
