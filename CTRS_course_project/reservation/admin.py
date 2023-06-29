from django.contrib import admin

from CTRS_course_project.reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    ...
