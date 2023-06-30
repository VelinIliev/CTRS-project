from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic as views

from CTRS_course_project.tickets.forms import CreateTicketForm
from CTRS_course_project.tickets.models import Ticket


def index_tickets(request):
    return HttpResponse("index_tickets")


class CreateTicketView(LoginRequiredMixin, PermissionRequiredMixin, views.CreateView):
    permission_required = 'tickets.add_ticket'
    login_url = "/profile/login/"
    template_name = 'tickets/create-ticket-page.html'
    form_class = CreateTicketForm
    success_url = reverse_lazy('tickets index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class ListTicketView(views.ListView):
    template_name = 'tickets/list-ticket-page.html'
    model = Ticket

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class EditTicketView(LoginRequiredMixin, PermissionRequiredMixin, views.UpdateView):
    permission_required = 'tickets.add_ticket'
    login_url = "/profile/login/"
    template_name = 'tickets/edit-ticket-page.html'
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('tickets index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DeleteTicketView(LoginRequiredMixin, PermissionRequiredMixin, views.DeleteView):
    permission_required = 'tickets.delete_ticket'
    template_name = 'tickets/delete-ticket-page.html'
    login_url = "/profile/login/"
    model = Ticket
    success_url = reverse_lazy('tickets index')
