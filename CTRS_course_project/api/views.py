import datetime

from rest_framework import generics as rest_views
from rest_framework.exceptions import APIException

from CTRS_course_project.api.serialezers import MovieSerializer, ProjectionSerializer
from CTRS_course_project.movies.models import Movie
from CTRS_course_project.projection.models import Projection


class InvalidDateException(APIException):
    status_code = 400
    default_detail = 'Invalid date format. Date format must be: DD-MM-YYYY'
    default_code = 'invalid_date'


class MoviesListApiView(rest_views.ListAPIView):
    serializer_class = MovieSerializer

    def get_queryset(self):
        queryset = Movie.objects.filter()

        movie_title = self.request.query_params.get('title')
        movie_year = self.request.query_params.get('year')

        if movie_title:
            queryset = queryset.filter(title__icontains=movie_title)

        if movie_year:
            queryset = queryset.filter(year=movie_year)

        return queryset


class MovieApiView(rest_views.RetrieveAPIView):
    serializer_class = MovieSerializer
    lookup_url_kwarg = 'movie_id'
    queryset = Movie.objects.all()


class ProjectionListApiView(rest_views.ListAPIView):
    serializer_class = ProjectionSerializer

    def get_queryset(self):
        queryset = Projection.objects.filter().order_by('date', 'hour')

        today = datetime.datetime.now().date()
        movie_id = self.request.query_params.get('movie_id')
        movie_title = self.request.query_params.get('movie_title')
        start = self.request.query_params.get('start')
        end = self.request.query_params.get('end')

        if movie_id:
            queryset = queryset.filter(movie_id=movie_id)

        if movie_title:
            queryset = queryset.filter(movie__title__icontains=movie_title)

        if start:
            try:
                start = datetime.datetime.strptime(start, "%d-%m-%Y").date()
            except (ValueError,):
                raise InvalidDateException()
            queryset = queryset.filter(date__gte=start)
        else:
            queryset = queryset.filter(date__gte=today)

        if end:
            try:
                end = datetime.datetime.strptime(end, "%d-%m-%Y").date()
            except (ValueError,):
                raise InvalidDateException()
            queryset = queryset.filter(date__lte=end)
        else:
            queryset = queryset.filter(date__gte=today)

        return queryset


class ProjectionByDateListApiView(rest_views.ListAPIView):
    serializer_class = ProjectionSerializer
    lookup_url_kwarg = 'projection_date'

    def get_queryset(self):
        try:
            date = datetime.datetime.strptime(self.kwargs.get('projection_date'), "%d-%m-%Y").date()
        except ValueError:
            raise InvalidDateException()

        queryset = Projection.objects.filter(date=date).order_by('movie', 'hour')
        return queryset
