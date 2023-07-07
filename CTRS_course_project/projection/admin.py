from django.contrib import admin

from CTRS_course_project.projection.models import Projection


@admin.register(Projection)
class ProjectionAdmin(admin.ModelAdmin):
    list_filter = ['hall', 'date', 'movie']
    ordering = ['hall', 'movie', 'date', 'hour']
    list_display = ['hall', 'movie', 'date', 'formatted_hour']
    search_fields = ['movie__title', 'hall__name']

    def formatted_hour(self, obj):
        return obj.hour.strftime('%H:%M')

    formatted_hour.short_description = 'Hour'
