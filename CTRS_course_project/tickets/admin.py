from django.contrib import admin

from CTRS_course_project.tickets.models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_type', 'price', 'weekend_price']

