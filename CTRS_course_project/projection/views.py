from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render, redirect

from CTRS_course_project.hall.models import Hall
from CTRS_course_project.projection.forms import CreateProjectionForm
from CTRS_course_project.projection.helpers import create_seats, get_seats
from CTRS_course_project.projection.models import Projection, Seat


def index(request):
    return HttpResponse("projection index")


class DisplayProjectionView(views.ListView):
    template_name = 'projections/display-projections-page.html'
    model = Projection


class CreateProjectionView(LoginRequiredMixin, views.CreateView):
    login_url = "/profile/login/"
    template_name = 'projections/create-projection-page.html'
    form_class = CreateProjectionForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_staff'] = self.request.user.is_staff
        return context


class DetailsProjectionView(LoginRequiredMixin, views.DetailView):
    template_name = 'projections/details-projection-view.html'
    model = Projection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['seats'] = get_seats(self.object)
        return context


def reservations(request):
    if request.method == "GET":
        return redirect('index')
    elif request.method == "POST":
        print(f'values: {request.POST.get("type")}')
        values = [int(x) for x in request.POST.get("type").split(", ")]
        print(values)
        for v in values:
            Seat.objects.filter(pk=v).update(is_taken=True)

    return redirect('projection index')
