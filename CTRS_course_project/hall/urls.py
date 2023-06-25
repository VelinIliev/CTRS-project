from django.urls import path

from CTRS_course_project.hall.views import CreateHallView, DisplayHallView, HallDetailsView, EditHallView, \
    DeleteHallView

urlpatterns = [
    path('', DisplayHallView.as_view(), name='hall index'),
    path('add/', CreateHallView.as_view(), name='add hall'),
    path('details/<int:pk>/<str:slug>/', HallDetailsView.as_view(), name='details hall'),
    path('edit/<int:pk>/<str:slug>/', EditHallView.as_view(), name='edit hall'),
    path('delete/<int:pk>/<str:slug>/', DeleteHallView.as_view(), name='delete hall'),
]
