import datetime

from django.contrib.auth import views as auth_view, get_user_model, login
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.db.models import Q, Count
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic as views

from CTRS_course_project.reservation.models import Reservation
from CTRS_course_project.user_app.forms import UserCreateForm, UserCreateStaffForm
from CTRS_course_project.user_app.models import AppUser

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

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect(self.success_url)


class CreateUpStaffView(PermissionRequiredMixin, views.CreateView):
    permission_required = 'user_app.add_appuser'
    template_name = 'accounts/register-staff-user.html'
    form_class = UserCreateStaffForm
    success_url = reverse_lazy('list staff users')


class SignOutView(auth_view.LogoutView):
    next_page = reverse_lazy('index')


class UserDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        today = datetime.datetime.now().date()
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        groups = self.object.groups.all()
        context['groups'] = ", ".join(str(x) for x in groups) if groups else "No groups"
        context['new_reservations'] = Reservation.objects \
            .filter(
            user=self.object.pk,
            is_finished=True,
            projection__date__gte=today,
        ) \
            .order_by(
            'projection__date',
            'projection__hour'
        )
        context['old_reservations'] = Reservation.objects \
            .filter(
            user=self.object.pk,
            is_finished=True,
            projection__date__lt=today,
        ) \
            .order_by(
            'projection__date',
            'projection__hour'
        )
        return context


class UserEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'
    model = UserModel
    fields = ('first_name', 'last_name', 'age', 'email')

    def get_success_url(self):
        return reverse_lazy('details user', kwargs={'pk': self.request.user.pk, })

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class UserDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'
    model = UserModel
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_owner'] = self.request.user == self.object
        return context


class ListStaffUsersView(LoginRequiredMixin, PermissionRequiredMixin, views.ListView):
    permission_required = 'user_app.view_appuser'
    login_url = "/profile/login/"
    template_name = 'accounts/profile-list-staff-page.html'
    model = UserModel

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        staff_users = UserModel.objects.filter(is_staff=True, is_superuser=False).order_by('username')
        staff_groups = []
        for staff in staff_users:
            groups = staff.groups.all()
            staff_groups.append((staff.username, ", ".join(str(x) for x in groups) if groups else "No groups"))
        context['staff_users'] = staff_groups
        return context

    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     queryset = queryset.filter(is_staff=True) \
    #         .annotate(group_count=Count('groups')) \
    #         .filter(group_count__gt=0).values_list('username', 'groups__name', 'id') \
    #         .order_by('username')
    #     return queryset
