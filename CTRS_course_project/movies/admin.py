from django.contrib import admin

from CTRS_course_project.movies.forms import CreateMovieForm
from CTRS_course_project.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'is_active']
    list_filter =["year", "is_active"]
    ordering = ['year', 'title']
    search_fields = ['title', ]