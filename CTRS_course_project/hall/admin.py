from django.contrib import admin

from CTRS_course_project.hall.models import Hall


@admin.register(Hall)
class HallAdmin(admin.ModelAdmin):
    ...