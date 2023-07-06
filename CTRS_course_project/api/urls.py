from django.urls import path, include

from CTRS_course_project.api.views import MoviesListApiView, ProjectionListApiView, ProjectionByDateListApiView, \
    MovieApiView

urlpatterns = [
    path('movies/', MoviesListApiView.as_view(), name='movies list api'),
    path('movies/<int:movie_id>/', MovieApiView.as_view(), name='movies view api'),
    path('projections/', ProjectionListApiView.as_view(), name='projections list api'),
    path('projections/<str:projection_date>/', ProjectionByDateListApiView.as_view(),
         name='projections list by date api'),
]
