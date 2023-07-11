from django.urls import path
from .signals import *

from CTRS_course_project.user_app.views import index, SignInView, SignUpView, SignOutView, UserDetailsView, \
    UserEditView, UserDeleteView, CreateUpStaffView

urlpatterns = [
    path('', index, name='profile index'),
    path('login/', SignInView.as_view(), name='login'),
    path('logout/', SignOutView.as_view(), name='logout'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('register/staff/', CreateUpStaffView.as_view(), name='register staff user'),
    path('details/<int:pk>/', UserDetailsView.as_view(), name='details user'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete user'),
    path('edit/<int:pk>/', UserEditView.as_view(), name='edit user'),
]
