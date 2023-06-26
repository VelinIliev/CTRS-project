from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CTRS_course_project.common.urls')),
    path('profile/', include('CTRS_course_project.user_app.urls')),
    path('movie/', include('CTRS_course_project.movies.urls')),
    path('hall/', include('CTRS_course_project.hall.urls')),
    path('projection/', include('CTRS_course_project.projection.urls')),
    path('ticket/', include('CTRS_course_project.tickets.urls')),
    path('resrvation/', include('CTRS_course_project.reservation.urls')),
]
