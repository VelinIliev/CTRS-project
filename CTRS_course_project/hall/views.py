from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from CTRS_course_project.hall.forms import CreateHallForm
from CTRS_course_project.hall.models import Hall


def index_hall(request):
    return HttpResponse("Hall index")


class CreateHallView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = 'hall.add_hall'
    login_url = "/profile/login/"
    template_name = 'halls/hall-create-page.html'
    form_class = CreateHallForm

    def get_success_url(self):
        return reverse_lazy('details hall', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DisplayHallView(views.ListView):
    template_name = 'halls/halls-main-page.html'
    model = Hall

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['halls'] = Hall.objects.all().order_by('-id')
        return context


class HallDetailsView(views.DetailView):
    template_name = 'halls/hall-details-page.html'
    model = Hall

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        context['total_seats'] = self.object.rows * self.object.seats_per_row
        context['rows'] = range(self.object.rows)
        context['seats'] = range(self.object.seats_per_row)
        return context


class EditHallView(LoginRequiredMixin, PermissionRequiredMixin,  views.UpdateView):
    permission_required = 'hall.change_hall'
    login_url = "/profile/login/"
    template_name = 'halls/hall-edit-page.html'
    model = Hall
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('details hall', kwargs={'pk': self.object.pk, 'slug': self.object.slug})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DeleteHallView(LoginRequiredMixin, PermissionRequiredMixin, views.DeleteView):
    permission_required = 'hall.delete_hall'
    template_name = 'halls/hall-delete-page.html'
    model = Hall
    success_url = reverse_lazy('hall index')
