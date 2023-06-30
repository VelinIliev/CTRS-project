from django.contrib import admin

from CTRS_course_project.reservation.models import Reservation


@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ['date', 'user', 'projection', 'is_finished']
    list_filter = ['is_finished', 'date']
    ordering = ['date', 'user']
    search_fields = ['user__username', ]

