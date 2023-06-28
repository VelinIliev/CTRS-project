from django.urls import path

from CTRS_course_project.reservation.views import create_reservation, \
    ReservationStep1View, ReservationStep2View, ReservationDetailsView

urlpatterns = [
    # path('', index_reservation, name='index reservation'),
    path('start/', create_reservation, name='start reservation'),
    path('<int:pk>/step1/', ReservationStep1View.as_view(), name='reservation step 1'),
    path('<int:pk>/step2/', ReservationStep2View.as_view(), name='reservation step 2'),
    path('<int:pk>/review/', ReservationDetailsView.as_view(), name='reservation review'),
]
