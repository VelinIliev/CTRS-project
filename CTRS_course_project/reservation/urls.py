from django.urls import path

from CTRS_course_project.reservation.views import index_reservation, create_reservation, reservation_step1, \
    ReservationStep1View, ReservationStep2View, reservation_review, ReservationDetailsView

urlpatterns = [
    path('', index_reservation, name='index reservation'),
    path('start/<int:pk>/', create_reservation, name='start reservation'),
    path('<int:pk>/step1/', ReservationStep1View.as_view(), name='reservation step 1'),
    path('<int:pk>/step2/', ReservationStep2View.as_view(), name='reservation step 2'),
    path('<int:pk>/review/', ReservationDetailsView.as_view(), name='reservation review'),
]
