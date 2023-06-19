from django.urls import path, include

from CTRS_course_project.common.views import index

urlpatterns = [
    path('', index, name='index'),
]
