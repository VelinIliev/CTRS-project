from django.urls import path

from CTRS_course_project.reservation.views import create_reservation, \
    ReservationStep1View, ReservationStep2View, ReservationDetailsView, save_projection

urlpatterns = [
    path('start/', create_reservation, name='start reservation'),
    path('save/<int:pk>/', save_projection, name='save projection'),
    path('step1/', ReservationStep1View.as_view(), name='reservation step 1'),
    path('step2/', ReservationStep2View.as_view(), name='reservation step 2'),
    path('review/<int:pk>/', ReservationDetailsView.as_view(), name='reservation review'),
]
