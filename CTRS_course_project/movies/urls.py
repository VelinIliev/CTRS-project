from django.contrib.auth.decorators import login_required
from django.urls import path

from CTRS_course_project.movies.views import CreateMovieView, DisplayMoviesView, \
    DisplayMovieDetailsView, EditMovieView

urlpatterns = [
    path('', DisplayMoviesView.as_view(), name='movies'),
    path('add/', CreateMovieView.as_view(), name='add movie'),
    path('details/<int:pk>/', DisplayMovieDetailsView.as_view(), name='details movie'),
    path('edit/<int:pk>/', EditMovieView.as_view(), name='edit movie'),
]
