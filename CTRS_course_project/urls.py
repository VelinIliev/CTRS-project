from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('CTRS_course_project.common.urls')),
    path('profile/', include('CTRS_course_project.user_app.urls')),
]
