from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic as views
from django.http import HttpResponse
from django.shortcuts import render

from CTRS_course_project.hall.models import Hall
from CTRS_course_project.projection.forms import CreateProjectionForm
from CTRS_course_project.projection.helpers import create_seats
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
        # hall = Hall.objects.filter(pk=3).get()
        # seats = [[f'{r:02d}-{s:02d}' for s in range(1, hall.seats_per_row + 1)] for r in range(1, hall.rows + 1)]
        # context['seats'] = create_seats(hall)
        return context


class DetailsProjectionView(LoginRequiredMixin, views.DetailView):
    template_name = 'projections/details-projection-view.html'
    model = Projection

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        seats = Seat.objects.filter(projection_id=self.object.id).order_by('row_n', 'seat_n')
        final_seats = []
        for row in range(1, self.object.hall.rows + 1):
            new_row = []
            for seat in range(1, self.object.hall.seats_per_row + 1):
                new_row.append(
                    Seat.objects.filter(projection_id=self.object.id, row_n=f'{row:02d}', seat_n=f'{seat:02d}').get())
            final_seats.append(new_row)
        context['seats'] = final_seats
        return context
