from django.contrib.auth.decorators import login_required
from django.urls import path

from CTRS_course_project.movies.views import CreateMovieView, DisplayMoviesView, \
    DisplayMovieDetailsView, EditMovieView, VoteMovieView, EditCommentView, \
    DeleteComment


urlpatterns = [
    path('', DisplayMoviesView.as_view(), name='movies'),
    path('add/', CreateMovieView.as_view(), name='add movie'),
    path('details/<int:pk>/<str:slug>/', DisplayMovieDetailsView.as_view(), name='details movie'),
    path('edit/<int:pk>/<str:slug>/', EditMovieView.as_view(), name='edit movie'),
    path('vote/<int:pk>/<str:slug>/', VoteMovieView.as_view(), name='vote movie'),
    path('comment/<int:pk>/delete/', DeleteComment.as_view(), name='delete comment'),
    path('comment/<int:pk>/edit/', EditCommentView.as_view(), name='edit comment'),
]
