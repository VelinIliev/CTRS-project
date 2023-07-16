from django.contrib import admin

from CTRS_course_project.movies.models import Movie, MovieComment


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['title', 'year', 'is_active']
    list_filter = ["year", "is_active"]
    ordering = ['year', 'title']
    search_fields = ['title', ]


@admin.register(MovieComment)
class MovieCommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'movie', 'text']
    list_filter = ["movie"]
    ordering = ['publication_date_and_time']
    search_fields = ['user__username', 'movie__title', 'text']
