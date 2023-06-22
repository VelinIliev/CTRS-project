from django.urls import path, include

from CTRS_course_project.projection.views import index, CreateProjectionView, DisplayProjectionView, \
    DetailsProjectionView, reservations

urlpatterns = [
    path('', DisplayProjectionView.as_view(), name='projection index'),
    path('add/', CreateProjectionView.as_view(), name='add projection'),
    path('details/<int:pk>/<str:slug>/', DetailsProjectionView.as_view(), name='details projection'),
    path('reservations/', reservations, name='reservations'),
]
