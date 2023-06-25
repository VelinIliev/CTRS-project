from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render

from CTRS_course_project.tickets.forms import CreateTicketForm
from CTRS_course_project.tickets.models import Ticket


def index_tickets(request):
    return HttpResponse("index_tickets")


class CreateTicketView(LoginRequiredMixin, views.CreateView):
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


class EditTicketView(LoginRequiredMixin, views.UpdateView):
    login_url = "/profile/login/"
    template_name = 'tickets/edit-ticket-page.html'
    model = Ticket
    fields = '__all__'
    success_url = reverse_lazy('tickets index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DeleteTicketView(LoginRequiredMixin, views.DeleteView):
    template_name = 'halls/hall-delete-page.html'
    model = Ticket
    success_url = reverse_lazy('tickets index')
