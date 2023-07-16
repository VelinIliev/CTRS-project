from django.urls import path

from CTRS_course_project.projection.views import CreateProjectionView, DisplayProjectionView, \
    DetailsProjectionView, DisplayProjectionByDayView

urlpatterns = [
    path('', DisplayProjectionView.as_view(), name='projection index'),
    path('add/', CreateProjectionView.as_view(), name='add projection'),
    path('details/<int:pk>/<str:slug>/', DetailsProjectionView.as_view(), name='details projection'),
    path('<str:day>/', DisplayProjectionByDayView.as_view(), name='projection day'),
]
