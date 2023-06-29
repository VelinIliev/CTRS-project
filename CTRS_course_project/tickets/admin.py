from django.contrib import admin

from CTRS_course_project.tickets.models import Ticket


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    ...
