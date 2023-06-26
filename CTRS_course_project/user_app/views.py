from django.contrib.auth import views as auth_view, get_user_model
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy

from CTRS_course_project.reservation.models import Reservation
from CTRS_course_project.user_app.forms import UserCreateForm, UserCreateStaffForm

UserModel = get_user_model()


def index(request):
    return HttpResponse('profile index')


class SignInView(auth_view.LoginView):
    template_name = 'accounts/login-page.html'
    success_url = reverse_lazy('index')


class SignUpView(views.CreateView):
    template_name = 'accounts/register-user.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('index')


class CreateUpStaffView(views.CreateView):
    template_name = 'accounts/register-staff-user.html'
    form_class = UserCreateStaffForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        context['reservations'] = Reservation.objects.filter(user=self.object.pk, is_finished=True)
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'age', 'email')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk, })


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')
