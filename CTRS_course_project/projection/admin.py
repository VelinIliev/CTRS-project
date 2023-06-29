from django.contrib import admin

from CTRS_course_project.projection.models import Projection


@admin.register(Projection)
class ProjectionAdmin(admin.ModelAdmin):
    ...