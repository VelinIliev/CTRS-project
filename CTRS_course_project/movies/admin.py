from django.contrib import admin

from CTRS_course_project.movies.models import Movie


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    ...